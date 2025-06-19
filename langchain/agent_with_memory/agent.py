import os
from typing import TypedDict, Annotated, List
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from neo4j import GraphDatabase
import json
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
# Neo4j Memory Manager
class Neo4jMemory:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self._create_constraints()
    
    def _create_constraints(self):
        """Create necessary constraints and indexes"""
        with self.driver.session() as session:
            # Create constraint for conversation nodes
            session.run("""
                CREATE CONSTRAINT conversation_id IF NOT EXISTS 
                FOR (c:Conversation) REQUIRE c.id IS UNIQUE
            """)
            
            # Create constraint for message nodes
            session.run("""
                CREATE CONSTRAINT message_id IF NOT EXISTS 
                FOR (m:Message) REQUIRE m.id IS UNIQUE
            """)
    
    def store_message(self, conversation_id: str, message: BaseMessage, message_id: str = None):
        """Store a message in Neo4j"""
        if message_id is None:
            message_id = f"{conversation_id}_{datetime.now().timestamp()}"
        
        message_type = "Human" if isinstance(message, HumanMessage) else "AI"
        
        with self.driver.session() as session:
            session.run("""
                MERGE (c:Conversation {id: $conversation_id})
                CREATE (m:Message {
                    id: $message_id,
                    type: $message_type,
                    content: $content,
                    timestamp: datetime()
                })
                CREATE (c)-[:CONTAINS]->(m)
            """, 
            conversation_id=conversation_id,
            message_id=message_id,
            message_type=message_type,
            content=message.content
            )
    
    def get_conversation_history(self, conversation_id: str, limit: int = 10) -> List[BaseMessage]:
        """Retrieve conversation history from Neo4j"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Conversation {id: $conversation_id})-[:CONTAINS]->(m:Message)
                RETURN m.type as type, m.content as content, m.timestamp as timestamp
                ORDER BY m.timestamp
                LIMIT $limit
            """, conversation_id=conversation_id, limit=limit)
            
            messages = []
            for record in result:
                if record["type"] == "Human":
                    messages.append(HumanMessage(content=record["content"]))
                else:
                    messages.append(AIMessage(content=record["content"]))
            
            return messages
    
    def close(self):
        """Close the Neo4j connection"""
        self.driver.close()

# Define the agent state
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    conversation_id: str

# Agent class
class Neo4jAgent:
    def __init__(self, groq_api_key: str, neo4j_uri: str, neo4j_user: str, neo4j_password: str):
        # Initialize ChatGroq
        self.llm = ChatGroq(
            
            model="Gemma2-9b-It",  # You can change this to other Groq models
            temperature=0.7
        )
        
        # Initialize Neo4j memory
        self.memory = Neo4jMemory(neo4j_uri, neo4j_user, neo4j_password)
        
        # Create the prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful AI assistant with access to conversation history. 
            Use the context from previous messages to provide relevant and coherent responses.
            Be conversational and remember what has been discussed before."""),
            ("placeholder", "{messages}")
        ])
        
        # Build the graph
        self.graph = self._build_graph()
    
    def _build_graph(self):
        """Build the LangGraph workflow"""
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("load_memory", self._load_memory)
        workflow.add_node("process", self._process_message)
        workflow.add_node("save_memory", self._save_memory)
        
        # Define the flow
        workflow.set_entry_point("load_memory")
        workflow.add_edge("load_memory", "process")
        workflow.add_edge("process", "save_memory")
        workflow.add_edge("save_memory", END)
        
        return workflow.compile()
    
    def _load_memory(self, state: AgentState):
        """Load conversation history from Neo4j"""
        conversation_id = state["conversation_id"]
        
        # Get previous messages from Neo4j
        previous_messages = self.memory.get_conversation_history(conversation_id, limit=10)
        
        # Combine with current messages
        all_messages = previous_messages + state["messages"]
        
        return {"messages": all_messages, "conversation_id": conversation_id}
    
    def _process_message(self, state: AgentState):
        """Process the message with the LLM"""
        # Format messages for the prompt
        formatted_prompt = self.prompt.format_messages(messages=state["messages"])
        
        # Get response from Groq
        response = self.llm.invoke(formatted_prompt)
        
        # Add the AI response to messages
        updated_messages = state["messages"] + [response]
        
        return {"messages": updated_messages, "conversation_id": state["conversation_id"]}
    
    def _save_memory(self, state: AgentState):
        """Save new messages to Neo4j"""
        conversation_id = state["conversation_id"]
        
        # Save the last human message and AI response
        if len(state["messages"]) >= 2:
            # Save the human message (second to last)
            human_msg = state["messages"][-2]
            if isinstance(human_msg, HumanMessage):
                self.memory.store_message(conversation_id, human_msg)
            
            # Save the AI response (last message)
            ai_msg = state["messages"][-1]
            if isinstance(ai_msg, AIMessage):
                self.memory.store_message(conversation_id, ai_msg)
        
        return state
    
    def chat(self, message: str, conversation_id: str = "default"):
        """Main chat method"""
        # Create initial state
        initial_state = {
            "messages": [HumanMessage(content=message)],
            "conversation_id": conversation_id
        }
        
        # Run the graph
        result = self.graph.invoke(initial_state)
        
        # Return the last AI message
        return result["messages"][-1].content
    
    def close(self):
        """Close connections"""
        self.memory.close()

# Example usage
def main():
    # Configuration - replace with your actual credentials
    GROQ_API_KEY="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",
    NEO4J_URI = "neo4j://127.0.0.1:7687"  # Default Neo4j URI
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = "password"
    
    # Initialize the agent
    agent = Neo4jAgent(
        groq_api_key=GROQ_API_KEY,
        neo4j_uri=NEO4J_URI,
        neo4j_user=NEO4J_USER,
        neo4j_password=NEO4J_PASSWORD
    )
    
    try:
        # Example conversation
        conversation_id = "user_123"
        
        print("Agent: Hello! I'm your AI assistant with memory. What would you like to talk about?")
        
        # Simulate a conversation
        responses = [
            "Hi, my name is Alice and I love programming.",
            "What programming languages do you think I should learn?",
            "Do you remember my name?",
            "What did we talk about programming languages?"
        ]
        
        for user_input in responses:
            print(f"User: {user_input}")
            response = agent.chat(user_input, conversation_id)
            print(f"Agent: {response}\n")
        
        # Interactive mode (uncomment to use)
        # while True:
        #     user_input = input("You: ")
        #     if user_input.lower() in ['quit', 'exit', 'bye']:
        #         break
        #     
        #     response = agent.chat(user_input, conversation_id)
        #     print(f"Agent: {response}")
    
    finally:
        # Clean up
        agent.close()

if __name__ == "__main__":
    main()
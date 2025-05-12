from typing import TypedDict
from langgraph.graph import END, StateGraph

# Define the state type
class MyState(TypedDict, total=False):
    greeting: str

# Define a node
def hello_node(state: MyState) -> MyState:
    print("Hello!")
    state['greeting'] = "Hello from langgraph"
    return state

# Build the graph
graph = StateGraph(MyState)
graph.add_node("hello", hello_node)

# This tells LangGraph to go from "hello" node to END
graph.add_edge("hello", END)

graph.set_entry_point("hello")
# graph.set_finish_point(END)

# Compile the app
app = graph.compile()

# Invoke the app
output = app.invoke({})
print(output)

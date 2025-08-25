import asyncio
import logging
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Load environment variables from .env
load_dotenv()

# Neo4j connection settings
NEO4J_URI = os.getenv("NEO4J_URI", "neo4j://127.0.0.1:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# Validate
if not all([NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD]):
    raise ValueError("Missing Neo4j connection info in environment variables.")

# Main async function
async def main():
    graphiti = Graphiti(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
    try:
        # Setup indices once
        await graphiti.build_indices_and_constraints()

        # Read full raw text file
        with open("/home/abhishek/daily/tasks/langchain/agent_with_memory/info_text.txt", "r") as f:
            full_text = f.read().strip()

        # Index entire document as a single episode
        await graphiti.add_episode(
            name="complete_chat",
            episode_body=full_text,
            source=EpisodeType.text,
            source_description="Full assistant-user conversation as one session",
            reference_time=datetime.now(timezone.utc),
        )

        logger.info("Episode successfully added and indexed.")

    finally:
        await graphiti.close()
        logger.info("Connection closed")

# Entry point
if __name__ == "__main__":
    asyncio.run(main())

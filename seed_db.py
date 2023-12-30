import datetime
from pymongo import MongoClient, TEXT

client = MongoClient("mongodb://localhost:27017/")
db = client["gpt_database"]

# Define the Conversations collection
conversations = db["conversations"]

# Create text indexes for fuzzy search on query and response fields
conversations.create_index([("query", TEXT), ("response", TEXT)])

# Example document:
conversation_entry = {
    "conversation_id": "some_session_id",
    "timestamp": datetime.datetime.utcnow(),
    "query": "some_query",
    "response": "some_response",
    "system_message": "some_system_message",  # Or a reference to the SystemMessages collection
}

# Inserting the document
conversations.insert_one(conversation_entry)

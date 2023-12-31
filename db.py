import datetime
from pymongo import MongoClient
from enum import Enum
from dtypes import Role


client = MongoClient("mongodb://localhost:27017/")
db = client["gpt_database"]

# Define the Conversations collection
conversations = db["conversations"]


def load_conversation(conversation_id):
    conversation = conversations.find({"conversation_id": conversation_id})
    return conversation


def get_last_conversation_id():
    last_conversation = conversations.find_one(sort=[("timestamp", -1)])
    if last_conversation:
        return last_conversation["conversation_id"]
    else:
        return None


def add_record(conversation_id, query, response, system_message):
    conversation_entry = {
        "conversation_id": conversation_id,
        "timestamp": datetime.datetime.utcnow(),
        "query": query,
        "response": response,
        "system_message": system_message,
    }
    conversations.insert_one(conversation_entry)


def search_conversations(search_term):
    search_results = conversations.find({"$text": {"$search": search_term}})
    return list(search_results)

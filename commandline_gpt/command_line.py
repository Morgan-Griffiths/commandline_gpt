import os
import sys
import uuid
import click
from system_messages import CHATGPT_IDENTITY
import openai
from db import (
    add_record,
    search_conversations,
    get_last_conversation_id,
    load_conversation,
)
from utils import get_gpt_response,construct_conversation

openai.api_key = os.getenv("OPENAI_API_KEY")

@click.command()
@click.argument("query", type=str, required=False)
@click.option("-c", "--cont", is_flag=True, help="Continue the last conversation")
@click.option("-s", "--search", type=str, help="Search term for fuzzy search")
def cli(query, cont, search):
    if not sys.stdin.isatty():  # If there is a pipe
        conversation_id = get_last_conversation_id()
        code_with_prompt = sys.stdin.read()
        response = get_gpt_response(code_with_prompt)
        add_record(conversation_id, query, response, CHATGPT_IDENTITY)
        click.echo(response)
    
    elif search:
        results = search_conversations(search)
        for result in results:
            click.echo(
                f"Conversation ID: {result['conversation_id']}, Query: {result['query']}, Response: {result['response']}"
            )
    else:
        if cont:
            # get latest conversation id
            conversation_id = get_last_conversation_id()

            if not conversation_id:
                click.echo("Please start a new conversation with the -n flag.")
                return
            # load conversation from db
            conversations = load_conversation(conversation_id)
            # Process the query
            message_history = construct_conversation(conversations)
            response = get_gpt_response(message_history + '\n\nUser:\n' + query)
            add_record(conversation_id, query, response, CHATGPT_IDENTITY)
            click.echo(response)
        else:
            conversation_id = str(uuid.uuid4())
            # Process the query
            response = get_gpt_response(query)

            # Add the record to MongoDB
            add_record(conversation_id, query, response, CHATGPT_IDENTITY)

            click.echo(response)


if __name__ == "__main__":
    cli()

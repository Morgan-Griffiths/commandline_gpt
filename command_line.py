import os
import sys
import uuid
import click
import config
from db import (
    add_record,
    search_conversations,
    get_last_conversation_id,
    load_conversation,
    update_conversation,
)
from utils import get_gpt_response


@click.command()
@click.argument("query", type=str, required=False)
@click.option("-c", "--cont", is_flag=True, help="Continue a conversation")
@click.option(
    "-s",
    "--system_message",
    type=click.Choice(config.SYSTEM_MESSAGES, case_sensitive=False),
    help="Set system message",
)
@click.option("-s", "--search", type=str, help="Search term for fuzzy search")
def cli(query, cont, system_message, search):
    if not sys.stdin.isatty():  # If there is a pipe
        conversation_id = get_last_conversation_id()
        code_with_prompt = sys.stdin.read()
        response = get_gpt_response(code_with_prompt)
        add_record(conversation_id, query, response, system_message)
        click.echo(response)
    if query:
        if system_message:
            config.set_system_message(system_message)
        if cont:
            # get latest conversation id
            conversation_id = get_last_conversation_id()

            if not conversation_id:
                click.echo("Please start a new conversation with the -n flag.")
                return
            click.echo(f"Continuing conversation with ID: {conversation_id}")
            # load conversation from db
            conversation = load_conversation(conversation_id)

        else:
            conversation_id = str(uuid.uuid4())
            click.echo(f"New conversation started with ID: {conversation_id}")
            # Process the query
            response = get_gpt_response(query)

            # Add the record to MongoDB
            add_record(conversation_id, query, response, system_message)

            click.echo(response)
    elif search:
        print("here")
        results = search_conversations(search)
        print("here")
        for result in results:
            click.echo(
                f"Conversation ID: {result['conversation_id']}, Query: {result['query']}, Response: {result['response']}"
            )


if __name__ == "__main__":
    cli()

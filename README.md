# Introduction

This is a minimalist commandline tool for interacting and piping text to GPT. It uses MongoDB to store the conversations and allow for fuzzy search.

# Setup

## Install MongoDB

Follow the instructions here: https://www.mongodb.com/docs/manual/administration/install-community/

## Install the python dependencies with poetry

`pip install poetry`
`poetry install`

## Set up an alias (optional)

Add this to your .bashrc or .zshrc
`alias g="python ~/code/commandline_gpt/main.py"`

# Usage

## Start a conversation

`g <prompt>`

## Continue the last conversation

`g -c <prompt>`

## Fuzzy search through conversations

`g -s <search term>`

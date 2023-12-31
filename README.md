# Introduction

This is a minimalist commandline tool for interacting and piping text to GPT. It uses MongoDB to store the conversations and allow for fuzzy search.

# Setup

## Install MongoDB

Follow the instructions here: https://docs.mongodb.com/manual/installation/

## Install Python requirements

`pip install -r requirements.txt`

## Set up an alias

Add this to your .bashrc or .zshrc
`alias g="python ~/code/commandline_gpt/command_line.py"`

# Usage

## Start a conversation

`g <prompt>`

## Continue a conversation

`g`

## Fuzzy search through conversations

`g <search term>`

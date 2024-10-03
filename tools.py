from langchain.agents import Tool
from langchain.tools import BaseTool
from langchain.tools import StructuredTool
import streamlit as st
from datetime import date
from dotenv import load_dotenv
import json
import re
import os
from document_db import DocumentDb

load_dotenv()

def get_current_user(input: str):
    db = DocumentDb()
    user = db.get_user(1)  # Assuming userId 1 is the current user
    db.close()
    return user

get_current_user_tool = Tool(
    name='GetCurrentUser',
    func=get_current_user,
    description="Returns the current user for querying documents."
)

def get_documents(userId: str):
    """Returns the documents associated with the provided userId by running the query: SELECT * FROM Documents WHERE userId = ?."""
    try:
        db = DocumentDb()
        documents = db.get_user_documents(userId)
        db.close()
        return documents
    except Exception as e:
        return f"Error: {e}'"

get_recent_documents_tool = Tool(
    name='GetUserDocuments',
    func=get_documents,
    description="Returns the documents associated with the provided userId by running the query: SELECT * FROM Documents WHERE userId = provided_userId."
)
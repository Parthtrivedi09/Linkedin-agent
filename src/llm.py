from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
llm=ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.7
)
# llm_engine.py
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class SQLResponse:
    def __init__(self, sql_query, explanation):
        self.sql_query = sql_query
        self.explanation = explanation

def generate_sql(user_question: str, db_schema: str) -> SQLResponse:
    """Generates a structured SQL query using Groq Cloud API with updated models."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ Error: GROQ_API_KEY is missing from your .env file.")
        return None
        
    client = Groq(api_key=api_key)
    
    system_prompt = f"""
    You are an expert text-to-SQL data analyst. 
    You must output a raw JSON object string matching this exact pattern:
    {{
        "sql_query": "SELECT * FROM customers;",
        "explanation": "Description goes here"
    }}
    
    Database Layout Schema:
    {db_schema}
    
    Rules:
    1. Only use table and column names explicitly defined above.
    2. Never use markdown code backticks like ```json or ``` anywhere in your output.
    3. Output raw text string only. No pleasantries.
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Updated to the currently active model
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Question: {user_question}"}
            ],
            temperature=0.0,
            response_format={"type": "json_object"} 
        )
        
        raw_text = response.choices[0].message.content.strip()
        
        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]
        raw_text = raw_text.strip()
        
        data = json.loads(raw_text)
        return SQLResponse(sql_query=data["sql_query"], explanation=data["explanation"])
        
    except Exception as e:
        print(f"❌ Groq Parsing Error Encountered: {e}")
        return None
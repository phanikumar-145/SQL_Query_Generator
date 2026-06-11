# test_ai.py
import os
from dotenv import load_dotenv
from llm_engine import generate_sql

load_dotenv()

print("\n=============================================")
print("       --- GROQ ENGINE DIAGNOSTICS ---       ")
print("=============================================")
print(f"Checking .env Configuration... Key Found: {'Yes' if os.getenv('GROQ_API_KEY') else 'No'}")

mock_schema = """
Table: customers
Columns:
 - customer_id (integer)
 - first_name (character varying)
 - last_name (character varying)
"""

test_question = "Show me all customers"

print("\nSending request payload to Groq Cloud...")
response = generate_sql(test_question, mock_schema)

if response:
    print("✅ SUCCESS: Groq parsed structured response cleanly!")
    print(f"SQL: {response.sql_query}")
    print(f"Explanation: {response.explanation}")
else:
    print("❌ FAILED: Go look at the RAW TEXT print log above to see why it broke.")
print("=============================================\n")
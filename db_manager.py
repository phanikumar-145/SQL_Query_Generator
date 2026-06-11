# db_manager.py
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Establishes a connection to your local PostgreSQL server."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def fetch_database_schema() -> str:
    """Programmatically extracts table layouts for Groq context."""
    schema_text = ""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute("""
            SELECT table_name, column_name, data_type 
            FROM information_schema.columns 
            WHERE table_schema = 'public'
            ORDER BY table_name, ordinal_position;
        """)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        
        if not rows:
            return "No tables found in the 'public' schema of SQL_db."
            
        current_table = ""
        for row in rows:
            if row['table_name'] != current_table:
                current_table = row['table_name']
                schema_text += f"\nTable: {current_table}\nColumns:\n"
            schema_text += f" - {row['column_name']} ({row['data_type']})\n"
            
    except Exception as e:
        schema_text = f"Error connection or fetching schema: {str(e)}"
        
    return schema_text

def execute_sql_query(sql_query: str):
    """Executes the Groq-generated SQL query directly on SQL_db."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results, None
    except Exception as e:
        return None, str(e)
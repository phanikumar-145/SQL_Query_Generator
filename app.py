# app.py
import streamlit as st
import pandas as pd
from db_manager import fetch_database_schema, execute_sql_query
from llm_engine import generate_sql

st.set_page_config(page_title="Groq SQL Analyst", page_icon="⚡", layout="wide")

st.title("⚡ Groq Natural Language to SQL Assistant")
st.caption("Powered by Llama-3 via Groq Cloud Engine")

# Read database schema right away
schema_context = fetch_database_schema()

# Sidebar Setup
st.sidebar.header("System Settings")
st.sidebar.success("Connected to SQL_db")
with st.sidebar.expander("Inspected DB Columns"):
    st.code(schema_context, language="text")

# User prompt field
user_question = st.text_input(
    "What metrics would you like to retrieve from your database?",
    placeholder="e.g., Show me all details for customer Phani Kumar"
)

if st.button("Generate & Execute Query", type="primary"):
    if not user_question.strip():
        st.warning("Please specify a data analytics question first.")
    elif "Error" in schema_context or "No tables found" in schema_context:
        st.error("Cannot proceed. Please run your setup script to seed tables into SQL_db first.")
    else:
        # Step 1: Query processing via Groq
        with st.spinner("Groq engine processing syntax..."):
            ai_response = generate_sql(user_question, schema_context)
            
        if ai_response:
            st.markdown("### 🛠️ Generated SQL Query")
            st.code(ai_response.sql_query, language="sql")
            st.info(f"💡 **AI Logic Statement:** {ai_response.explanation}")
            
            # Step 2: Query running on local Postgres database
            st.markdown("### 📊 Fetched Rows Result")
            with st.spinner("Extracting records from PostgreSQL..."):
                rows, error = execute_sql_query(ai_response.sql_query)
                
            if error:
                st.error(f"PostgreSQL Compile/Execution Error: {error}")
            elif rows:
                df = pd.DataFrame(rows)
                st.dataframe(df, use_container_width=True)
                st.success(f"Successfully loaded {len(df)} records.")
            else:
                st.info("Query compiled successfully but returned 0 conditional matches.")
        else:
            st.error("Groq application layer failed to unpack a structured response configuration object.")
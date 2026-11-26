# ⚡ AI-Powered SQL Query Generator

An AI-powered Natural Language to SQL application built using **Python, Streamlit, Groq API, Llama 3, and PostgreSQL**.

Convert everyday English questions into SQL queries and retrieve database information without manually writing SQL statements.

## 📌 Project Overview

Working with databases often requires knowledge of SQL, which can be challenging for non-technical users.

The **AI-Powered SQL Query Generator** simplifies database interaction by allowing users to communicate with databases using natural language.

The application uses a Large Language Model (LLM) through the Groq API to understand user questions, analyze the database schema, and generate relevant SQL queries.

The generated SQL query is then executed against a PostgreSQL database, and the retrieved results are displayed through an interactive Streamlit interface.

## 🎯 Project Objectives

- Convert natural language questions into SQL queries.
- Integrate Large Language Models into database applications.
- Automate SQL query generation using Generative AI.
- Retrieve database schema dynamically.
- Execute AI-generated queries against PostgreSQL.
- Display database results in an interactive interface.
- Explain generated SQL queries in understandable language.
- Simplify database access for non-technical users.

## ✨ Key Features

### 1. Natural Language to SQL

- Accepts questions in simple English.
- Understands user requirements using an LLM.
- Generates SQL queries automatically.
- Reduces the need for manually writing SQL statements.

### 2. AI-Powered SQL Generation

- Integrates Groq Cloud API.
- Uses Llama 3 for natural language understanding.
- Generates SQL based on database schema.
- Provides explanations for generated queries.

### 3. Dynamic Database Schema Extraction

- Connects to PostgreSQL.
- Retrieves available database tables.
- Extracts table names and column information.
- Provides database schema as context to the LLM.

### 4. PostgreSQL Integration

- Executes generated SQL queries.
- Retrieves database records.
- Handles database connection errors.
- Displays query results in tabular format.

### 5. Interactive Streamlit Interface

- Simple and user-friendly interface.
- Natural language question input.
- Displays generated SQL queries.
- Shows AI-generated explanations.
- Displays database query results.
- Provides execution status messages.

### 6. Database Setup

- Automatically creates sample database tables.
- Inserts sample customer records.
- Creates customer-order relationships.
- Provides sample data for testing.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Groq API | LLM inference |
| Llama 3 | Natural language understanding and SQL generation |
| PostgreSQL | Relational database |
| Psycopg2 | PostgreSQL connectivity |
| Pandas | Query result processing |
| Python-Dotenv | Environment variable management |

## 🏗️ System Architecture

```text
          User Natural Language Question
                       |
                       v
               Streamlit Interface
                       |
                       v
              Database Schema Fetch
                       |
                       v
                 Groq API
                       |
                       v
                 Llama 3 LLM
                       |
                       v
                SQL Generation
                       |
                       v
             SQL Query Explanation
                       |
                       v
              PostgreSQL Database
                       |
                       v
               Query Execution
                       |
                       v
              Retrieve DB Records
                       |
                       v
               Pandas DataFrame
                       |
                       v
             Display Results in UI
```

## 📂 Project Structure

```text
SQL_Query_Generator/
│
├── app.py
├── db_manager.py
├── llm_engine.py
├── setup_db.py
├── test_ai.py
├── requirements.txt
├── .env
└── README.md
```

### File Descriptions

| File | Description |
|---|---|
| `app.py` | Main Streamlit application and user interface |
| `db_manager.py` | Handles PostgreSQL connections, schema extraction, and SQL execution |
| `llm_engine.py` | Integrates Groq API and generates SQL queries using Llama 3 |
| `setup_db.py` | Creates database tables and inserts sample records |
| `test_ai.py` | Tests the AI-based SQL generation functionality |
| `requirements.txt` | Contains required Python dependencies |
| `.env` | Stores sensitive configuration variables locally |

## 🗄️ Database Design

The project uses PostgreSQL with two main tables.

### 1. Customers Table

| Column | Description |
|---|---|
| customer_id | Unique customer identifier |
| first_name | Customer first name |
| last_name | Customer last name |
| email | Customer email address |
| join_date | Customer registration date |

### 2. Orders Table

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| customer_id | References the customer |
| order_date | Order creation date |
| total_amount | Total order amount |
| status | Current order status |

**Relationship:** One customer can have multiple orders. The `customer_id` column connects the two tables.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/phanikumar-145/SQL_Query_Generator.git
```

### Step 2: Navigate to the Project

```bash
cd SQL_Query_Generator
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Environment

For Windows PowerShell:

```powershell
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure PostgreSQL

1. Install PostgreSQL.
2. Open pgAdmin.
3. Create a database named `SQL_db`.
4. Configure your PostgreSQL connection details.

### Step 7: Configure Environment Variables

Create a `.env` file in the project root directory.

Add:

```env
GROQ_API_KEY=your_groq_api_key

DB_HOST=localhost
DB_NAME=SQL_db
DB_USER=postgres
DB_PASSWORD=your_database_password
DB_PORT=5432
```

Get your Groq API key from:

https://console.groq.com/keys

Never upload your actual API keys or database passwords to GitHub.

### Step 8: Initialize the Database

Run:

```bash
python setup_db.py
```

This creates the required tables and inserts sample customer and order records.

### Step 9: Run the Application

```bash
streamlit run app.py
```

The application will open at:

http://localhost:8501

## 💡 Example Usage

Enter a question in natural language:

**Example 1:**

```text
Show me all customers.
```

Generated SQL:

```sql
SELECT * FROM customers;
```

**Example 2:**

```text
Show me all completed orders.
```

Generated SQL:

```sql
SELECT *
FROM orders
WHERE status = 'Completed';
```

**Example 3:**

```text
Show customer names and their total order amounts.
```

Generated SQL:

```sql
SELECT
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS total_amount
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;
```

*These are illustrative examples of the expected functionality.*

## 🔄 Application Workflow

1. User enters a question in natural language.
2. Streamlit receives the question.
3. The application retrieves the PostgreSQL database schema.
4. The schema and user question are passed to the Groq LLM.
5. Llama 3 generates the corresponding SQL query.
6. The application displays the generated query and its explanation.
7. The generated query is executed against PostgreSQL.
8. Retrieved records are converted into a Pandas DataFrame.
9. Results are displayed in the Streamlit interface.

## 🧪 Testing

Run the AI integration diagnostic script:

```bash
python test_ai.py
```

This checks the Groq API configuration and tests whether the application can generate a structured SQL response.

## 🔐 Security Considerations

- Store API keys and database credentials in environment variables.
- Never expose database credentials in source code.
- Use a dedicated PostgreSQL user with minimum required permissions.
- Validate AI-generated SQL before execution.
- Restrict generated queries to approved read-only operations.
- Apply query timeouts and result limits.
- Avoid exposing internal database errors to end users.

**Important:** The current implementation executes generated SQL directly. It should not be exposed to untrusted users or production databases without SQL validation, read-only database permissions, and additional execution safeguards.

## 🌍 Real-World Applications

- Business intelligence systems.
- Database analytics platforms.
- Customer data analysis.
- Sales reporting applications.
- Business reporting automation.
- Internal data assistants.
- Natural language database interfaces.

## 🔮 Future Enhancements

- Add SQL query validation and safety checks.
- Support multiple database systems.
- Generate interactive charts from query results.
- Add query history and saved queries.
- Support complex SQL joins and nested queries.
- Add conversational database interaction.
- Implement user authentication.
- Add CSV and Excel export functionality.
- Introduce query optimization suggestions.
- Deploy the application using Docker and cloud services.

## 👨‍💻 Author

**Phani Kumar**

AI/ML & Generative AI Developer

- GitHub: https://github.com/phanikumar-145
- Project Repository: https://github.com/phanikumar-145/SQL_Query_Generator

---

⭐ If you find this project useful, consider giving it a star!

**Built with Python, Streamlit, Groq API, Llama 3, and PostgreSQL.**

# setup_db.py
from db_manager import get_db_connection

sql_script = """
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    join_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);

INSERT INTO customers (first_name, last_name, email, join_date) VALUES
('Phani', 'Kumar', 'phani@example.com', '2026-01-15'),
('Alice', 'Smith', 'alice@example.com', '2026-02-20')
ON CONFLICT (email) DO NOTHING;

INSERT INTO orders (customer_id, total_amount, status) VALUES
(1, 250.00, 'Completed'),
(2, 1200.00, 'Completed')
ON CONFLICT DO NOTHING;
"""

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_script)
    conn.commit()
    print("✅ Tables created and mock data populated successfully!")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Error running setup: {e}")
import sqlite3


def create_database():
    conn = sqlite3.connect("fraud_detection.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total_transactions INTEGER,
        normal_transactions INTEGER,
        fraud_transactions INTEGER,
        fraud_percentage REAL,
        prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_prediction(total, normal, fraud, percentage):
    conn = sqlite3.connect("fraud_detection.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO prediction_history
    (total_transactions, normal_transactions, fraud_transactions, fraud_percentage)
    VALUES (?, ?, ?, ?)
    """, (total, normal, fraud, percentage))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect("fraud_detection.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM prediction_history
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data
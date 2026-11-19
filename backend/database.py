
import os
import sqlite3

# Main project directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Database folder and file paths
DATABASE_DIR = os.path.join(BASE_DIR, "database")
DATABASE_PATH = os.path.join(
    DATABASE_DIR, "diamondiq.db"
)


# Create database and table
def initialize_database():

    # Create database folder if it does not exist
    os.makedirs(DATABASE_DIR, exist_ok=True)

    # Connect to SQLite database
    connection = sqlite3.connect(DATABASE_PATH)

    # Create prediction history table
    connection.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            carat REAL NOT NULL,
            cut TEXT NOT NULL,
            color TEXT NOT NULL,
            clarity TEXT NOT NULL,
            depth REAL NOT NULL,
            table_value REAL NOT NULL,
            x REAL NOT NULL,
            y REAL NOT NULL,
            z REAL NOT NULL,
            predicted_price REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully!")

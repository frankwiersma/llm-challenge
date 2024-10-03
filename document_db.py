import sqlite3
import time
import json 

class DocumentDb:
    def __init__(self, db_name="documents.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
        self.seed_data()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                userId INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Documents (
                documentId INTEGER PRIMARY KEY,
                userId INTEGER NOT NULL,
                title TEXT,
                content TEXT,
                confidential_level TEXT
            )
        ''')

        self.conn.commit()

    def seed_data(self):
        cursor = self.conn.cursor()

        # Sample users
        users = [
            (1, "john_doe", "Password1"),
            (2, "jane_smith", "SecurePass2"),
            (3, "alice_jones", "AlicePass3"),
            (4, "bob_brown", "BobSecure4"),
            (5, "admin", "AdminPass!@#")
        ]
        cursor.executemany("INSERT OR IGNORE INTO Users (userId, username, password) VALUES (?, ?, ?)", users)

        # Sample documents
        documents = [
            (1, 1, "Project Plan", "Confidential project plan content.", "High"),
            (2, 1, "Meeting Notes", "Notes from the last meeting.", "Medium"),
            (3, 2, "Financial Report", "Annual financial report.", "High"),
            (4, 2, "Personal Notes", "Personal notes and reminders.", "Low"),
            (5, 3, "Research Paper", "Draft of the research paper.", "High"),
            (6, 4, "Invoice", "Invoice details for client.", "Medium"),
            (7, 5, "Admin Credentials", "Username and password details.", "Top Secret")
        ]
        cursor.executemany("INSERT OR IGNORE INTO Documents (documentId, userId, title, content, confidential_level) VALUES (?, ?, ?, ?, ?)", documents)

        self.conn.commit()

    def get_user_documents(self, userId):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM Documents WHERE userId = '{str(userId)}'")
        rows = cursor.fetchall()

        # Get column names
        columns = [column[0] for column in cursor.description]

        # Convert rows to dictionaries with column names as keys
        documents = [dict(zip(columns, row)) for row in rows]

        # Convert to JSON format
        return json.dumps(documents, indent=4)

    def get_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT userId, username FROM Users WHERE userId = {str(user_id)}"
        )
        rows = cursor.fetchall()

        # Get column names
        columns = [column[0] for column in cursor.description]

        # Convert rows to dictionaries with column names as keys
        users = [dict(zip(columns, row)) for row in rows]

        # Convert to JSON format
        return json.dumps(users, indent=4)

    def close(self):
        self.conn.close()
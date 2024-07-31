import sqlite3

def create_db():
  conn = sqlite3.connect('mydatabase.db') 
  cursor = conn.cursor()

  # Create a sample table (you can add more tables as needed)
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          email TEXT UNIQUE NOT NULL
      )
  ''')

  conn.commit()
  conn.close()

if __name__ == '__main__':
  create_db()
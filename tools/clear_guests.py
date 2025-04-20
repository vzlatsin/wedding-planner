import sys
import os

# Ensure access to database module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Database

def clear_guests_table():
    db = Database()
    db.execute("DELETE FROM guests")
    print("✅ Guests table cleared.")

if __name__ == '__main__':
    clear_guests_table()


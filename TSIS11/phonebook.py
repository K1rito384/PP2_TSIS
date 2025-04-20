import psycopg2
import csv
import json

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="deti0609",
        options="-c client_encoding=utf8"  
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)

    cur.execute("SELECT COUNT(*) FROM phonebook;")
    count = cur.fetchone()[0]
    if count == 0:
        initial_data = [
            ("Alice", "1234567890"),
            ("Bob", "9876543210"),
            ("Charlie", "5556667777")
        ]
        for name, phone in initial_data:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def query_data():
    filter_value = input("Search by name or phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_records_by_pattern(%s)", (filter_value,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def insert_or_update_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_many_users():
    users_list = [
        {"name": "Alice", "phone": "1234567890"},
        {"name": "Bob", "phone": "9876543210"},
        {"name": "Charlie", "phone": "5556667777"},
        {"name": "David", "phone": "0012345678"}
    ]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL insert_multiple_users(%s)", [json.dumps(users_list)])
    conn.commit()
    cur.close()
    conn.close()

def query_paginated_data():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated_records(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_entry():
    value = input("Enter name or phone to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_user_by_name_or_phone(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()

def main():
    create_table() 
    
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert or Update User")
        print("2. Insert Multiple Users")
        print("3. Query Paginated Data")
        print("4. Delete Entry")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            insert_or_update_user()
        elif choice == "2":
            insert_many_users()
        elif choice == "3":
            query_paginated_data()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

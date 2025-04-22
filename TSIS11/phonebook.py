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
    cur.execute("DROP TABLE IF EXISTS phonebook;")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def query_data():
    filter_value = input("Search by name or phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", 
                (f'%{filter_value}%', f'%{filter_value}%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def insert_or_update_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    if len(phone) != 11 or phone[0] != '8' or not phone.isdigit():
        print("Номер телефона должен быть 11 символов, начинаться с 8 и содержать только цифры.")
        return

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO phonebook (name, phone)
        VALUES (%s, %s)
        ON CONFLICT (name) 
        DO UPDATE SET phone = EXCLUDED.phone
    """, (name, phone))
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

    for user in users_list:
        if len(user["phone"]) != 11 or user["phone"][0] != '8' or not user["phone"].isdigit():
            print(f"Неверный номер телефона для пользователя {user['name']}: {user['phone']}")
            continue
        
        cur.execute("SELECT id FROM phonebook WHERE name = %s", (user["name"],))
        existing_user = cur.fetchone()

        if existing_user:
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE name = %s",
                (user["phone"], user["name"])
            )
        else:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (user["name"], user["phone"])
            )

    conn.commit()
    cur.close()
    conn.close()

def query_paginated_data():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_entry():
    value = input("Enter name or phone to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    cur.close()
    conn.close()

def get_all_records():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
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
        print("5. Show All Records")
        print("6. Exit")
        
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
            get_all_records()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

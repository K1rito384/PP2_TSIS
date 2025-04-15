import psycopg2
import csv

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="deti06091"
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
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def update_data():
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")
    new_phone = input("Enter new phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET name = %s, phone = %s WHERE name = %s", (new_name, new_phone, old_name))
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

def delete_entry():
    value = input("Enter name or phone to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    cur.close()
    conn.close()

def main():
    create_table()
    
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert from CSV")
        print("2. Insert from Console")
        print("3. Update Data")
        print("4. Query Data")
        print("5. Delete Entry")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            filename = input("Enter CSV filename: ")
            insert_from_csv(filename)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

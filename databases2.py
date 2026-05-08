import sqlite3

DB = "school.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade INTEGER,
                city TEXT 
            )
        """)
    print("Database ready!")

def add_student(name, grade, city):
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO students (name, grade, city) VALUES (?, ?, ?)", (name, grade, city))
    print(f"{name} added!")

def get_all_students():
    with sqlite3.connect(DB) as conn:
        return conn.execute("SELECT * FROM students").fetchall()

def update_grade(name, new_grade):
    with sqlite3.connect(DB) as conn:
        conn.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, name))
    print(f"{name}'s grade updated to {new_grade}!")

def delete_student(name):
    with sqlite3.connect(DB) as conn:
        conn.execute("DELETE FROM students WHERE name = ?", (name,))
    print(f"{name} deleted!")

def show_students():
    students = get_all_students()
    print(f"\n{'ID':<5} {'Name':<15} {'Grade':<10} {'City'}")
    print("-" * 40)
    for row in students:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<10} {row[3]}")

# Run it!
init_db()
add_student("Ethan", 95, "Nashville")
add_student("Zuko", 88, "Fire Nation")
add_student("Kya", 92, "Water Tribe")
add_student("Mako", 78, "Republic City")
show_students()
update_grade("Mako", 85)
show_students()
delete_student("Zuko")
show_students()
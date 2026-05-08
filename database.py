import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade INTEGER,
        city TEXT
    )
 """)

conn.commit()
print("database created!")
conn.close()

conn = sqlite3.connect("students.db")
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("INSERT INTO students (name, grade, city) VALUES (?, ?, ?)", ("Ethan", 95, "Nashville"))
    cursor.execute("INSERT INTO students (name, grade, city) VALUES (?, ?, ?)", ("Zuko", 88, "Fire Nation"))
    cursor.execute("INSERT INTO students (name, grade, city) VALUES (?, ?, ?)", ("Kya", 92, "Water Tribe"))
    cursor.execute("INSERT INTO students (name, grade, city) VALUES (?, ?, ?)", ("Mako", 78, "Republic City"))
    conn.commit()
    print("Students added!")
else:
    print("Students already exist!")

conn.close()

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

print("")
print(f"{'ID':<5} {'Name':<15} {'Grade':<10} {'City'}")
print("-" * 40)
for row in students:
    print(f"{row[0]:<5} {row[1]:<15} {row[2]:<10} {row[3]}")
conn.close()

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Get only students with grade above 85
cursor.execute("SELECT * FROM students WHERE grade > 85")
high_achievers = cursor.fetchall()
print("\nHigh achievers (grade > 85):")
for row in high_achievers:
    print(f"  {row[1]} - {row[2]}")

# Get students ordered by grade
cursor.execute("SELECT * FROM students ORDER BY grade DESC")
ranked = cursor.fetchall()
print("\nRanked by grade:")
for i, row in enumerate(ranked):
    print(f"  {i+1}. {row[1]} - {row[2]}")

# Get average grade
cursor.execute("SELECT AVG(grade) FROM students")
avg = cursor.fetchone()[0]
print(f"\nClass average: {avg:.1f}")

conn.close()

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Update a student's grade
cursor.execute("UPDATE students SET grade = 95 WHERE name = 'Mako'")
conn.commit()
print("\nMako's grade updated!")

# Delete a student
cursor.execute("DELETE FROM students WHERE name = 'Mako'")
conn.commit()
print("Mako Deleted!")

# Show final table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\nFinal table:")
for row in rows:
    print(f"  {row[1]} - {row[2]} - {row[3]}")
conn.close()
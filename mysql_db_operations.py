import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='YourActualPassword'  # replace with your password
)

cursor = conn.cursor()

# 1. Create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
print("Database 'testdb' created or already exists.")

# 2. Connect to the new database
conn.database = 'testdb'

# 3. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
""")
print("Table 'students' created or already exists.")

# 4. Insert data into table
cursor.execute("INSERT INTO students (name, age) VALUES ('John Doe', 22)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Jane Smith', 21)")
conn.commit()
print("Data inserted into 'students' table.")

# 5. Read data from table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudents Table:")
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()

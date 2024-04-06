import psycopg2
import sys

# Connect to the A3 database
def connect():
    con = psycopg2.connect(
        dbname="test 7",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    ) 
    return (con, con.cursor())

# Global connection and cursor objects
(connection, cursor) = connect()

connection.autocommit = True

#returns True if successful, False otherwise
def createNewMember(name, password, age, weight, height, phone, address, email):
    try:
        cursor.execute(f"INSERT INTO member (name, password, age, weight, height, phone, address, email) \
                       VALUES('{name}', '{password}', {age}, {weight}, {height}, '{phone}', '{address}', '{email}');")
        return True
    except Exception as e:
        print(str(e))
        return False

#returns member id if successful, None otherwise
def login(email, password):
    cursor.execute(f"SELECT member.id FROM member WHERE email = '{email}' AND password = '{password}';")
    res = cursor.fetchall()
    if (res):
        return res[0][0]
    else:
        return None

print(login("isaac@gmail.com", "12345678"))
createNewMember("d", "12345678", 1, 1, 1, '1', '1', 'daniel@gmail.com')
print(login("daniel@gmail.com", "12345678"))









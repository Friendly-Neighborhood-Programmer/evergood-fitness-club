import psycopg2
import sys
#TODO: import Member file

# Connect to the A3 database
def connect():
    con = psycopg2.connect(
        dbname="Fitness",
        user="postgres",
        password="comp3005",
        host="localhost",
        port="5432"
    ) 
    return (con, con.cursor())

# Global connection and cursor objects
(connection, cursor) = connect()

#returns trainer id if successful and none otherwise
def loginTrainer(name, password):
    cursor.execute(f"SELECT id FROM trainer WHERE name = '{name}' and password = '{password}';")
    res = cursor.fetchall()
    if(res):
        trainer_id = res[0][0]
        return trainer_id
    else:
        return None

def trainerMenu():
    print("(1) Schedule Management\n(2) View Member Profile\n(q) Log out")

def checkClassesOverlap(s, e, d, id, type):
    cursor.execute(f"SELECT * FROM class WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND {type}_id = {id};")
    res = cursor.fetchall()
    if(res):
        return True
    else:
        return False
    
def checkSessionsOverlap(s, e, d, id, type):
    cursor.execute(f"SELECT * FROM personal_session WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND {type}_id = {id};")
    res = cursor.fetchall()
    if(res):
        return True
    else:
        return False

def checkOverlap(s, e, d, id, type):
    return checkClassesOverlap(s, e, d, id, type) or checkSessionsOverlap(s, e, d, id, type)

def addSession(name, s, e, d, tid, rid):
    if (not (checkOverlap(s, e, d, tid, 'trainer') or checkOverlap(s, e, d, rid, 'room'))):
        cursor.execute(f"INSERT INTO personal_session(name, trainer_id, room_id, member_id, day, start_time, end_time) VALUES\
                       ('{name}', {tid}, {rid}, 1, '{d}', '{s}', '{e}');")
        connection.commit()
        return True
    return False

def printAvailableRooms(s, e, d):
    cursor.execute(f"SELECT * FROM room WHERE NOT EXISTS( \
                   SELECT * FROM class WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND room_id = room.id)\
                   AND NOT EXISTS( \
                   SELECT * FROM personal_session WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND room_id = room.id);")
    res = cursor.fetchall()
    printRooms(res)
    
def findMember(name):
    cursor.execute(f"SELECT id FROM member WHERE name = '{name}';")
    res = cursor.fetchall()
    if(res):
        member_id = res[0][0]
        return member_id
    else:
        return None

def printRooms(res):
    print(f"Rooms\n{'id': ^5}|{'name': ^20}")
    for i in range(25):
        print("-", end="")
    print()
    for row in res:
        print(f"{row[0]: ^5}|{row[1] : <20}")
    
print(loginTrainer('lance lift', 'bigmuscles'))
print(loginTrainer('max muscle', 'gains4days'))
print(checkSessionsOverlap('10:00:00', '11:00:00', 'TUE', 1, 'trainer'))
print(checkSessionsOverlap('09:00:00', '11:00:00', 'MON', 1, 'trainer'))

printAvailableRooms('10:00:00', '11:00:00', 'TUE')
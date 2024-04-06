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

def getAllClasses():
    cursor.execute(f"SELECT class.name, class.day, class.start_time, class.end_time, trainer.name, class.id \
                   FROM class \
                   INNER JOIN trainer ON trainer.id = class.trainer_id \
                   INNER JOIN room ON room.id = class.room_id \
                   ORDER BY class.day, class.start_time;")
    print(f"Classes this week\n{'Class name': ^30}|{'Date': <5}|{'Start': <10}|{'End': <10}|{'Trainer': <20}|Registered")
    res = cursor.fetchall()
    for row in res:
        print(f"{row[0]: <30}|{row[1]: <5}| {row[2]} | {row[3]} |{row[4]: <20}|", end="")
        cursor.execute(f"SELECT member.name FROM member INNER JOIN member_takes_class ON member.id = member_takes_class.member_id WHERE member_takes_class.class_id = {row[5]};")
        for innerRow in cursor.fetchall():
            print(f"{innerRow[0]}, ", end="")
        print()

def getAllSessions():
    cursor.execute(f"SELECT personal_session.name, personal_session.day, personal_session.start_time, personal_session.end_time, trainer.name, member.name \
                   FROM personal_session \
                   INNER JOIN trainer ON trainer.id = personal_session.trainer_id \
                   INNER JOIN member ON member.id = personal_session.member_id \
                   INNER JOIN room ON room.id = personal_session.room_id \
                   ORDER BY personal_session.day, personal_session.start_time;")
    print(f"Personal Sessions this week\n{'Sesson name': ^20}|{'Date': <5}|{'Start': <10}|{'End': <10}|{'Trainer': <20}|{'Member': <15}")
    for row in cursor.fetchall():
        print(f"{row[0]: ^20}|{row[1]: <5}| {row[2]} | {row[3]} |{row[4]: <20}|{row[5]: <15}")

def checkOverlapTable(s, e, d, id, type, table):
    cursor.execute(f"SELECT * FROM {table} WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND {type}_id = {id};")
    if(cursor.fetchall()):
        return True
    else:
        return False

def checkOverlapType(s, e, d, id, type):
    return checkOverlapTable(s, e, d, id, type, "class") or checkOverlapTable(s, e, d, id, type, "personal_session")

def addSession(name, s, e, d, tid, rid):
    if (not (checkOverlapType(s, e, d, tid, 'trainer') or checkOverlapType(s, e, d, rid, 'room'))):
        cursor.execute(f"INSERT INTO personal_session(name, trainer_id, room_id, member_id, day, start_time, end_time) VALUES\
                       ('{name}', {tid}, {rid}, 1, '{d}', '{s}', '{e}');")
        connection.commit()
        return True
    return False

def getAvailable(s, e, d, table):
    cursor.execute(f"SELECT * FROM {table} WHERE NOT EXISTS( \
                   SELECT * FROM class WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND {table}_id = {table}.id)\
                   AND NOT EXISTS( \
                   SELECT * FROM personal_session WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND {table}_id = {table}.id);")
    res = cursor.fetchall()
    print(f"Available {table}s on {d} from {s} to {e}\n{'id': ^5}|{'name': <30}")
    for i in range(25):
        print("-", end="")
    print()
    for row in res:
        print(f"{row[0]: ^5}|{row[1] : <20}")
    
def findMember(name):
    cursor.execute(f"SELECT id FROM member WHERE name = '{name}';")
    res = cursor.fetchall()
    if(res):
        member_id = res[0][0]
        return member_id
    else:
        return None

    
    
print(loginTrainer('lance lift', 'bigmuscles'))
print(loginTrainer('max muscle', 'gains4days'))
print(checkOverlapType('10:00:00', '11:00:00', 'TUE', 1, 'trainer'))
print(checkOverlapType('09:00:00', '11:00:00', 'MON', 1, 'trainer'))

getAvailable('10:00:00', '11:00:00', 'TUE', 'room')
getAvailable('10:00:00', '11:00:00', 'TUE', 'trainer')
getAllSessions()
getAllClasses()
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

def checkClassesOverlapTrainer(s, e, d, tid):
    cursor.execute(f"SELECT * FROM class WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND trainer_id = {tid};")
    res = cursor.fetchall()
    if(res):
        return True
    else:
        return False
    
def checkSessionsOverlapTrainer(s, e, d, tid):
    cursor.execute(f"SELECT * FROM personal_session WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND trainer_id = {tid};")
    res = cursor.fetchall()
    if(res):
        return True
    else:
        return False

def checkOverlapTrainer(s, e, d, tid):
    return    checkClassesOverlapTrainer(s, e, d, tid) or  checkSessionsOverlapTrainer(s, e, d, tid)

def addSession(s, e, d, tid, rid):
    return
    
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
print(checkSessionsOverlapTrainer('10:00:00', '11:00:00', 'TUE', 1))
print(checkSessionsOverlapTrainer('09:00:00', '11:00:00', 'MON', 1))
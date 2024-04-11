import psycopg2
import sys
#TODO: import Member file

#returns trainer id if successful and none otherwise
def login_trainer(cursor, name, password):
    cursor.execute(f"SELECT id FROM trainer WHERE name = '{name}' and password = '{password}';")
    res = cursor.fetchall()
    if(res):
        trainer_id = res[0][0]
        return trainer_id
    else:
        return None

#menus
def trainer_menu():
    print("(1) Schedule Management\n(2) View Member Profile\n(q) Log out")

def schedule_menu():
    print("(1) View Classes\n(2) View Personal Sessions\n(3) Add Personal Session\n(4)Delete Personal Session\n(q) Back")

def get_all_classes(cursor):
    cursor.execute(f"SELECT class.id, class.name, room.name, class.day, class.start_time, class.end_time, trainer.name \
                   FROM class \
                   INNER JOIN trainer ON trainer.id = class.trainer_id \
                   INNER JOIN room ON room.id = class.room_id \
                   ORDER BY class.day, class.start_time;")
    print(f"Classes this week\n{'id': ^4}|{'class name': ^30}|{'room': <15}|{'date': <5}|{'start': <10}|{'end': <10}|{'trainer': <20}|registered")
    res = cursor.fetchall()
    for row in res:
        print(f"{row[0]: <4}|{row[1]: <30}|{row[2]: <15}|{row[3]: <5}| {row[4]} | {row[5]} |{row[6]: <20}|", end="")
        cursor.execute(f"SELECT member.name FROM member INNER JOIN member_takes_class ON member.id = member_takes_class.member_id WHERE member_takes_class.class_id = {row[0]};")
        for innerRow in cursor.fetchall():
            print(f"{innerRow[0]}, ", end="")
        print()

#get classes by type (use for trainer or room)
def get_classes_by_type(cursor, id, type):
    other = 'trainer'
    if(type=='room'):
        other = 'trainer'
    cursor.execute(f"SELECT class.id, class.name, {other}.name, class.day, class.start_time, class.end_time \
                   FROM class \
                   INNER JOIN trainer ON trainer.id = class.trainer_id \
                   INNER JOIN room ON room.id = class.room_id \
                   WHERE class.{type}_id = {id}\
                   ORDER BY class.day, class.start_time;")
    print(f"Classes this week\n{'id': ^4}|{'class name': ^30}|{other: <20}|{'date': <5}|{'start': <10}|{'end': <10}|registered")
    res = cursor.fetchall()
    for row in res:
        print(f"{row[0]: <4}|{row[1]: <30}|{row[2]: <20}|{row[3]: <5}| {row[4]} | {row[5]}|", end="")
        cursor.execute(f"SELECT member.name FROM member INNER JOIN member_takes_class ON member.id = member_takes_class.member_id WHERE member_takes_class.class_id = {row[0]};")
        for innerRow in cursor.fetchall():
            print(f"{innerRow[0]}, ", end="")
        print()

def get_classes_by_member(cursor, id):
    cursor.execute(f"SELECT c.id, c.name, r.name, c.day, c.start_time, c.end_time, t.name \
                   FROM class c \
                   INNER JOIN trainer t ON t.id = c.trainer_id \
                   INNER JOIN room r ON r.id = c.room_id \
                   WHERE EXISTS(\
                   SELECT * \
                   FROM member_takes_class t \
                   WHERE c.id = t.class_id and t.member_id = {id})
                   ORDER BY c.day, c.start_time;")
    print(f"Classes this week\n{'id': ^4}|{'class name': ^30}|{'room': <15}|{'date': <5}|{'start': <10}|{'end': <10}|{'trainer': <20}|registered")
    res = cursor.fetchall()
    for row in res:
        print(f"{row[0]: <4}|{row[1]: <30}|{row[2]: <15}|{row[3]: <5}| {row[4]} | {row[5]} |{row[6]: <20}|", end="")
        cursor.execute(f"SELECT member.name FROM member INNER JOIN member_takes_class ON member.id = member_takes_class.member_id WHERE member_takes_class.class_id = {row[0]};")
        for innerRow in cursor.fetchall():
            print(f"{innerRow[0]}, ", end="")
        print()

def get_all_sessions(cursor):
    cursor.execute(f"SELECT personal_sesson.id, personal_session.name, room.name, personal_session.day, personal_session.start_time, personal_session.end_time, trainer.name, member.name \
                   FROM personal_session \
                   INNER JOIN trainer ON trainer.id = personal_session.trainer_id \
                   INNER JOIN member ON member.id = personal_session.member_id \
                   INNER JOIN room ON room.id = personal_session.room_id \
                   ORDER BY personal_session.day, personal_session.start_time;")
    print(f"Personal Sessions this week\n{'id': ^4}|{'sesson name': ^20}|{'room': <15}|{'date': <5}|{'start': <10}|{'end': <10}|{'trainer': <20}|{'member': <15}")
    for row in cursor.fetchall():
        print(f"{row[0]: <4}|{row[1]: <20}|{row[2]: <15}|{row[3]: <5}|{row[4]: <5}| {row[5]} | {row[6]} |{row[7]: <20}|{row[8]: <15}")


#get sessions by type (use for trainer or room)
def get_sessions_by_type(cursor, id, type):
    other = 'trainer'
    if(type=='room'):
        other = 'trainer'
    cursor.execute(f"SELECT personal_sesson.id, personal_session.name, {other}.name, personal_session.day, personal_session.start_time, personal_session.end_time, member.name \
                   FROM personal_session \
                   INNER JOIN trainer ON trainer.id = personal_session.trainer_id \
                   INNER JOIN member ON member.id = personal_session.member_id \
                   INNER JOIN room ON room.id = personal_session.room_id \
                   WHERE personal_session.{type}_id = {id}\
                   ORDER BY personal_session.day, personal_session.start_time;")
    print(f"Personal Sessions this week\n{'id': ^4}|{'sesson name': ^20}|{other: <20}|{'date': <5}|{'start': <10}|{'end': <10}|{'member': <15}")
    for row in cursor.fetchall():
        print(f"{row[0]: <4}|{row[1]: <20}|{row[2]: <15}|{row[3]: <5}|{row[4]: <5}| {row[5]} | {row[6]}|{row[7]: <15}")

def get_sessions_by_member(cursor, id):
    cursor.execute(f"SELECT personal_sesson.id, personal_session.name, room.name, personal_session.day, personal_session.start_time, personal_session.end_time, trainer.name \
                   FROM personal_session \
                   INNER JOIN trainer ON trainer.id = personal_session.trainer_id \
                   INNER JOIN member ON member.id = personal_session.member_id \
                   INNER JOIN room ON room.id = personal_session.room_id \
                   WHERE personal_session.member_id = {id} \
                   ORDER BY personal_session.day, personal_session.start_time;")
    print(f"Personal Sessions this week\n{'id': ^4}|{'sesson name': ^20}|{'room': <15}|{'date': <5}|{'start': <10}|{'end': <10}|{'trainer': <20}")
    for row in cursor.fetchall():
        print(f"{row[0]: <4}|{row[1]: <20}|{row[2]: <15}|{row[3]: <5}|{row[4]: <5}| {row[5]} | {row[6]} |{row[7]: <20}")

def check_time_overlap(cursor, s, e, d, id, type, table):
    cursor.execute(f"SELECT * FROM {table} WHERE day = '{d}' AND \
                   (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND \
                   end_time >= '{e}' OR start_time > '{s}' AND end_time <= '{e}') AND {type}_id = {id};")
    if(cursor.fetchall()):
        return True
    else:
        return False

def check_overlap_type(cursor, s, e, d, id, type):
    return check_time_overlap(cursor, s, e, d, id, type, "class") or check_time_overlap(cursor, s, e, d, id, type, "personal_session")

#add session, return True if success and False otherwise
def add_session(cursor, name, s, e, d, tid, rid):
    if (not (check_overlap_type(cursor, s, e, d, tid, 'trainer') or check_overlap_type(cursor, s, e, d, rid, 'room'))):
        try:
            cursor.execute(f"INSERT INTO personal_session(name, trainer_id, room_id, member_id, day, start_time, end_time) VALUES\
                       ('{name}', {tid}, {rid}, 1, '{d}', '{s}', '{e}');")
            return True
        except Exception as e:
            print(str(e))
            return False
    return False

#delete session from the database with matching id
def delete_session(cursor, id):
    try:
        cursor.execute(f"DELETE FROM session WHERE id = {id} AND member_id = 1;")
        return True
    except Exception as e:
        print(str(e))
        return False

#prints out the id and name of available entities (used for trainer and room)
def get_available(cursor, s, e, d, table):
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
        print(f"{row[0]: ^5}|{row[1] : <30}")
    
def find_member_by_name(cursor, name):
    cursor.execute(f"SELECT id FROM member WHERE name = '{name}';")
    res = cursor.fetchall()
    if(res):
        member_id = res[0][0]
        return member_id
    else:
        return None
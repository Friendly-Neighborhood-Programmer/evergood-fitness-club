from trainer import *

#add session, return True if success and False otherwise
def add_class(cursor, name, s, e, d, tid, rid):
    if (not (check_overlap_type(cursor, s, e, d, tid, 'trainer') or check_overlap_type(cursor, s, e, d, rid, 'room'))):
        cursor.execute(f"INSERT INTO class(name, trainer_id, room_id, day, start_time, end_time) VALUES\
                       ('{name}', {tid}, {rid}, '{d}', '{s}', '{e}');")
        return True
    return False

#delete class from the database with matching id
def delete_class(cursor, id):
    cursor.execute(f"DELETE FROM member_takes_class WHERE member_takes_class.class_id = {id};")
    cursor.execute(f"DELETE FROM class WHERE class.id = {id};")

#Prints out all equipment and relevant information
def get_all_equipment(cursor):
    cursor.execute(f"SELECT e.id, e.name, r.name, r.id, a.name, e.condition \
                   FROM equipment e \
                   INNER JOIN room r ON r.id = e.room_id \
                   INNER JOIN admin a ON a.id = e.admin_id \
                   ORDER BY r.id;")
    print(f"All equipment\n{'id': ^4}|{'name': ^15}|{'room': ^20}|{'admin': ^20}|{'condition': 8}")
    for row in cursor.fetchall():
        condition = 'check in'
        if(row[5]):
            condition = 'good'
        print(f"{row[0]: <4}|{row[1]: <15}|{row[2] + ' ' +row[3]: <20}|{row[4]: <20}|{condition}")

#Prints out equipment for a specific admin and relevant information
def get_equipment_by_admin(cursor, id):
    cursor.execute(f"SELECT e.id, e.name, r.name, r.id, e.condition \
                   FROM equipment e \
                   INNER JOIN room r ON r.id = e.room_id \
                   INNER JOIN admin a ON a.id = e.admin_id \
                   WHERE a.id = {id} \
                   ORDER BY r.id;")
    print(f"Equipment\n{'id': ^4}|{'name': ^15}|{'room': ^20}|{'condition': 8}")
    for row in cursor.fetchall():
        condition = 'check in'
        if(row[4]):
            condition = 'good'
        print(f"{row[0]: <4}|{row[1]: <15}|{row[2] + ' ' +row[3]: <20}|{condition}")

def update_equipment_condition(cursor, id, condition):
    cursor.execute(f"UPDATE equipment\
                   SET condition = {condition} \
                    WHERE id = {id};")
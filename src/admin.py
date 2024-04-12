from trainer import *
import trainer

# returns member id if successful, None otherwise
def login(cursor, name, password):
    cursor.execute(f"SELECT admin.id FROM admin WHERE name = '{name}' AND password = '{password}';")
    res = cursor.fetchall()
    
    if (res):
        return res[0][0]
    else:
        return None
    
#add session, return True if success and False otherwise
def add_class(connection, cursor, name, s, e, d, tid, rid):
    if (not (check_overlap_type(cursor, s, e, d, tid, 'trainer') or check_overlap_type(cursor, s, e, d, rid, 'room'))):
        try:
            cursor.execute(f"INSERT INTO class(name, trainer_id, room_id, day, start_time, end_time) VALUES\
                       ('{name}', {tid}, {rid}, '{d}', '{s}', '{e}');")
            connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
    return False

#delete class from the database with matching id
def delete_class(connection, cursor, id):
    try:
        cursor.execute(f"DELETE FROM member_takes_class WHERE member_takes_class.class_id = {id};")
        cursor.execute(f"DELETE FROM class WHERE class.id = {id};")
        connection.commit()
    except Exception as e:
        print(str(e))

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

def update_equipment_condition(connection, cursor, id, condition):
    try:
        cursor.execute(f"UPDATE equipment\
                    SET condition = {condition} \
                        WHERE id = {id};")
        connection.commit()
        return True
    except Exception as e:
        print(str(e))
        return False   

def member_pay_bill(connection, cursor, member_id):
    try:
        cursor.execute(f"UPDATE member\
                        SET paid = true \
                        WHERE id = {member_id};")
        connection.commit()
        return True
    except Exception as e:
        print(str(e))
        return False 
    
def get_all_classes(cursor):
    trainer.get_all_classes(cursor)

def get_available_rooms_for_class(cursor, class_id):
    cursor.execute(f"SELECT * FROM class WHERE id = {class_id}")
    res = cursor.fetchall()

    class_info = res[0]

    if (class_info):
        return trainer.get_available(cursor, class_info[3], class_info[4], class_info[2], 'room')
    else:
        print("No available rooms for that time")
        return []

def change_class_room(connection, cursor, class_id, room_id, available_rooms):
    if room_id in available_rooms:
        try:
            cursor.execute(f"UPDATE class SET room_id = {room_id} WHERE id = {class_id};")

            connection.commit()
            return True
        except Exception as e:
            print(str(e))

    return False


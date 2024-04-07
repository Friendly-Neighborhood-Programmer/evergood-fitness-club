import psycopg2
from trainer import *
def add_class(cursor, name, s, e, d, tid, rid):
    if (not (check_overlap_type(cursor, s, e, d, tid, 'trainer') or check_overlap_type(cursor, s, e, d, rid, 'room'))):
        cursor.execute(f"INSERT INTO personal_session(name, trainer_id, room_id, day, start_time, end_time) VALUES\
                       ('{name}', {tid}, {rid}, '{d}', '{s}', '{e}');")
        return True
    return False
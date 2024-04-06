#check for overlaps in the table with 
# def checkTimeOverlap(cursor, table, start, end, day, id, data):
#     cursor.execute(f"SELECT * FROM {table} WHERE day = '{day}' AND \
#                     (start_time <= '{start}' AND end_time > '{start}' OR \
#                     start_time < '{end}' AND end_time >= '{end}' OR \
#                     start_time > '{start}' AND end_time <= '{end}') AND {data}_id = {id};")
    
#     if(cursor.fetchall()):
#         return True
#     else:
#         return False
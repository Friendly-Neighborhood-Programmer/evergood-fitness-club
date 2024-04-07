import psycopg2
import sys

# Connect to the A3 database
def connect():
    con = psycopg2.connect(
        dbname="test 8",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    ) 
    return (con, con.cursor())

# Global connection and cursor objects
(connection, cursor) = connect()

#connection.autocommit = True

#returns True if successful, False otherwise
def createNewMember(cursor, name, password, age, weight, height, phone, address, email):
    try:
        cursor.execute(f"INSERT INTO member (name, password, age, weight, height, phone, address, email) \
                       VALUES('{name}', '{password}', {age}, {weight}, {height}, '{phone}', '{address}', '{email}');")
        return True
    
    except Exception as e:
        print(str(e))
        return False

# return True if there is a member with the given email, False otherwise
def check_email(cursor, email):
    cursor.execute(f"SELECT * FROM member WHERE email = '{email}';")
    return len(cursor.fetchall())

def check_phone(cursor, email):
    cursor.execute(f"SELECT * FROM member WHERE email = '{email}';")
    return len(cursor.fetchall())

# returns member id if successful, None otherwise
def login(cursor, email, password):
    cursor.execute(f"SELECT member.id FROM member WHERE email = '{email}' AND password = '{password}';")
    res = cursor.fetchall()
    
    if (res):
        return res[0][0]
    else:
        return None

#prints current member information
def viewPersonalInformation(cursor, id):
    cursor.execute(f"SELECT * FROM member WHERE member.id = {id}")
    res = cursor.fetchall()

    if (res):
        print(res)
    else:
        print("Could not find personal information.")

#updates member name, age, address, phone, email, password
def updatePersonalInformation(cursor, id, updateMap):
    try:
        for (key, value) in updateMap.items():
            if key == 'age':
                cursor.execute(f"UPDATE member\
	                        SET {key} = {value}\
	                        WHERE id = {id}")
            else:
                cursor.execute(f"UPDATE member\
	                        SET {key} = '{value}'\
	                        WHERE id = {id}")
        return True
                
    except Exception as e:
        print(str(e))
        return False

#prints current member goals
def viewGoals(cursor, id):
    cursor.execute(f"SELECT * FROM goal WHERE goal.member_id = {id}")
    res = cursor.fetchall()

    if (res):
        print(res)
    else:
        print("Could not find goals information.")

#add a goal for a user, return True if successful, False otherwise
def createGoal(cursor, id, description):
    try:
        cursor.execute(f"INSERT INTO goal (description, member_id)\
                       VALUES ('{description}', {id})")
        print("Successfully added goal.")
        return True
    
    except Exception as e:
        print(str(e))
        return False
    
#prints all metrics entered
def viewMetrics(cursor, id):
    cursor.execute(f"SELECT kg FROM weight WHERE weight.member_id = {id};")
    weights = cursor.fetchall()
    cursor.execute(f"SELECT count FROM step WHERE step.member_id = {id}")
    steps = cursor.fetchall()
    cursor.execute(f"SELECT bpm FROM heartrate WHERE heartrate.member_id = {id}")
    bpms = cursor.fetchall()

    if (weights or steps or bpms):
        print(weights) if weights else None
        print(steps) if steps else None
        print(bpms) if bpms else None
    else:
        print("Could not find metrics information.")

#add achievement
def addAchievement(cursor, id, name):
    try:
        cursor.execute(f"INSERT INTO achievement (name, member_id) \
                        SELECT '{name}', {id}\
                        WHERE NOT EXISTS (\
                            SELECT *\
                            FROM achievement\
                            WHERE name = '{name}' AND member_id = {id}\
                        );")
        connection.commit()
        return True
    
    except Exception as e:
        print(str(e))
        return False
    
def generateAchievement(id, name, val, min, step):
    if val >= min + 2*step:
        addAchievement(id, name + '++')
    if val >= min + step:
        addAchievement(id, name + '+')
    if val >= min:
        addAchievement(id, name)
    
#add weight entry, return True if successful, False otherwise
def addWeight(cursor, id, kg):
    try:
        cursor.execute(f"INSERT INTO weight (kg, member_id) \
                       VALUES({kg}, {id});")
        connection.commit()
        generateAchievement(id, 'Heavyweight', kg, 100, 50)
        return True
    
    except Exception as e:
        print(str(e))
        return False

#add steps entry, return True if successful, False otherwise
def addSteps(cursor, id, count):
    try:
        cursor.execute(f"INSERT INTO step (count, member_id) \
                       VALUES({count}, {id});")
        connection.commit()
        generateAchievement(id, 'Trekker', count, 20000, 5000)
        return True
    
    except Exception as e:
        print(str(e))
        return False

#add heartrate entry, return True if successful, False otherwise
def addHeartrate(cursor, id, bpm):
    try:
        cursor.execute(f"INSERT INTO heartrate (bpm, member_id) \
                       VALUES({bpm}, {id});")
        connection.commit()
        generateAchievement(id, "Pump", bpm, 100, 25)
        return True
    
    except Exception as e:
        print(str(e))
        return False

def viewSelectedRoutine(cursor, id):
    cursor.execute(f"SELECT routine.name, description\
                    FROM member JOIN routine ON member.routine_id = routine.id\
                    WHERE member.id = {id}")
    res = cursor.fetchall()

    if (res):
        print(res)
    else:
        print("Could not find routine information.")

def changeSelectedRoutine(cursor, id, routine_id):
    try:
        cursor.execute(f"UPDATE member\
                        SET routine_id = {routine_id}\
                        WHERE id = {id};")
        connection.commit()
        return True
    
    except Exception as e:
        print(str(e))
        return False

def viewAchievements(cursor, id):
    cursor.execute(f"SELECT name\
                    FROM achievement\
                    WHERE member_id = {id}\
                    ORDER BY name ASC;")
    res = cursor.fetchall()

    if (res):
        print(res)
    else:
        print("Could not find achievement information.")

def viewWeightStatistics(cursor, id):
    cursor.execute(f"SELECT MAX(kg) FROM weight GROUP BY member_id HAVING member_id = {id};")
    max = cursor.fetchall()
    cursor.execute(f"SELECT MIN(kg) FROM weight GROUP BY member_id HAVING member_id = {id};")
    min = cursor.fetchall()
    cursor.execute(f"SELECT AVG(kg) FROM weight GROUP BY member_id HAVING member_id = {id};")
    avg = cursor.fetchall()

    if (max or min or avg):
        print(max) if max else None
        print(min) if min else None
        print(avg) if avg else None
    else:
        print("Could not find weight information.")

def viewStepsStatistics(cursor, id):
    cursor.execute(f"SELECT MAX(count) FROM step GROUP BY member_id HAVING member_id = {id};")
    max = cursor.fetchall()
    cursor.execute(f"SELECT MIN(count) FROM step GROUP BY member_id HAVING member_id = {id};")
    min = cursor.fetchall()
    cursor.execute(f"SELECT AVG(count) FROM step GROUP BY member_id HAVING member_id = {id};")
    avg = cursor.fetchall()

    if (max or min or avg):
        print(max) if max else None
        print(min) if min else None
        print(avg) if avg else None
    else:
        print("Could not find steps information.")

def viewHeartrateStatistics(cursor, id):
    cursor.execute(f"SELECT MAX(bpm) FROM heartrate GROUP BY member_id HAVING member_id = {id};")
    max = cursor.fetchall()
    cursor.execute(f"SELECT MIN(bpm) FROM heartrate GROUP BY member_id HAVING member_id = {id};")
    min = cursor.fetchall()
    cursor.execute(f"SELECT AVG(bpm) FROM heartrate GROUP BY member_id HAVING member_id = {id};")
    avg = cursor.fetchall()

    if (max or min or avg):
        print(max) if max else None
        print(min) if min else None
        print(avg) if avg else None
    else:
        print("Could not find heartrate information.")

def viewHealthStatistics(id):
    viewWeightStatistics(id)
    viewStepsStatistics(id)
    viewHeartrateStatistics(id)

# UI menus for member
def trainerMenu():
    print("(1) Profile Management\n(2) Dashboard\n(3) Schedule Management\n(q) Back")

def profileManagementMenu():
    print("(1) Update Personal Information\n(2) Goals\n(3) Health Metrics\n(q) Back")

def personalInfoMenu():
    print("(1) View Information\n(2) Update Information")

def goalsMenu():
    print("(1) View All Goals\n(2) Create Goal\n(3)")

def healthMetricsMenu():
    print("(1) View All Metrics\n(2) Enter weight\n(3) Enter steps\n (4) Enter heartrate")

def dashboardMenu():
    print("(1) Routines\n(2) Achievements\n(3) Health Statistics(q) Back")

def routinesMenu():
    print("(1) Change Routine")
    
if __name__ == "__main__":
    print('test')
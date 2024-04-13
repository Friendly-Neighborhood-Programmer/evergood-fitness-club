import trainer
#returns True if successful, False otherwise
def createNewMember(connection, cursor, name, password, age, phone, address, email, gender):
    try:
        cursor.execute(f"INSERT INTO member (name, password, age, phone, address, email, gender) \
                       VALUES('{name}', '{password}', {age}, '{phone}', '{address}', '{email}', '{gender}');")
        connection.commit()
        return True
    
    except Exception as e:
        print(str(e))
        return False

# return True if there is a member with the given email, False otherwise
def check_email(cursor, email):
    cursor.execute(f"SELECT * FROM member WHERE email = '{email}';")
    return len(cursor.fetchall())

# def check_phone(cursor, email):
#     cursor.execute(f"SELECT * FROM member WHERE email = '{email}';")
#     return len(cursor.fetchall())

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
        print("Your Information:")
        person = res[0]
        print(f"Name:    {person[1]}\n" +
                f"Age:     {person[2]}\n" +
                f"Address: {person[3]}\n" +
                f"Phone:   {person[4]}\n" +
                f"Email:   {person[5]}\n" +
                f"Gender:  {person[6]}\n" +
                f"Paid:    {'Yes' if person[8] else 'No'}\n")
    else:
        print("Could not find personal information.")

#updates member name, age, address, phone, email, password
def updatePersonalInformation(connection, cursor, id, updateMap):
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
            connection.commit()
        return True
                
    except Exception as e:
        print(str(e))
        return False

#prints current member goals
def viewGoals(cursor, id):
    cursor.execute(f"SELECT * FROM goal WHERE goal.member_id = {id}")
    res = cursor.fetchall()

    if (res):
        print("Your Goals:")
        for i, goal in enumerate(res):
            print(f"{i+1}. {goal[1]}")
    else:
        print("Could not find goals information.")

#add a goal for a user, return True if successful, False otherwise
def createGoal(connection, cursor, id, description):
    try:
        cursor.execute(f"INSERT INTO goal (description, member_id)\
                       VALUES ('{description}', {id})")
        print("Successfully added goal.")
        connection.commit()
        return True
    
    except Exception as e:
        print(str(e))
        return False
    
#prints all metrics entered
def viewMetrics(cursor, id):
    cursor.execute(f"SELECT kg FROM weight WHERE weight.member_id = {id} ORDER BY id ASC;")
    weights = cursor.fetchall()
    cursor.execute(f"SELECT count FROM step WHERE step.member_id = {id} ORDER BY id ASC;")
    steps = cursor.fetchall()
    cursor.execute(f"SELECT bpm FROM heartrate WHERE heartrate.member_id = {id} ORDER BY id ASC;")
    heartrates = cursor.fetchall()

    if (weights or steps or heartrates):
        print("Your Metrics:")
        if weights:
            print("Weights")
            for kg in weights:
                print(str(kg[0]) + " kg")

            print()
        
        if steps:
            print("Steps")
            for count in steps:
                print(str(count[0]) + " steps")

            print()

        if heartrates:
            print("Heartrates")
            for bpm in heartrates:
                print(str(bpm[0]) + " bpm")

            print()
    else:
        print("Could not find metrics information.")
        print()

#add achievement
def addAchievement(connection, cursor, id, name):
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
    
def generateAchievement(connection, cursor, id, name, val, min, step):
    if val >= min + 2*step:
        addAchievement(connection, cursor, id, name + '++')
    if val >= min + step:
        addAchievement(connection, cursor, id, name + '+')
    if val >= min:
        addAchievement(connection, cursor, id, name)
    
#add weight entry, return True if successful, False otherwise
def addWeight(connection, cursor, id, kg):
    try:
        cursor.execute(f"INSERT INTO weight (kg, member_id) \
                        VALUES({kg}, {id});")
        connection.commit()
        generateAchievement(connection, cursor, id, 'Heavyweight', kg, 100, 50)
        return True
    
    except Exception as e:
        print(str(e))
        return False

#add steps entry, return True if successful, False otherwise
def addSteps(connection, cursor, id, count):
    try:
        cursor.execute(f"INSERT INTO step (count, member_id) \
                       VALUES({count}, {id});")
        connection.commit()
        generateAchievement(connection, cursor, id, 'Trekker', count, 20000, 5000)
        return True
    
    except Exception as e:
        print(str(e))
        return False

#add heartrate entry, return True if successful, False otherwise
def addHeartrate(connection, cursor, id, bpm):
    try:
        cursor.execute(f"INSERT INTO heartrate (bpm, member_id) \
                       VALUES({bpm}, {id});")
        connection.commit()
        generateAchievement(connection, cursor, id, "Pump", bpm, 100, 25)
        return True
    
    except Exception as e:
        print(str(e))
        return False
    
def viewAllRoutines(cursor):
    cursor.execute(f"SELECT routine.id, routine.name FROM routine")

    print(f"Routines\n{'id': ^4}|{'name': ^30}")
    for row in cursor.fetchall():
        print(f"{row[0]: ^4}|{row[1]: ^30}")

def viewSelectedRoutine(cursor, id):
    cursor.execute(f"SELECT routine.name, description\
                    FROM member JOIN routine ON member.routine_id = routine.id\
                    WHERE member.id = {id}")
    res = cursor.fetchall()

    if (res):
        routine = res[0]
        print(f"Routine name: {routine[0]}\n" +
              f"Description: {routine[1]}\n")
    else:
        print("Could not find routine information.")

def changeSelectedRoutine(connection, cursor, id, routine_id):
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
        for achievement in res:
            print(achievement[0])
        print()
    else:
        print("Could not find achievement information.")

def printStats(max, min, avg, units):
    print(f"Max: {max[0][0]} {units}\n" +
          f"Min: {min[0][0]} {units}\n" +
          f"Avg: " + (f"%.2f {units}\n" % avg[0][0] if units != "steps" else f"{avg[0][0]//1} {units}\n"))

def viewWeightStatistics(cursor, id):
    cursor.execute(f"SELECT MAX(kg) FROM weight GROUP BY member_id HAVING member_id = {id};")
    max = cursor.fetchall()
    cursor.execute(f"SELECT MIN(kg) FROM weight GROUP BY member_id HAVING member_id = {id};")
    min = cursor.fetchall()
    cursor.execute(f"SELECT AVG(kg) FROM weight GROUP BY member_id HAVING member_id = {id};")
    avg = cursor.fetchall()

    if (max or min or avg):
        printStats(max, min, avg, "kg")
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
        printStats(max, min, avg, "steps")
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
        printStats(max, min, avg, "bpm")
    else:
        print("Could not find heartrate information.")

def viewHealthStatistics(cursor, id):
    print("Weight Stats:")
    viewWeightStatistics(cursor, id)
    print("Steps Stats:")
    viewStepsStatistics(cursor, id)
    print("Heartrate Stats:")
    viewHeartrateStatistics(cursor, id)


# UI menus for member
def memberMenu():
    print("(1) Profile Management\n(2) Dashboard\n(3) Schedule Management\n(q) Logout")

def profileManagementMenu():
    print("(1) Manage Personal Information\n(2) Manage Fitness Goals\n(3) Manage Health Metrics\n(q) Back")

def personalInfoMenu():
    print("(1) View Information\n(2) Update Information")

def goalsMenu():
    print("(1) View All Goals\n(2) Create Goal\n(3)")

def healthMetricsMenu():
    print("(1) View All Metrics\n(2) Enter weight\n(3) Enter steps\n (4) Enter heartrate")

def dashboardMenu():
    print("(1) Routines\n(2) Achievements\n(3) Health Statistics\n(q) Back")

def routinesMenu():
    print("(1) View Current Routine\n(2) Change Routine\n(q) Back")

def enroll_in_class(connection, cursor, mid, cid):
    cursor.execute(f"SELECT start_time, end_time, day \
                   FROM class\
                   WHERE id = {cid}")
    res = cursor.fetchall()
    s_time, e_time, day = "", "", ""
    if(res):
        (s_time, e_time, day) = res[0]
    else:
        return False
    if(not check_member_overlap(cursor, mid, s_time, e_time, day)):
        try:
            cursor.execute(f"INSERT INTO member_takes_class(member_id, class_id) VALUES ({mid}, {cid});")
            connection.commit()
            return True
        except Exception as e:
            print(str(e)) 
            return False
    return False

def schedule_session(connection, cursor, mid, sid):
    cursor.execute(f"SELECT start_time, end_time, day \
                   FROM personal_session\
                   WHERE id = {sid} AND member_id = 1")
    res = cursor.fetchall()
    s_time, e_time, day = "", "", ""
    if(res):
        (s_time, e_time, day) = res[0]
    else:
        return False
    if(not check_member_overlap(cursor, mid, s_time, e_time, day)):
        try:
            cursor.execute(f"UPDATE personal_session \
                           SET member_id = {mid} \
                            WHERE id = {sid};")
            connection.commit()
            return True
        except Exception as e:
            print(str(e)) 
            return False
    return False

def unschedule_session(connection, cursor, mid, sid):
    try:
            cursor.execute(f"UPDATE personal_session \
                           SET member_id = 1 \
                            WHERE id = {sid} AND member_id = {mid};")
            connection.commit()
            return True
    except Exception as e:
        print(str(e)) 
        return False       
    
def check_member_overlap(cursor, mid, s, e, d):
    cursor.execute(f"SELECT * \
                   FROM personal_session \
                   WHERE (day = '{d}') AND (start_time <= '{s}' AND end_time > '{s}' OR start_time < '{e}' AND end_time >= '{e}' OR start_time > '{s}' AND end_time < '{e}') AND member_id = {mid};")
    if(cursor.fetchall()):
        return True
    cursor.execute(f"SELECT * \
                   FROM class \
                   WHERE EXISTS (\
                   SELECT *\
                   FROM member_takes_class AS takes\
                   WHERE (takes.class_id = class.id) AND (takes.member_id = {mid}) AND day = '{d}' AND ((start_time <= '{s}' AND end_time > '{s}') OR (start_time < '{e}' AND end_time >= '{e}') OR (start_time > '{s}' AND end_time < '{e}'))\
                   );\
                   ")
    if(cursor.fetchall()):
        return True
    return False

def get_available_sessions(cursor):
    trainer.get_sessions_by_member(cursor, 1)
    
if __name__ == "__main__":
    print('test')
    #addWeight(cursor, 2, 200)
    #viewPersonalInformation(cursor, 2)
    #viewGoals(cursor, 2)
    #viewMetrics(cursor, 2)
    #viewSelectedRoutine(cursor, 2)
    #viewAchievements(cursor, 2)
    #viewWeightStatistics(cursor, 2)
    #viewHealthStatistics(cursor, 2)

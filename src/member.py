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

#add weight entry, return True if successful, False otherwise
def addWeight(cursor, id, kg):
    try:
        cursor.execute(f"INSERT INTO weight (kg, member_id) \
                       VALUES({kg}, {id});")
        return True
    
    except Exception as e:
        print(str(e))
        return False

#add steps entry, return True if successful, False otherwise
def addSteps(cursor, id, count):
    try:
        cursor.execute(f"INSERT INTO step (count, member_id) \
                       VALUES({count}, {id});")
        return True
    
    except Exception as e:
        print(str(e))
        return False

#add heartrate entry, return True if successful, False otherwise
def addHeartrate(cursor, id, bpm):
    try:
        cursor.execute(f"INSERT INTO heartrate (bpm, member_id) \
                       VALUES({bpm}, {id});")
        return True
    
    except Exception as e:
        print(str(e))
        return False

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

if __name__ == "__main__":
    viewPersonalInformation(9)
    update = {'name':'danny', 'age':2}
    updatePersonalInformation(9, update)
    viewPersonalInformation(9)

    viewGoals(9)
    createGoal(9, "weee")
    viewGoals(9)

    viewMetrics(9)
    addWeight(9, 12)
    addSteps(9, 1000)
    addHeartrate(9, 100)
    viewMetrics(9)
    #print(login("isaac@gmail.com", "12345678"))
    #createNewMember("d", "12345678", 1, 1, 1, '1', '1', 'daniel@gmail.com')
    #print(login("daniel@gmail.com", "12345678"))

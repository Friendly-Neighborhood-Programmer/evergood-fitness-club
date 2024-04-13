import database
import member
import trainer
import admin

def main_loop(db):
    while(True):
        # add options to select between member, trainer, and admin
         
        match login_menu():
            case "1":
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                member_id = member.login(db.cursor, email, password)
                if (member_id):
                    print("Login successful. Welcome back!")
                    member_menu(db, member_id)

                else:
                    print("Login failed. Please try again.")     

            case "2":
                data = new_member_prompt(db.con, db.cursor)
                if (member.createNewMember(db.cursor, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])):
                    print("Account created successfully. Welcome to the Evergood Fitness Club!")
                else:
                    print("Account creation failed. Please try again.")
                
            case "3":
                # todo trainer login
                print("Trainer login unimplemented.")
                
            case "4":
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                admin_id = admin.login(db.cursor, name, password)
                if (admin_id):
                    print("Login successful. Welcome back!")
                    admin_menu(db, admin_id) 


            case "5":
                print("Goodbye!")
                break

            case _:
                print("Invalid option. Please try again.")

def login_menu():
    print("\nWelcome to the Evergood Fitness App: ")
    print("(1) Login as existing user")
    print("(2) Sign up as new user")
    print("(3) Login as trainer")
    print("(4) Login as admin")
    print("(5) Exit")
    return input()

def new_member_prompt(connection, cursor):
    email = input("Enter your email: ")
    while(member.check_email(cursor, email)):
        print("Email already exists. Please enter a different email.")
        email = input("Enter your email: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone: ")
    age = input("Enter your age: ")
    height = input("Enter your height: ")
    weight = input("Enter your weight: ")
    return (name, password, age, weight, height, phone, address, email)

def member_menu(db, member_id):
    member.memberMenu()
    member_choice = input()

    while (member_choice != 'q'):
        match member_choice:
            case "1":
                profile_management_menu(db, member_id)
            case "2":
                dashboard_menu
            case "3":
                member._______()
            case "q":
                print("Logging out.")
                break
            case _:
                print("Invalid option. Please try again.")

        member.memberMenu()
        member_choice = input()

def profile_management_menu(db, member_id):
    member.profileManagementMenu()
    profile_choice = input()

    while (profile_choice != 'q'):
        match profile_choice:
            case "1":
                personal_information_menu(db, member_id)
            case "2":
                goal_menu(db, member_id)
            case "3":
                metric_menu(db, member_id)
            case "q":
                print("Returning to member menu.")
                break
            case _:
                print("Invalid option. Please try again.")

        member.profileManagementMenu()
        profile_choice = input()

def dashboard_menu(db, member_id):
    member.dashboardMenu()
    dashboard_choice = input()

    while (dashboard_choice != 'q'):
        match dashboard_choice:
            case "1":
                
            case "2":
                member.viewAchievements(db.cursor, member_id)
            case "3":
                member.viewHealthStatistics(db.cursor, member_id)
            case "q":
                print("Returning to member menu.")
                break
            case _:
                print("Invalid option. Please try again.")

        member.dashboardMenu()
        dashboard_choice = input()

def routine_menu(db, member_id):
    member.routinesMenu()
    routine_choice = input()

    while (routine_choice != 'q'):
        match routine_choice:
            case "1":
                member.viewSelectedRoutine(db.cursor, member_id)
            case "2":
                member.(db.cursor)
                routine_id = input("Enter the ID of the new routine you want to select: ")
                member.changeSelectedRoutine(db.con, db.cursor, member_id, routine_id)
            case "q":
                print("Returning to profile management menu.")
                break

        member.routinesMenu()
        routine_choice = input()

def personal_information_menu(db, member_id):
    print("\n(1) View Personal Information\n(2) Update Personal Information\n(q) Back")
    personal_choice = input()

    while (personal_choice != 'q'):
        match personal_choice:
            case "1":
                member.viewPersonalInformation(db.cursor, member_id)
            case "2":
                details = prompt_for_personal_information(db, member_id)
                member.updatePersonalInformation(db.con, db.cursor, member_id, details)
            case "q":
                print("Returning to profile management menu.")
                break

        print("\n(1) View Personal Information\n(2) Update Personal Information\n(q) Back")
        personal_choice = input()
    
def goal_menu(db, member_id):
    print("\n(1) View All Goals\n(2) Create New Goal\n(q) Back")
    goal_choice = input()

    while (goal_choice != 'q'):
        match goal_choice:
            case "1":
                member.viewGoals(db.cursor, member_id)
            case "2":
                goal = input("Enter the description of your new goal: ")
                member.createGoal(db.con, db.cursor, member_id, goal)
            case "q":
                print("Returning to profile management menu.")
                break
            case _:
                print("Invalid option. Please try again.")

        print("\n(1) View All Goals\n(2) Create New Goal\n(q) Back")
        goal_choice = input()

def metric_menu(db, member_id):
    print("\n(1) View All Metrics\n(2) Enter Weight\n(3) Enter Steps\n(4) Enter Workout Heartrate\n(q) Back")
    metric_choice = input()

    while (metric_choice != 'q'):
        match metric_choice:
            case "1":
                member.viewMetrics(db.cursor, member_id)
            case "2":
                weight = input("Enter your new weight: ")
                member.addWeight(db.con, db.cursor, member_id, float(weight))
            case "3":
                steps = input("Enter your new steps: ")
                member.addSteps(db.con, db.cursor, member_id, int(steps))
            case "4":
                heartrate = input("Enter your new heartrate: ")
                member.addHeartrate(db.con, db.cursor, member_id, float(heartrate))
            case "q":
                print("Returning to profile management menu.")
                break
            case _:
                print("Invalid option. Please try again.")

        print("\n(1) View All Metrics\n(2) Enter Weight\n(3) Enter Steps\n(4) Enter Workout Heartrate\n(q) Back")
        metric_choice = input()

def prompt_for_personal_information(db, member_id):
    details = {}
    details["email"] = input("Enter your email: ")
    while(member.check_email(db.cursor, details["email"])):
        print("Email already exists. Please enter a different email.")
        details["email"] = input("Enter your email: ")
    details["password"] = input("Enter your password: ")
    details["name"] = input("Enter your name: ")
    details["address"] = input("Enter your address: ")
    details["phone"] = input("Enter your phone: ")
    details["age"] = input("Enter your age: ")

    return details

def admin_menu(db, admin_id):
    print("\n(1) Change Fitness-Class Room\n(2) Equipment Maintenance\n(3) Bill Payment\n(4) Fitness-Class Management\n(q) Logout")
    admin_choice = input()

    while (admin_choice != 'q'):
        match admin_choice:
            case "1":
                admin.get_all_classes(db.cursor)
                class_id = input("Enter the ID of the class you want to change: ")
                available_rooms = admin.get_available_rooms_for_class(db.cursor, class_id)
                room_id = input("Enter the ID of the room you want to change to: ")
                admin.change_class_room(db.con, db.cursor, class_id, room_id, available_rooms)
            case "2":
                equipment_maintenance_menu(db, admin_id)
            case "3":
                bill_payment_menu(db, admin_id)
            case "4":
                class_manage_menu(db, admin_id)
            case "q":
                print("Logging out.")
                break
            case _:
                print("Invalid option. Please try again.")

        print("\n(1) Change Fitness-Class Room\n(2) Equipment Maintenance\n(3) Bill Payment\n(4) Fitness-Class Management\n(q) Logout")
        admin_choice = input()

def equipment_maintenance_menu(db, admin_id):
    print("\n(1) View Equipment\n(2) Update Equipment Condition\n(3) Show All Equipment\n(q) Back")
    equipment_choice = input()

    while (equipment_choice != 'q'):
        match equipment_choice:
            case "1":
                admin.get_equipment_by_admin(db.cursor, admin_id)
            case "2":
                equipment_id = input("Enter the ID of the equipment you want to update: ")
                condition = input("Enter the new condition of the equipment (0 for bad, 1 for good): ")
                admin.update_equipment_condition(db.con, db.cursor, equipment_id, condition)
            case "3":
                admin.get_all_equipment(db.cursor)
            case "q":
                print("Returning to admin menu.")
                break
            case _:
                print("Invalid option. Please try again.")
        
        print("\n(1) View Equipment\n(2) Update Equipment Condition\n(3) Show All Equipment\n(q) Back")
        equipment_choice = input()

def bill_payment_menu(db, admin_id):
    print("\n(1) View Paid Bills\n(2) View Unpaid Bill\n(3) Pay Bill\n(q) Back")
    bill_choice = input()

    while (bill_choice != 'q'):
        match bill_choice:
            case "1":
                admin.show_paid_members(db.cursor)
            case "2":
                admin.show_unpaid_members(db.cursor)
            case "3":
                member_id = input("Enter the ID of the member you want to charge: ")
                if (admin.member_pay_bill(db.con, db.cursor, member_id)):
                    print("Payment successful.")
            case "q":
                print("Returning to admin menu.")
                break
            case _:
                print("Invalid option. Please try again.")
        
        print("\n(1) View Paid Bills\n(2) View Unpaid Bill\n(3) Pay Bill\n(q) Back")
        bill_choice = input()

def class_manage_menu(db, admin_id):
    print("\n(1) Create A Class\n(2) Delete A Class\n(q) Back")
    class_manage_choice = input()

    while (class_manage_choice != 'q'):
        match class_manage_choice:
            case "1":
                class_name = input("Enter the name of the class: ")
                day = input("Enter the day of the class: ")
                start_time = input("Enter the start time of the class: ")
                end_time = input("Enter the end time of the class: ")
                trainer.get_available(db.cursor, start_time, end_time, day, 'trainer')
                trainer_id = input("Enter the ID of the trainer for the class: ")
                trainer.get_available(db.cursor, start_time, end_time, day, 'room')
                room_id = input("Enter the ID of the room for the class: ")
                admin.add_class(db.con, db.cursor, class_name, start_time, end_time, day, trainer_id, room_id)
            case "2":
                admin.get_all_classes(db.cursor)
                class_id = input("Enter the ID of the class you want to delete: ")
                admin.delete_class(db.con, db.cursor, class_id)
            case "q":
                print("Returning to admin menu.")
                break
            case _:
                print("Invalid option. Please try again.")
        
        print("\n(1) Create A Class\n(2) Delete A Class\n(q) Back")
        class_manage_choice = input()

def main():
    # get database login information from file 
    dbinfo = database.get_from_file()
    # establish database connection
    db = database.Database(dbinfo)
    # start program CLI
    main_loop(db)
    
main()
#admin.get_all_classes(db.cursor)
#available_room = admin.get_available_rooms_for_class(db.cursor, 1)
#admin.member_pay_bill(db.con, db.cursor, 2)
#member.viewPersonalInformation(db.cursor, 2)
#admin.change_class_room(db.con, db.cursor, 1, 6, available_room)
#admin.change_class_room(db.con, db.cursor, 1, 7, available_room)
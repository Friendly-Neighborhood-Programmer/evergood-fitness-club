import database
import member
import trainer
import admin

def main_loop(db):
    while(True):
        # add options to select between member, trainer, and admin
         
        match login_menu():
            case "1":
                email = input("Enter your email:")
                password = input("Enter your password:")
                member_id = member.login(db.cursor, email, password)
                if (member_id):
                    print("Login successful. Welcome back!")
                    member_menu(member_id)

                else:
                    print("Login failed. Please try again.")     

            case "2":
                data = new_member_prompt(db.cursor)
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
    print("\nWelcome to the Evergood Fitness App:")
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

def member_menu(member_id):
    member.memberMenu()
    member_choice = input()

    while (member_choice != 'q'):
        match member_choice:
            case "1":
                member.profileManagementMenu()
            case "2":
                member.dashboardMenu()
            case "3":
                member.healthMetricsMenu()
            case "q":
                print("Logging out.")
                break
            case _:
                print("Invalid option. Please try again.")

        member.memberMenu()
        member_choice = input()

def admin_menu(db, admin_id):
    print("\n(1) Change Fitness-Class Room\n(2) Equipment Maintenance\n(3) Fitness-Class Management\n(3) Bill Payment\n(q) Logout")
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
                member_id = input("Enter the ID of the member you want to charge: ")
                admin.member_pay_bill(db.con, db.cursor, member_id)
            case "4":
                admin.healthMetricsMenu()
            case "q":
                print("Logging out.")
                break
            case _:
                print("Invalid option. Please try again.")

        print("\n(1) Change Fitness-Class Room\n(2) Equipment Maintenance\n(3) Fitness-Class Management\n(4) Bill Payment\n(q) Logout")
        admin_choice = input()

def equipment_maintenance_menu(db, admin_id):
    print("\n(1) View Equipment\n(2) Update Equipment Condition\n Show All Equipment\n(q) Back")
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
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
                # todo trainer login
                print("Admin login unimplemented.")

            case "5":
                print("Goodbye!")
                break

            case _:
                print("Invalid option. Please try again.")

def login_menu():
    print("Welcome to the Evergood Fitness App:")
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

def member_menu():
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

def main():
    # get database login information from file 
    dbinfo = database.get_from_file("../db.txt")
    # establish database connection
    db = database.Database(dbinfo)
    # start program CLI
    main_loop(db)

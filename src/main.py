import database

def main():
    db = database.Database(database.get_from_file())

if __name__ == "__main__":
    main()


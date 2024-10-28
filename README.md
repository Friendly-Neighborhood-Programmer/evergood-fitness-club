# evergood-fitness-club
A CLI application with full PostgreSQL integration, providing users, trainers, and administrators control over their journey at the Evergood Fitness Club

link to youtube demo video: https://www.youtube.com/watch?v=AO5oeES8XUw

## Steps To Run
Install these dependencies before running:
```
pip install psycopg2
```

Make sure you have pgAdmin4 setup with your database

Create a txt file named 'db.txt' in the root directory containing your PostgreSQL details and credentials
with the format:
```
dbname, user, password, host, port
```

Open and run the DDL.sql and DML.sql using the pgAdmin GUI

In the root directory of the project run 
```
python src/main.py
```

follow the UI prompts on screen to do what you need to

Documentation:
![ER-Diagram](https://github.com/Friendly-Neighborhood-Programmer/evergood-fitness-club/assets/96633176/a18aae28-4bc2-4176-903e-b49b1ed320f9)

![ER-Schema](https://github.com/Friendly-Neighborhood-Programmer/evergood-fitness-club/assets/96633176/c94d2e3b-f3aa-4b1d-a5ba-01b89f17c57b)


Passwords:

## member
Isaac Robert - 12345678

Rachel Stewart - 12345678

## trainer
lance lift - bigmuscles

tina treadmill - I<3running

max muscle - gains4days

holly heartbeat - 95bpmandlovingit

## all admin
12345678


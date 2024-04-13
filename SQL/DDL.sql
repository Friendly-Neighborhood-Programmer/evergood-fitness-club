CREATE TYPE DAY AS ENUM ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT');

CREATE TABLE admin
    (id         SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    password    TEXT NOT NULL,
        CHECK (char_length(password) >= 8 AND char_length(password) <= 32));

CREATE TABLE room
    (id         SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
	admin_id    INT,	
    FOREIGN KEY (admin_id)
        REFERENCES admin(id));

CREATE TABLE equipment
	(id         SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    condition   BOOLEAN DEFAULT TRUE,
	room_id     INT,
	admin_id    INT,
    FOREIGN KEY (room_id)
        REFERENCES room(id),
    FOREIGN KEY (admin_id)
        REFERENCES admin(id));

CREATE TABLE routine
	(id         SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    description TEXT);

CREATE TABLE member
	(id         SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    age         INT  NOT NULL,
    address     TEXT NOT NULL,
    phone       TEXT NOT NULL UNIQUE,
    email       TEXT NOT NULL UNIQUE,
    gender      TEXT,
    bill_amount NUMERIC(5,2) DEFAULT 250,
    paid        BOOLEAN DEFAULT FALSE,
    password    TEXT NOT NULL 
        CHECK (char_length(password) >= 8 AND char_length(password) <= 32),
    routine_id  INT,
    FOREIGN KEY (routine_id)
        REFERENCES routine(id));

CREATE TABLE goal
	(id         SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    member_id   INT,
    FOREIGN KEY (member_id) 
        REFERENCES member(id));

CREATE TABLE weight
	(id SERIAL PRIMARY KEY,
	kg NUMERIC(5, 2) NOT NULL,
	member_id INT,
	FOREIGN KEY (member_id) REFERENCES member(id));

CREATE TABLE step
	(id SERIAL PRIMARY KEY,
	count INT NOT NULL,
	member_id INT,
	FOREIGN KEY (member_id) REFERENCES member(id));

CREATE TABLE heartrate
	(id SERIAL PRIMARY KEY,
	bpm NUMERIC(5, 2) NOT NULL,
	member_id INT,
	FOREIGN KEY (member_id) REFERENCES member(id));

CREATE TABLE achievement
    (id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    member_id INT,
    FOREIGN KEY (member_id) REFERENCES member(id));

CREATE TABLE trainer
    (id         SERIAL PRIMARY KEY,
	name        TEXT NOT NULL,
	specialty   TEXT NOT NULL,
	password    TEXT NOT NULL   
        CHECK (char_length(password) >= 8 AND char_length(password) <= 32));

CREATE TABLE class
    (id         SERIAL PRIMARY KEY,
	name        TEXT NOT NULL,
    day         DAY  NOT NULL,
	start_time  TIME NOT NULL,
	end_time    TIME NOT NULL,
	trainer_id  INT,
	room_id     INT,
	FOREIGN KEY (trainer_id) 
        REFERENCES trainer(id),
	FOREIGN KEY (room_id)
        REFERENCES room(id));

CREATE TABLE personal_session
    (id         SERIAL PRIMARY KEY,
	name        TEXT NOT NULL,
    day         DAY  NOT NULL,
	start_time  TIME NOT NULL,
	end_time    TIME NOT NULL,
	trainer_id  INT,
	room_id     INT,
	member_id   INT,
	FOREIGN KEY (trainer_id)
		REFERENCES trainer(id),
	FOREIGN KEY (room_id)
		REFERENCES room(id),
	FOREIGN KEY (member_id)
		REFERENCES member(id));

CREATE TABLE member_takes_class
    (member_id  INT,
	class_id    INT,
	FOREIGN KEY (member_id)
		REFERENCES member(id),
	FOREIGN KEY (class_id)
		REFERENCES class(id));
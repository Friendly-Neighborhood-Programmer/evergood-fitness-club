CREATE TYPE DAY AS ENUM ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT');

CREATE TABLE admin
    (id         SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    password    TEXT NOT NULL CHECK (char_length(password) >= 8 AND char_length(password) <= 32));

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

CREATE TABLE goal
	(id         SERIAL PRIMARY KEY,
    description TEXT,
    member_id   INT,
    FOREIGN KEY (member_id) 
        REFERENCES member(id));

CREATE TABLE member
	(id         SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    password    TEXT NOT NULL CHECK (char_length(password) >= 8 AND char_length(password) <= 32),
    age         INT NOT NULL,
    weight      NUMERIC(5, 2),
    height      NUMERIC(5, 2),
    phone       VARCHAR(15) UNIQUE,
    address     VARCHAR(255),
    email       VARCHAR(255) UNIQUE,
    bill_amount NUMERIC(5,2),
    paid        BOOLEAN NOT NULL,
    routine_id  INT,
    FOREIGN KEY (routine_id)
        REFERENCES routine(id));

CREATE TABLE trainer
    (id         SERIAL PRIMARY KEY,
	name        TEXT NOT NULL,
	password    TEXT NOT NULL CHECK (char_length(password) >= 8 AND char_length(password) <= 32),
	specialty   TEXT);

CREATE TABLE class
    (id         SERIAL PRIMARY KEY ,
	name        TEXT NOT NULL,
	trainer_id  INT,
	room_id     INT,
	start_time  TIME,
	end_time    TIME,
	FOREIGN KEY (trainer_id) 
        REFERENCES trainer(id),
	FOREIGN KEY (room_id)
        REFERENCES room(id));

CREATE TABLE personal_session(
	id          SERIAL PRIMARY KEY,
	name        TEXT NOT NULL,
	start_time  TIME,
	end_time    TIME,
    day         DAY,
	trainer_id  INT,
	room_id     INT,
	member_id   INT,
	FOREIGN KEY (trainer_id)
		REFERENCES trainer(id),
	FOREIGN KEY (room_id)
		REFERENCES room(id),
	FOREIGN KEY (member_id)
		REFERENCES member(id));

CREATE TABLE member_takes_class(
	member_id   INT,
	class_id    INT,
	FOREIGN KEY (member_id)
		REFERENCES member(id),
	FOREIGN KEY (class_id)
		REFERENCES class(id));
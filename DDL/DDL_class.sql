CREATE TABLE trainer(
	id SERIAL,
	name TEXT NOT NULL,
	password TEXT NOT NULL CHECK (char_length(password) >= 8 AND char_length(password) <= 32),
	specialty TEXT,
	PRIMARY KEY (id)
);

CREATE TABLE class(
	id                SERIAL,
	name              TEXT NOT NULL,
	trainer_id        INT,
	room_id           INT,
	start             TIMESTAMP,
	end               TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (trainer_id)
		REFERENCES trainer (id),
	FOREIGN KEY (room_id)
		REFERENCES room (id)
);

CREATE TABLE personal_session(
	id                SERIAL,
	name              TEXT NOT NULL,
	trainer_id        INT,
	room_id           INT,
	member_id         INT,
	start_time        TIMESTAMP,
	end_time               TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (trainer_id)
		REFERENCES trainer (id),
	FOREIGN KEY (room_id)
		REFERENCES room (id),
	FOREIGN KEY (member_id)
		REFERENCES member (id)
);

CREATE TABLE member_takes_class(
	member_id         INT,
	class_id          INT,
	FOREIGN KEY (member_id)
		REFERENCES member (id),
	FOREIGN KEY (class_id)
		REFERENCES class (id)
);
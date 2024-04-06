CREATE TABLE routine
	(
		id SERIAL PRIMARY KEY,
		name TEXT NOT NULL,
		description TEXT
	);
CREATE TABLE member
	(
		id SERIAL PRIMARY KEY,
		name TEXT NOT NULL,
		password TEXT NOT NULL CHECK (char_length(password) >= 8 AND char_length(password) <= 32),
		age INT NOT NULL,
		weight NUMERIC(5, 2),
		height NUMERIC(5, 2),
		phone VARCHAR(15) UNIQUE,
		address VARCHAR(255),
		email VARCHAR(255) UNIQUE,
		bill_amount NUMERIC(5,2) DEFAULT 250,
		paid BOOLEAN NOT NULL,
		routine_id INT,
		FOREIGN KEY (routine_id) REFERENCES routine(id)
	);
CREATE TABLE goal
	(
		id SERIAL PRIMARY KEY,
		description TEXT,
		member_id INT,
		FOREIGN KEY (member_id) REFERENCES member(id)
	);
CREATE TABLE weight
	(
		id SERIAL PRIMARY KEY,
		kg NUMERIC(5, 2) NOT NULL,
		member_id INT,
		FOREIGN KEY (member_id) REFERENCES member(id)
	);
CREATE TABLE step
	(
		id SERIAL PRIMARY KEY,
		count INT NOT NULL,
		member_id INT,
		FOREIGN KEY (member_id) REFERENCES member(id)
	);
CREATE TABLE heartrate
	(
		id SERIAL PRIMARY KEY,
		bpm NUMERIC(5, 2) NOT NULL,
		member_id INT,
		FOREIGN KEY (member_id) REFERENCES member(id)
	);



	

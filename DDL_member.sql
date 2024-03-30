CREATE TABLE routine
	(
		id SERIAL PRIMARY KEY,
		name VARCHAR(255) NOT NULL,
		description TEXT
	);
CREATE TABLE goal
	(
		id SERIAL PRIMARY KEY,
		description TEXT,
		member_id INT,
		FOREIGN KEY (member_id) REFERENCES member(id)
	);
CREATE TABLE member
	(
		id SERIAL PRIMARY KEY,
		name VARCHAR(255) NOT NULL,
		age INT NOT NULL,
		weight NUMERIC(5, 2),
		height NUMERIC(5, 2),
		phone VARCHAR(15),
		address VARCHAR(255),
		email VARCHAR(255),
		bill_amount NUMERIC(5,2),
		paid BOOLEAN NOT NULL,
		routine_id INT,
		FOREIGN KEY (routine_id) REFERENCES routine(id)
	);
	

CREATE TABLE admin
    (id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL CHECK (char_length(password) >= 8 AND char_length(password) <= 32));

CREATE TABLE room
    (id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
	admin_id INT,	
    FOREIGN KEY (admin_id) REFERENCES admin(id));

CREATE TABLE equipment
	(id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    condition BOOLEAN DEFAULT TRUE,
	room_id INT,
	admin_id INT,	
    FOREIGN KEY (room_id) REFERENCES room(id),
    FOREIGN KEY (admin_id) REFERENCES admin(id));
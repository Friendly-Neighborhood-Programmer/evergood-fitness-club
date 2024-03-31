CREATE TABLE admin
    (id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL CHECK (char_length(name) >= 8 && char_length(name) <= 32));

CREATE TABLE room
    (id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES admin);

CREATE TABLE equipment
    (id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    condition BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (room_id) REFERENCES room,
    FOREIGN KEY (admin_id) REFERENCES admin);
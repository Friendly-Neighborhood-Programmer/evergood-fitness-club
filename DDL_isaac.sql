CREATE TABLE admin
    (id SERIAL PRIMARY KEY,
    name CHAR(20),
    password varchar(50));

CREATE TABLE room
    (id SERIAL PRIMARY KEY,
    name CHAR(20),
    FOREIGN KEY (admin_id) REFERENCES admin);

CREATE TABLE eqipment
    (id SERIAL PRIMARY KEY,
    name CHAR(20),
    condition BOOLEAN,
    FOREIGN KEY (room_id) REFERENCES room,
    FOREIGN KEY (admin_id) REFERENCES admin);
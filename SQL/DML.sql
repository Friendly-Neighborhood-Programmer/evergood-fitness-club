INSERT INTO admin (name, password) VALUES 
    ('bob feta', '12345678'),
    ('prince lee', 'abcdefgh'),
    ('one kobe', 'qwertyui'),
    ('paul patten', '98765432'),
    ('hand yolo', 'lmnopqrs');

INSERT INTO room (name, admin_id) VALUES 
    ('sauna', 1),
    ('free weights', 1),
    ('circuits room', 2),
    ('machine room', 3),
    ('machine room', 3),
    ('cardio room', 4),
    ('cardio room', 4),
    ('training room', 5),
    ('training room', 5),
    ('training room', 5);

INSERT INTO equipment (name, room_id, admin_id) VALUES
    ('dumbbells (10)', 2, 1),
    ('dumbbells (20)', 2, 1),
    ('dumbbells (30)', 2, 1),
    ('dumbbells (40)', 2, 1),
    ('dumbbells (50)', 2, 1),
    ('dumbbells (60)', 2, 1),
    ('dumbbells (70)', 2, 1),
    ('resistance band (weak)', 2, 1),
    ('resistance band (strong)', 2, 1),
    ('dumbbells (20)', 3, 2),
    ('dumbbells (30)', 3, 2),
    ('bike', 3, 2),
    ('bike', 3, 2),
    ('power rack', 4, 3),
    ('smith machine', 4, 3),
    ('cable machine', 4, 3),
    ('leg press', 4, 3),
    ('chest press', 4, 3),
    ('power rack', 5, 3),
    ('smith machine', 5, 5),
    ('cable machine', 5, 5),
    ('leg press', 5, 5),
    ('chest press', 5, 5),
    ('treadmill', 6, 5),
    ('treadmill', 6, 5),
    ('bike', 6, 5),
    ('bike', 6, 5),
    ('eliptical', 6, 4),
    ('eliptical', 6, 4),
    ('treadmill', 7, 4),
    ('treadmill', 7, 4),
    ('bike', 7, 4),
    ('bike', 7, 4),
    ('eliptical', 7, 4),
    ('eliptical', 7, 4);

INSERT INTO routine (name, description) VALUES
    ('Whole Body Workout', 'Bicep Curls - 3 x 8, Tricep Pushdown - 3 x 8, Chest Fly - 3 x 8, Rear Delt Fly - 3 x 8, Barbell Squat - 3 x 8, Lat Pulldown - 3 x 8'),
    ('Aerobics', 'Jumping Jacks - 100, Skipping - 100, Burpees - 100'),
    ('Arms', 'Biceps Curls - 3 x 8, Skull Crushers - 3 x 12, Face Pulls - 3 x 10, Pushups - 30');

INSERT INTO member (name, password, age, phone, gender, address, email, bill_amount, paid, routine_id) VALUES
    ('Dummy', '00000000', 0, '0', 'D', '0', 'dummy@gmail.com', 250, TRUE, 1),
    ('Isaac Robert', '12345678', 30, '613-613-6133', 'M', '1 Malvern Street', 'isaac@gmail.com', 250, FALSE, 1),
    ('Rachel Steward', '12345678', 30, '613-613-6134', 'G', '2 Malvern Street', 'rachel@gmail.com', 250, FALSE, 1);

INSERT INTO goal (description, member_id) VALUES
    ('BECOME BIG STRONG MAN', 1),
    ('BECOME BIG STRONG WOMAN', 2);

INSERT INTO weight (kg, member_id)
VALUES
  (170, 2),
  (140, 3);

INSERT INTO step (count, member_id)
VALUES
  (10000, 2),
  (20000, 3);

INSERT INTO heartrate (bpm, member_id)
VALUES
  (100, 2),
  (100, 3);

INSERT INTO trainer (name, password, specialty) VALUES
    ('lance lift', 'bigmuscles', 'deadlifts'),
    ('tina treadmill', 'I<3running', 'cardio machines'),
    ('max muscle', 'gains4days', 'weight machines'),
    ('holly heartbeat', '95bpmandlovingit', 'zumba');

INSERT INTO class(name, trainer_id, room_id, day, start_time, end_time) VALUES
    ('CycleCraze Spin Studio', 2, 6, 'SUN', '07:00:00', '08:00:00'),
    ('Zumba-Zest Fiesta', 4, 8, 'SAT','06:00:00', '07:00:00'),
    ('TreadTrek Treadmill Training', 2, 7, 'TUE','15:00:00', '16:00:00'),
    ('LiftWell Deadlift Training', 1, 2, 'SAT','07:00:00', '08:00:00'),
    ('Machine Mastery', 3, 4, 'SUN', '06:00:00', '07:00:00');

INSERT INTO personal_session(name, trainer_id, room_id, member_id, day, start_time, end_time) VALUES
    ('1', 1, 8, 1, 'MON', '09:00:00', '10:00:00'),
    ('1', 1, 8, 1, 'MON', '10:00:00', '11:00:00'),
    ('1', 1, 8, 1, 'MON', '11:00:00', '12:00:00'),
    ('1', 1, 8, 1, 'MON', '13:00:00', '14:00:00'),
    ('1', 1, 8, 1, 'MON', '14:00:00', '15:00:00'),
    ('2', 2, 9, 1, 'TUE', '09:00:00', '10:00:00'),
    ('2', 2, 9, 1, 'TUE', '10:00:00', '11:00:00'),
    ('2', 2, 9, 1, 'TUE', '11:00:00', '12:00:00'),
    ('2', 2, 9, 1, 'TUE', '13:00:00', '14:00:00'),
    ('2', 2, 9, 1, 'TUE', '14:00:00', '15:00:00'),
    ('3', 3, 10, 1, 'WED', '09:00:00', '10:00:00'),
    ('3', 3, 10, 1, 'WED', '10:00:00', '11:00:00'),
    ('3', 3, 10, 1, 'WED', '11:00:00', '12:00:00'),
    ('3', 3, 10, 1, 'WED', '13:00:00', '14:00:00'),
    ('3', 3, 10, 1, 'WED', '14:00:00', '15:00:00'),
    ('4', 4, 10, 1, 'THU', '09:00:00', '10:00:00'),
    ('4', 4, 10, 1, 'THU', '10:00:00', '11:00:00'),
    ('4', 4, 10, 1, 'THU', '11:00:00', '12:00:00'),
    ('4', 4, 10, 1, 'THU', '13:00:00', '14:00:00'),
    ('4', 4, 10, 1, 'THU', '14:00:00', '15:00:00');

INSERT INTO member_takes_class(member_id, class_id) VALUES
    (2, 1),
    (2, 2),
    (3, 2),
    (2, 3);

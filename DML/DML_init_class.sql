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
    ('1', 1, 8, NULL, 'MON', '09:00:00', '10:00:00'),
    ('1', 1, 8, NULL, 'MON', '10:00:00', '11:00:00'),
    ('1', 1, 8, NULL, 'MON', '11:00:00', '12:00:00'),
    ('1', 1, 8, NULL, 'MON', '13:00:00', '14:00:00'),
    ('1', 1, 8, NULL, 'MON', '14:00:00', '15:00:00'),
    ('2', 2, 9, NULL, 'TUE', '09:00:00', '10:00:00'),
    ('2', 2, 9, NULL, 'TUE', '10:00:00', '11:00:00'),
    ('2', 2, 9, NULL, 'TUE', '11:00:00', '12:00:00'),
    ('2', 2, 9, NULL, 'TUE', '13:00:00', '14:00:00'),
    ('2', 2, 9, NULL, 'TUE', '14:00:00', '15:00:00'),
    ('3', 3, 10, NULL, 'WED', '09:00:00', '10:00:00'),
    ('3', 3, 10, NULL, 'WED', '10:00:00', '11:00:00'),
    ('3', 3, 10, NULL, 'WED', '11:00:00', '12:00:00'),
    ('3', 3, 10, NULL, 'WED', '13:00:00', '14:00:00'),
    ('3', 3, 10, NULL, 'WED', '14:00:00', '15:00:00'),
    ('4', 4, 10, NULL, 'THU', '09:00:00', '10:00:00'),
    ('4', 4, 10, NULL, 'THU', '10:00:00', '11:00:00'),
    ('4', 4, 10, NULL, 'THU', '11:00:00', '12:00:00'),
    ('4', 4, 10, NULL, 'THU', '13:00:00', '14:00:00'),
    ('4', 4, 10, NULL, 'THU', '14:00:00', '15:00:00');

INSERT INTO member_takes_class(member_id, class_id) VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (1, 3);

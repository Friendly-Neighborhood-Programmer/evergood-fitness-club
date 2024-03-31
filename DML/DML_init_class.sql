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

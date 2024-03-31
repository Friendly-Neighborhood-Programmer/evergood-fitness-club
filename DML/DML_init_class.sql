INSERT INTO trainer (name, password, specialty) VALUES
    ('lance lift', 'bigmuscles', 'deadlifts'),
    ('tina treadmill', 'I<3running', 'cardio machines'),
    ('max muscle', 'gains4days', 'weight machines'),
    ('holly heartbeat', '95bpmandlovingit', 'zumba');

INSERT INTO class(name, trainer_id, room_id, day, start_time, end_time) VALUES
    ('CycleCraze Spin Studio', 2, 6, 'SUN', '07:00:00', '08:30:00'),
    ('Zumba-Zest Fiesta', 4, 8, 'MON','06:00:00', '07:30:00'),
    ('TreadTrek Treadmill Training', 2, 7, 'TUE','15:30:00', '16:30:00');

INSERT INTO personal_session(name, trainer_id, room_id, member_id, day, start_time, end_time) VALUES
    ('LiftWell Personal Deadlift Training', 1, 2, 1, 'WED','07:00:00', '08:30:00'),
    ('Machine Mastery', 3, 4, 2, 'THU', '06:00:00', '07:30:00');

INSERT INTO member_takes_class(member_id, class_id) VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (1, 3);

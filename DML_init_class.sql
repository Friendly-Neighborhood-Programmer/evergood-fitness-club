INSERT INTO trainer (name, password, specialty) VALUES
    ('lance lift', 'bigmuscles', 'deadlifts'),
    ('tina treadmill', 'I<3running', 'cardio machines'),
    ('max muscle', 'gains4days', 'weight machines'),
    ('holly heartbeat', '95bpmandlovingit', 'zumba');

INSERT INTO class(name, trainer_id, room_id, start, end) VALUES
    ('CycleCraze Spin Studio', 2, 6, '2024-04-27 07:00:00', '2023-04-27 8:30:00'),
    ('Zumba-Zest Fiesta', 4, 8, '2024-04-25 06:00:00', '2023-04-25 7:30:00'),
    ('TreadTrek Treadmill Training', 2, 7, '2023-04-23 15:30:00', '2023-04-23 16:30:00');

INSERT INTO personal_session(name, trainer_id, room_id, member_id, start, end) VALUES
    ('LiftWell Personal Deadlift Training', 1, 2, 1, '2024-04-22 07:00:00', '2023-04-22 8:30:00'),
    ('Machine Mastery', 3, 4, 2, '2024-04-21 06:00:00', '2023-04-21 7:30:00');

INSERT INTO member_takes_class(member_id, class_id) VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (1, 3);

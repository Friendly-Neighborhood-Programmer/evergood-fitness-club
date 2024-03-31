INSERT INTO routine (name, description)
VALUES
  ("Whole Body Workout", "Bicep Curls - 3 x 8, Tricep Pushdown - 3 x 8, Chest Fly - 3 x 8, Rear Delt Fly - 3 x 8, Barbell Squat - 3 x 8, Lat Pulldown - 3 x 8"),
  ("Aerobics", "Jumping Jacks - 100, Skipping - 100, Burpees - 100");

INSERT INTO member (name, password, age, weight, height, phone, address, email, bill_amount, paid, routine_id)
VALUES
  ("Isaac Roberts", "12345678", 30, 170, "613-613-6133", "1 Malvern Street", "isaac@gmail.com", 250, FALSE, 1),
  ("Rachel Steward", "12345678", 30, 140, "613-613-6134", "2 Malvern Street", "rachel@gmail.com", 250, FALSE, 1),
  ("Dummy", "12345678", 30, 170, "613-613-6133", "1 Malvern Street", "dummy@gmail.com", 250, TRUE, 1);

INSERT INTO goal (description, member_id)
VALUES
  ("BECOME BIG STRONG MAN", 1),
  ("BECOME BIG STRONG WOMAN", 2);


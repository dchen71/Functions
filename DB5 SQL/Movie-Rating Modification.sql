/*
SQLite Syntax

Schema:
Highschooler ( ID, name, grade )
English: There is a high school student with unique ID and a given first name in a certain grade.

Friend ( ID1, ID2 )
English: The student with ID1 is friends with the student with ID2. Friendship is mutual, so if (123, 456) is in the Friend table, so is (456, 123).

Likes ( ID1, ID2 )
English: The student with ID1 likes the student with ID2. Liking someone is not necessarily mutual, so if (123, 456) is in the Likes table, there is no guarantee that (456, 123) is also present. 
 */

/*
Q1:
It's time for the seniors to graduate. Remove all 12th graders from Highschooler. 
 */

DELETE FROM Highschooler
WHERE grade = 12

/*
Q2:
If two students A and B are friends, and A likes B but not vice-versa, remove the Likes tuple. 
*/

DELETE FROM Likes
WHERE exists (SELECT * FROM Friend F WHERE F.id1 = Likes.id1 AND F.id2 = Likes.id2) AND
      not exists (SELECT * FROM Likes L2 WHERE Likes.id1 = L2.id2 AND Likes.id2 = L2.id1) 

/*
Q3:
For all cases where A is friends with B, and B is friends with C, add a new friendship for the pair A and C. Do not add duplicate friendships, friendships that already exist, or friendships with oneself. (This one is a bit challenging; congratulations if you get it right.) 
 */

INSERT INTO Friend (id1,id2)
SELECT 
FROM 
WHERE 
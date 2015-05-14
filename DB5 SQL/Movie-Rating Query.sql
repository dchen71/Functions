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
Find the names of all students who are friends with someone named Gabriel. 
 */

SELECT name
FROM Highschooler H 
  Join Friend on
  Friend.id1 = H.id
WHERE id2 in (SELECT id
              FROM Highschooler
              WHERE name = 'Gabriel')

/*
Q2:
For every student who likes someone 2 or more grades younger than themselves, 
return that student's name and grade, and the name and grade of the student they like. 
 */

SELECT H.name, H.grade, H2.name, H2.grade
FROM Highschooler H 
  JOIN Likes ON
  Likes.id1 = H.id 
  JOIN Highschooler H2 ON
  H2.id = Likes.id2
WHERE H2.grade <= H.grade - 2

/*
Q3:
For every pair of students who both like each other, return the name and grade of both students. 
Include each pair only once, with the two names in alphabetical order. 
 */

SELECT H1.name, H1.grade,H2.name,H2.grade 
FROM Highschooler H1, Highschooler H2, Likes L1, Likes L2
WHERE L1.ID1 = L2.ID2 AND L2.ID1 = L1.ID2 AND L1.ID1 = H1.ID AND L1.ID2 = H2.ID
      AND H1.name < H2.name

/*
Q4:
Find all students who do not appear in the Likes table (as a student who likes or is liked) and 
return their names and grades. Sort by grade, then by name within each grade. 
 */

SELECT H1.name, H1.grade
FROM Highschooler H1 
GROUP BY grade,name
HAVING H1.id not in (SELECT id1
                     FROM Likes)
  AND H1.id not in (SELECT id2
                   FROM Likes)

/*
Q5:
For every situation where student A likes student B, but we have no information about whom B likes 
(that is, B does not appear as an ID1 in the Likes table), return A and B's names and grades. 
 */

SELECT H1.name, H1.grade,H2.name,H2.grade 
FROM Highschooler H1, Highschooler H2, Likes L
WHERE L.ID1 = H1.ID AND L.ID2 = H2.ID AND H2.ID NOT IN (SELECT ID1
                                                        FROM Likes)


/*
Q6:
Find names and grades of students who only have friends in the same grade. Return the result sorted 
by grade, then by name within each grade. 
 */

SELECT distinct name, grade
FROM Highschooler H, Friend F
WHERE ID NOT IN (SELECT distinct H1.ID
             FROM Highschooler H1, Friend F, Highschooler H2
             WHERE H1.ID = F.ID1 AND H2.ID = F.ID2 
             AND H2.grade <> H1.grade)
ORDER BY grade

/*
Q7:
For each student A who likes a student B where the two are not friends, find if they have a friend C in 
common (who can introduce them!). For all such trios, return the name and grade of A, B, and C. 
 */

SELECT distinct H1.name, H1.grade, H2.name, H2.grade, H3.name, H3.grade
FROM Highschooler H1, Likes L, Highschooler H2, Highschooler H3, Friend F1, Friend F2
WHERE H1.ID = L.ID1 AND L.ID2 = H2.ID AND
    H2.ID NOT IN (SELECT ID2 FROM Friend WHERE ID1 = H1.ID) AND
    H1.ID = F1.ID1 AND F1.ID2 = H3.ID AND
    H3.ID = F2.ID1 AND F2.ID2 = H2.ID

/*
Q8:
Find the difference between the number of students in the school and the number of different first names. 
 */

SELECT count(*) - count(distinct name)
FROM Highschooler

/*
Q9:
Find the name and grade of all students who are liked by more than one other student. 
 */

SELECT Highschooler.name, grade
FROM Highschooler 
  JOIN Likes ONLikes.ID2 = Highschooler.ID
GROUP BY ID2
HAVING COUNT(ID2) > 1
/*
SQLite Syntax

Schema:
Movie ( mID, title, year, director )
English: There is a movie with ID number mID, a title, a release year, and a director.

Reviewer ( rID, name )
English: The reviewer with ID number rID has a certain name.

Rating ( rID, mID, stars, ratingDate )
English: The reviewer rID gave the movie mID a number of stars rating (1-5) on a certain ratingDate. 
 */

/*
Q1:
Add the reviewer Roger Ebert to your database, with an rID of 209. 
 */

INSERT INTO Reviewer values(209,"Roger Ebert")

/*
Q2:
Insert 5-star ratings by James Cameron for all movies in the database. Leave the review date as NULL. 
 */

INSERT into Rating  ( rID, mID, stars, ratingDate )
SELECT Reviewer.rID , Movie.mID, 5, null 
FROM Movie
LEFT OUTER JOIN Reviewer
WHERE Reviewer.name="James Cameron"

/*
Q3:
For all movies that have an average rating of 4 stars or higher, add 25 to the release year. 
(Update the existing tuples; don't insert new tuples.) 
 */

UPDATE Movie 
set year = year + 25
WHERE mID in (
  SELECT Rating.mID
  FROM Movie JOIN Rating on
  Movie.mid = Rating.mID
  GROUP BY Rating.mID
  HAVING avg(stars) >= 4)

/*
Q4:
Remove all ratings where the movie's year is before 1970 or after 2000, and the rating is fewer than 4 stars. 
 */

DELETE FROM Rating
WHERE mID in (
     SELECT Rating.mID
     FROM Rating Join Movie on
     Rating.mID = Movie.mID
     WHERE year < 1970 OR year > 2000)
     AND stars < 4
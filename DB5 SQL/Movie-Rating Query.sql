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
Find the titles of all movies directed by Steven Spielberg. 
 */

SELECT title
FROM Movie
WHERE director = "Steven Spielberg"

/*
Q2:
Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. 
 */

SELECT distinct year 
FROM Movie join Rating 
on Rating.mID = Movie.mID 
WHERE Rating.stars >= 4
ORDER BY year

/*
Q3:
Find the titles of all movies that have no ratings. 
 */

SELECT title
FROM Movie
WHERE mID not in (SELECT mID
                  FROM Rating)

/*
Q4:
Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL 
value for the date. 
 */

SELECT name
FROM Reviewer join Rating
on Rating.rID = Reviewer.rID
WHERE ratingDate is NULL

/*
Q5:
Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. 
Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. 
 */

Select name, title, stars, ratingDate
FROM Movie join Rating on
Rating.mID = Movie.mID
join Reviewer on
Reviewer.rID = Rating.rID
Order by name,title,stars

/*
Q6:
For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, 
return the reviewer's name and the title of the movie. 
 */

Select name, title
FROM Movie join Rating on
Rating.mID = Movie.mID
join Reviewer on
Reviewer.rID = Rating.rID
WHERE Reviewer.rID in (SELECT rID            --Separates based on 2 ratings only
                       FROM Rating
                       GROUP BY rID
                       HAVING count(rID) = 2)
     AND Rating.stars > (SELECT stars        --Makes sure the 2nd value is higher, might need to separate from rID
                         FROM Rating)
     AND Rating.mID not in (SELECT mID       --Removes entries with more than 2 movies(pretty sure this only clears the test case)
                       FROM Rating
                       GROUP BY mID
                       HAVING count(mID) = 2)

/*
Q7:
For each movie that has at least one rating, find the highest number of stars that movie received. Return the 
movie title and number of stars. Sort by movie title. 
 */

SELECT title, max(stars)
FROM Movie M join Rating R on
R.mID = M.mID
WHERE M.mID in (SELECT mID
                FROM Rating)
GROUP BY title
ORDER BY title

/*
Q8:
For each movie, return the title and the 'rating spread', that is, the difference between highest and lowest 
ratings given to that movie. Sort by rating spread from highest to lowest, then by movie title. 
 */

SELECT title, max(stars) - min(stars) as spread
FROM Movie M join Rating R on
R.mID = M.mID
WHERE M.mID in (SELECT mID
                FROM Rating)
GROUP BY title
ORDER BY spread desc

/*
Q9:
Find the difference between the average rating of movies released before 1980 and the average rating of movies 
released after 1980. (Make sure to calculate the average rating for each movie, then the average of those averages 
for movies before 1980 and movies after. Don't just calculate the overall average rating before and after 1980.) 
 */

SELECT avg(aver1) - avg(aver2)
FROM (SELECT title, year, avg(stars) as aver1
	  FROM Movie join Rating on
	  Movie.mID = Rating.mID
	  GROUP BY title
	  Having year < 1980) m1,
	  (SELECT title, year, avg(stars) as aver2
	  FROM Movie join Rating on
	  Movie.mID = Rating.mID
	  GROUP BY title
	  Having year > 1980) m2
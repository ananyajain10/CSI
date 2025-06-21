--https://www.hackerrank.com/challenges/weather-observation-station-4/problem

SELECT COUNT(*) - COUNT(DISTINCT CITY) AS Difference
FROM STATION;

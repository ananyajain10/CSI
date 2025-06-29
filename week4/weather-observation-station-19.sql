---https://www.hackerrank.com/challenges/weather-observation-station-19/problem

SELECT CAST (
    SQRT (
        SQUARE(MIN([LAT_N]) - MAX([LAT_N])) +
        SQUARE(MIN([LONG_W]) - MAX([LONG_W]))
    )
    AS DECIMAL(10,4)
)
FROM STATION;
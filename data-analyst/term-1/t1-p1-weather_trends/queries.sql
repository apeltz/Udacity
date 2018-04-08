-- Explore data formats; get data types and syntax from schema
SELECT *
	FROM city_list
	LIMIT 10;

SELECT *
	FROM city_data
	LIMIT 10;

SELECT *
	FROM global_data
	LIMIT 10;

-- This works because there are no instances of these cities in other countries
SELECT *
	FROM city_list
    WHERE city IN ('Los Angeles', 'London', 'Moscow')
    AND country IN ('United States', 'United Kingdom', 'Russia')
	LIMIT 10;

-- Get city data
SELECT year, city, avg_temp
	FROM city_data
    WHERE city IN ('Los Angeles', 'London', 'Moscow')
    AND country IN ('United States', 'United Kingdom', 'Russia')
    AND year >= 1900
	ORDER BY city, year;

-- Get global data
SELECT *
	FROM global_data
    WHERE year >= 1900
	ORDER BY year;
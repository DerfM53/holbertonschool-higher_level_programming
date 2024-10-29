-- List values of cities of California and sorted result at small to big id 
SELECT cities.id, cities.name FROM cities WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
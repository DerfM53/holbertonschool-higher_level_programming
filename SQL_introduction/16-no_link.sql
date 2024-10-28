-- Script that lists all records of the table second_table
-- Excludes rows without a name value
-- Displays the score and name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

CREATE TABLE second_table (id INT, name VARCHAR(256), score INT) AS SELECT 1 AS id, "John" AS name, 10 AS score UNION ALL SELECT 2, "Alex", 3 UNION ALL SELECT 3, "Bob", 14 UNION ALL SELECT 4, "George", 8;

-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Enter in database hbtn_0d_usa
USE hbtn_0d_usa;
-- Create table states with primary key and auto-generated id an value name
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);

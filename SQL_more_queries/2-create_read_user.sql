-- Create the database hbtn_0d_2 if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Replace or create the password for the user if it exists
ALTER USER IF EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Create user user_0d_2 if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Revoke all existing privileges to ensure only SELECT will be granted
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_2'@'localhost';
-- Grant SELECT privilege to user_0d_2 on the hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Apply the changes
FLUSH PRIVILEGES;
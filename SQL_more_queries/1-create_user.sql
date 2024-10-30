-- script that creates the MySQL server user user_0d_1 and grant all previligies to it
CREATE USER IF NOT EXISTS "user_0d_1"@"localhost" IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* to "user_0d_1"@"localhost";

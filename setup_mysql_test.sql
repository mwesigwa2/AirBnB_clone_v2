--- create A database hbnb_test_db
--- A new user hbnb_test (in localhost)
CREATE DATABASE IF NOT EXISTS 'hbnb_test_db';
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnbhbnb_test'@'localhost';
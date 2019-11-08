-- creates database bh_test_db
CREATE DATABASE IF NOT EXISTS bh_test_db;
USE bh_test_db;
CREATE USER IF NOT EXISTS 'bh_test'@'localhost';
SET PASSWORD FOR 'bh_test'@'localhost' = 'bh_test_pwd';
GRANT ALL PRIVILEGES ON bh_test_db.* TO 'bh_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'bh_test'@'localhost';

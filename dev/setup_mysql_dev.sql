-- Creates database bh_dev_db
CREATE DATABASE IF NOT EXISTS bh_dev_db;
USE bh_dev_db;
CREATE USER IF NOT EXISTS 'bh_dev'@'localhost';
SET PASSWORD FOR 'bh_dev'@'localhost' = 'bh_dev_pwd';
GRANT ALL PRIVILEGES ON bh_dev_db.* TO 'bh_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'bh_dev'@'localhost';

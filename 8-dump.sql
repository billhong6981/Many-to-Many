-- MySQL dump 10.13  Distrib 5.7.8-rc, for Linux (x86_64)
--
-- Host: localhost    Database: bh_dev_db
-- ------------------------------------------------------
-- Server version	5.7.8-rc

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Drop database
DROP DATABASE IF EXISTS bh_dev_db;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS bh_dev_db;
CREATE USER IF NOT EXISTS 'bh_dev'@'localhost';
SET PASSWORD FOR 'bh_dev'@'localhost' = 'bh_dev_pwd';
GRANT ALL ON bh_dev_db.* TO 'bh_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'bh_dev'@'localhost';
FLUSH PRIVILEGES;

USE bh_dev_db;

--
-- Table structure for table `todos`
--

DROP TABLE IF EXISTS `todos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `todos` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `title` varchar(128) NOT NULL,
  `due_date` datetime NOT NULL,
  `completed` int  NOT NULL  DEFAULT 0,
  `description` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todos`
--

LOCK TABLES `todos` WRITE;
/*!40000 ALTER TABLE `todos` DISABLE KEYS */;
INSERT INTO `todos` VALUES ('017ec502-e84a-4a0f-92d6-d97e27bb6bdf','2017-03-25 02:17:06','2017-03-25 02:17:06','delectus aut autem','2019-02-03','1','well done'),('0d375b05-5ef9-4d43-aaca-436762bb25bf','2017-03-25 02:17:06','2017-03-25 02:17:06','quis ut nam facilis et officia qui','2019-11-05','0','need to follow up'),('12e9ccb4-03e4-4f82-ac3d-4fc7e3ebfbfe','2017-03-25 02:17:06','2017-03-25 02:17:06','fugiat veniam minus','2019-12-01','0','search online'),('1e0f976d-beef-497b-b29c-b4a25d1c071a','2017-03-25 02:17:06','2017-03-25 02:17:06','et porro tempora','2020-01-02','0','Other pet(s)'),('20f281b1-2cd1-4e36-a7c7-d1062ff16bcd','2017-03-25 02:17:06','2017-03-25 02:17:06','laboriosam mollitia et enim quasi adipisci quia provident illum','2019-09-09','1','Smartlock'),('28ff856a-2cfb-44df-91b8-1285914553c8','2017-03-25 02:17:06','2017-03-25 02:17:06','qui ullam ratione quibusdam voluptatem quia omnis','2019-11-11','0','prepare material'),('2a98b8af-1cd7-4236-a99e-7200c992fad7','2017-03-25 02:17:06','2017-03-25 02:17:06','illo expedita consequatur quia in','2019-10-15','1','9 out of 10'),('2c620702-d41c-4732-a1cf-6e40f7877dc3','2017-03-25 02:17:06','2017-03-25 02:17:06','quo adipisci enim quam ut ab','2019-10-24','0','Self Check-In'),('2f055228-5fd3-4b1d-a021-7e4b9b7d70a6','2017-03-25 02:17:06','2017-03-25 02:17:06','molestiae perspiciatis ipsa','2019-9-19','0','too much TV shows'),('3e73edf2-c3d6-409f-9202-213df4a7a25a','2017-03-25 02:17:06','2017-03-25 02:17:06','illo est ratione doloremque quia maiores aut','2019-10-28','1','Cat(s)'),('3fccec93-2842-49a0-8fdb-4008af2ef041','2017-03-25 02:17:06','2017-03-25 02:17:06','vero rerum temporibus dolor','2019-11-08','1','very good'),('416cddd7-746e-4715-821c-3ad30b9bc3c3','2017-03-25 02:17:06','2017-03-25 02:17:06','ipsa repellendus fugit nisi','2019-11-10','0','Gym'),('43d414fb-0fff-4ea9-8c44-3819ec041c9b','2017-03-25 02:17:06','2017-03-25 02:17:06','et doloremque nulla','2019-10-30','1','Essentials'),('43de9883-8b2d-44dc-81d3-8b719ea50734','2017-03-25 02:17:06','2017-03-25 02:17:06','repellendus sunt dolores architecto voluptatum','2019-11-1','1','Heating'),('47327246-6852-4c70-b3db-77077ab61a32','2017-03-25 02:17:06','2017-03-25 02:17:06','ab voluptatum amet voluptas','2019-10-29','1','Family/kid friendly'),('49fcaedc-481a-4e05-934f-4867988c8ec5','2017-03-25 02:17:06','2017-03-25 02:17:06','accusamus eos facilis sint et aut voluptatem','2019-11-02','0','Wireless Internet'),('4a0a3fa7-21a0-411a-bb0a-9b4eed1901ef','2017-03-25 02:17:06','2017-03-25 02:17:06','quo laboriosam deleniti aut qui','2019-10-25','1','Pets allowed'),('4e320c4e-deb6-4ccb-b45e-b77a5df3ff40','2017-03-25 02:17:06','2017-03-25 02:17:06','dolorum est consequatur ea mollitia in culpa','2019-10-28','1','Kitchen painting'),('5429dc8c-799d-4555-98c6-f2d714a9fe50','2017-03-25 02:17:06','2017-03-25 02:17:06','molestiae ipsa aut voluptatibus pariatur dolor nihil','2019-11-04','0','Doorman Entry'),('6b9c3987-a344-4baf-8d11-077d719688ba','2017-03-25 02:17:06','2017-03-25 02:17:06','ullam nobis libero sapiente ad optio sint','2019-10-22','0','Lock on bedroom door'),('6dd36c9f-9863-4850-a810-a7629fe07d72','2017-03-25 02:17:06','2017-03-25 02:17:06','suscipit repellat esse quibusdam voluptatem incidunt','2019-11-06','0','Fix Washer'),('8d5b1bf3-4bd2-4283-86ce-91211fbc788d','2017-03-25 02:17:06','2017-03-25 02:17:06','distinctio vitae autem nihil ut molestias quo','2019-11-07','0','buy Keypad'),('919be9d0-5789-4b56-b785-0e4d72ecc8ba','2017-03-25 02:17:06','2017-03-25 02:17:06','et itaque necessitatibus maxime molestiae qui quas velit','2019-10-21','1','turn off Air conditioning'),('92709c8a-65d4-4fb9-811a-f25ef328822e','2017-03-25 02:17:06','2017-03-25 02:17:06','adipisci non ad dicta qui amet quaerat doloribus ea','2019-10-29','1','Suitable for events'),('98850f9d-0835-46df-90e3-5fef156724a0','2017-03-25 02:17:06','2017-03-25 02:17:06','voluptas quo tenetur perspiciatis explicabo natus','2019-11-09','0','Laptop friendly workspace'),('9c54e3ed-48b3-4438-bb2c-304e14a9bde4','2017-03-25 02:17:06','2017-03-25 02:17:06','aliquam aut quasi','2019-10-11','1','take Breakfast'),('a6fc4fa4-345b-4c64-aee9-791afaf10f11','2017-03-25 02:17:06','2017-03-25 02:17:06','veritatis pariatur delectus','2019-11-03','1','Smoke detector'),('baf27726-2b9c-4cb4-ad97-2baec4527be6','2017-03-25 02:17:06','2017-03-25 02:17:06','nesciunt totam sit blanditiis sit','2019-09-11','1','8 out of 10'),('c4b9d932-71f4-4f10-9e09-502c3eb67ee2','2017-03-25 02:17:06','2017-03-25 02:17:06','laborum aut in quam','2019-10-29','1','Safety card'),('cb0c9658-79a7-41ac-b816-4201f3e98d80','2017-03-25 02:17:06','2017-03-25 02:17:06','nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis','2019-08-10','0','not finished, postpond'),('cf701d1a-3c19-4bac-bd99-15321f1140f2','2017-03-25 02:17:06','2017-03-25 02:17:06','repudiandae totam in est sint facere fuga','2019-11-06','1','finished early'),('d087d6cd-2ded-4bf7-8f32-61612a2da417','2017-03-25 02:17:06','2017-03-25 02:17:06','earum doloribus ea doloremque quis','2019-11-11','0','Hangers'),('d3cb5b63-2f99-4c55-86a7-3127eb4a8128','2017-03-25 02:17:06','2017-03-25 02:17:06','sint sit aut vero','2019-8-05','1','Buzzer/wireless intercom'),('d7275f8c-70e5-4c27-bcd6-aafd5256fccd','2017-03-25 02:17:06','2017-03-25 02:17:06','porro aut necessitatibus eaque distinctio','2019-10-26','1','Carbon monoxide detector'),('dcfb45cc-b170-4ace-97af-9957b564606a','2017-03-25 02:17:06','2017-03-25 02:17:06','repellendus veritatis molestias dicta incidunt','2019-09-09','1','Indoor fireplace'),('e7680872-7b76-4565-aa8b-6c3d182caa1c','2017-03-25 02:17:06','2017-03-25 02:17:06','excepturi deleniti adipisci voluptatem et neque optio illum ad','2019-10-28','1','Private entrance'),('ea518e20-3370-4cb3-b38f-df1cccbdd8a9','2017-03-25 02:17:06','2017-03-25 02:17:06','sunt cum tempora','2019-09-29','1','fix Dryer'),('efafcf4e-59cf-45e2-b8c5-e14ae252ca01','2017-03-25 02:17:06','2017-03-25 02:17:06','totam quia non','2019-07-25','1','hire Doorman'),('f4dfd576-7c29-4bdf-9fbd-5c95a170ebce','2017-03-25 02:17:06','2017-03-25 02:17:06','doloremque quibusdam asperiores libero corrupti illum qui omnis','2019-11-03','0','buy Hair dryer'),('f4e98f0a-053a-42e2-9633-0cca2a587410','2017-03-25 02:17:06','2017-03-25 02:17:06','totam atque quo nesciunt','2019-10-30','0','swimming Pool'),('f7a087bb-13e2-463d-a951-b8feb7da899f','2017-03-25 02:17:06','2017-03-25 02:17:06','aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit','2019-11-01','1','Smoking allowed'),('f7c854a4-f565-4aa5-8542-c4e17c498ef1','2017-03-25 02:17:06','2017-03-25 02:17:06','rerum perferendis error quia ut eveniet','2019-11-04','0','First aid kit');
/*!40000 ALTER TABLE `todos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_todo`
--

DROP TABLE IF EXISTS `employee_todo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_todo` (
  `employee_id` varchar(60) NOT NULL,
  `todo_id` varchar(60) NOT NULL,
  PRIMARY KEY (`employee_id`,`todo_id`),
  KEY `todo_id` (`todo_id`),
  CONSTRAINT `employee_todo_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `employee_todo_ibfk_2` FOREIGN KEY (`todo_id`) REFERENCES `todos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_todo`
--

LOCK TABLES `employee_todo` WRITE;
/*!40000 ALTER TABLE `employee_todo` DISABLE KEYS */;
INSERT INTO `employee_todo` VALUES ('426624f6-84a9-4ec4-84f3-7655dc70e86e','017ec502-e84a-4a0f-92d6-d97e27bb6bdf'),('5e181cc6-cac7-49e9-a7a1-3095b0f9010b','0d375b05-5ef9-4d43-aaca-436762bb25bf'),('61302be9-4b31-4be0-92fc-d0dda253e167','12e9ccb4-03e4-4f82-ac3d-4fc7e3ebfbfe'),('70b18dcc-08ef-4040-91cf-4075973d320a','1e0f976d-beef-497b-b29c-b4a25d1c071a'),('7231eaa1-400f-4cb5-a867-f5eba8adbb81','20f281b1-2cd1-4e36-a7c7-d1062ff16bcd'),('f9b11370-f316-492c-92da-014d7bce7213','28ff856a-2cfb-44df-91b8-1285914553c8'),('fa44780d-ac48-41ab-9dd0-ac54a15755cf','2a98b8af-1cd7-4236-a99e-7200c992fad7'),('7771bbe9-92ab-46d1-a636-864526361d7d','2c620702-d41c-4732-a1cf-6e40f7877dc3'),('8394fd35-8a8a-479f-a398-48f53b4a6554','2f055228-5fd3-4b1d-a021-7e4b9b7d70a6'),('85651506-c13c-4c2f-9c79-8fbebc048e39','3e73edf2-c3d6-409f-9202-213df4a7a25a'),('887dcd8d-d5ee-48de-9626-73ff4ea732fa','3fccec93-2842-49a0-8fdb-4008af2ef041'),('91e27a07-1f47-43c9-b851-60c6882abcd3','416cddd7-746e-4715-821c-3ad30b9bc3c3'),('9e7b2291-3bff-43b9-9241-8ff685e7a6dd','43d414fb-0fff-4ea9-8c44-3819ec041c9b'),('9eec6c06-5918-4867-833a-face490d4715','43de9883-8b2d-44dc-81d3-8b719ea50734'),('aa92d1ff-f0ad-4ba3-9c20-2afef207bf70','47327246-6852-4c70-b3db-77077ab61a32'),('b6160096-c503-4909-a674-7bfbddc8cc45','49fcaedc-481a-4e05-934f-4867988c8ec5'),('c81d66a3-f0fe-44e9-9f31-cb3c6f27db4e','4a0a3fa7-21a0-411a-bb0a-9b4eed1901ef'),('cf1780e6-d294-4113-8749-1c728b9e3f81','4e320c4e-deb6-4ccb-b45e-b77a5df3ff40'),('d622edfa-fc35-4732-b5ec-a15d794267ec','5429dc8c-799d-4555-98c6-f2d714a9fe50'),('df668e22-e344-4c89-a050-e5ad211cbaa6','6b9c3987-a344-4baf-8d11-077d719688ba'),('dfc6b9a5-6673-4f1b-83cd-0dfa800c0d08','6dd36c9f-9863-4850-a810-a7629fe07d72'),('dfed3ea3-c133-47e8-8cfa-312eecbcc56d','8d5b1bf3-4bd2-4283-86ce-91211fbc788d'),('f33e2624-520b-4bc2-b6a0-190ee1d41855','919be9d0-5789-4b56-b785-0e4d72ecc8ba'),('426624f6-84a9-4ec4-84f3-7655dc70e86e','92709c8a-65d4-4fb9-811a-f25ef328822e'),('5e181cc6-cac7-49e9-a7a1-3095b0f9010b','98850f9d-0835-46df-90e3-5fef156724a0'),('61302be9-4b31-4be0-92fc-d0dda253e167','9c54e3ed-48b3-4438-bb2c-304e14a9bde4'),('70b18dcc-08ef-4040-91cf-4075973d320a','a6fc4fa4-345b-4c64-aee9-791afaf10f11'),('7231eaa1-400f-4cb5-a867-f5eba8adbb81','baf27726-2b9c-4cb4-ad97-2baec4527be6'),('f9b11370-f316-492c-92da-014d7bce7213','c4b9d932-71f4-4f10-9e09-502c3eb67ee2'),('fa44780d-ac48-41ab-9dd0-ac54a15755cf','cb0c9658-79a7-41ac-b816-4201f3e98d80'),('7771bbe9-92ab-46d1-a636-864526361d7d','cf701d1a-3c19-4bac-bd99-15321f1140f2'),('8394fd35-8a8a-479f-a398-48f53b4a6554','d087d6cd-2ded-4bf7-8f32-61612a2da417'),('85651506-c13c-4c2f-9c79-8fbebc048e39','d3cb5b63-2f99-4c55-86a7-3127eb4a8128'),('887dcd8d-d5ee-48de-9626-73ff4ea732fa','d7275f8c-70e5-4c27-bcd6-aafd5256fccd'),('91e27a07-1f47-43c9-b851-60c6882abcd3','dcfb45cc-b170-4ace-97af-9957b564606a'),('9e7b2291-3bff-43b9-9241-8ff685e7a6dd','e7680872-7b76-4565-aa8b-6c3d182caa1c'),('9eec6c06-5918-4867-833a-face490d4715','ea518e20-3370-4cb3-b38f-df1cccbdd8a9'),('aa92d1ff-f0ad-4ba3-9c20-2afef207bf70','efafcf4e-59cf-45e2-b8c5-e14ae252ca01'),('b6160096-c503-4909-a674-7bfbddc8cc45','f4dfd576-7c29-4bdf-9fbd-5c95a170ebce'),('c81d66a3-f0fe-44e9-9f31-cb3c6f27db4e','f4e98f0a-053a-42e2-9633-0cca2a587410'),('cf1780e6-d294-4113-8749-1c728b9e3f81','f7a087bb-13e2-463d-a951-b8feb7da899f'),('d622edfa-fc35-4732-b5ec-a15d794267ec','f7c854a4-f565-4aa5-8542-c4e17c498ef1'),('df668e22-e344-4c89-a050-e5ad211cbaa6','f7c854a4-f565-4aa5-8542-c4e17c498ef1'),('dfc6b9a5-6673-4f1b-83cd-0dfa800c0d08','f7c854a4-f565-4aa5-8542-c4e17c498ef1'),('dfed3ea3-c133-47e8-8cfa-312eecbcc56d','f7c854a4-f565-4aa5-8542-c4e17c498ef1'),('f33e2624-520b-4bc2-b6a0-190ee1d41855','f7a087bb-13e2-463d-a951-b8feb7da899f'),('426624f6-84a9-4ec4-84f3-7655dc70e86e','f7a087bb-13e2-463d-a951-b8feb7da899f'),('5e181cc6-cac7-49e9-a7a1-3095b0f9010b','f4e98f0a-053a-42e2-9633-0cca2a587410'),('61302be9-4b31-4be0-92fc-d0dda253e167','f4e98f0a-053a-42e2-9633-0cca2a587410'),('70b18dcc-08ef-4040-91cf-4075973d320a','f4dfd576-7c29-4bdf-9fbd-5c95a170ebce'),('7231eaa1-400f-4cb5-a867-f5eba8adbb81','ea518e20-3370-4cb3-b38f-df1cccbdd8a9'),('f9b11370-f316-492c-92da-014d7bce7213','e7680872-7b76-4565-aa8b-6c3d182caa1c'),('fa44780d-ac48-41ab-9dd0-ac54a15755cf','d7275f8c-70e5-4c27-bcd6-aafd5256fccd'),('7771bbe9-92ab-46d1-a636-864526361d7d','d087d6cd-2ded-4bf7-8f32-61612a2da417'),('8394fd35-8a8a-479f-a398-48f53b4a6554','cb0c9658-79a7-41ac-b816-4201f3e98d80'),('85651506-c13c-4c2f-9c79-8fbebc048e39','c4b9d932-71f4-4f10-9e09-502c3eb67ee2'),('887dcd8d-d5ee-48de-9626-73ff4ea732fa','baf27726-2b9c-4cb4-ad97-2baec4527be6'),('91e27a07-1f47-43c9-b851-60c6882abcd3','a6fc4fa4-345b-4c64-aee9-791afaf10f11'),('9e7b2291-3bff-43b9-9241-8ff685e7a6dd','a6fc4fa4-345b-4c64-aee9-791afaf10f11'),('9eec6c06-5918-4867-833a-face490d4715','98850f9d-0835-46df-90e3-5fef156724a0'),('aa92d1ff-f0ad-4ba3-9c20-2afef207bf70','92709c8a-65d4-4fb9-811a-f25ef328822e'),('b6160096-c503-4909-a674-7bfbddc8cc45','919be9d0-5789-4b56-b785-0e4d72ecc8ba'),('c81d66a3-f0fe-44e9-9f31-cb3c6f27db4e','8d5b1bf3-4bd2-4283-86ce-91211fbc788d'),('cf1780e6-d294-4113-8749-1c728b9e3f81','6dd36c9f-9863-4850-a810-a7629fe07d72'),('d622edfa-fc35-4732-b5ec-a15d794267ec','6b9c3987-a344-4baf-8d11-077d719688ba'),('df668e22-e344-4c89-a050-e5ad211cbaa6','5429dc8c-799d-4555-98c6-f2d714a9fe50'),('dfc6b9a5-6673-4f1b-83cd-0dfa800c0d08','4e320c4e-deb6-4ccb-b45e-b77a5df3ff40'),('dfed3ea3-c133-47e8-8cfa-312eecbcc56d','4a0a3fa7-21a0-411a-bb0a-9b4eed1901ef'),('f33e2624-520b-4bc2-b6a0-190ee1d41855','49fcaedc-481a-4e05-934f-4867988c8ec5');
/*!40000 ALTER TABLE `employee_todo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(128) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES ('421a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','AllDepartments','This All Departments is for all departments in the company'),('421a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','Marketing','Sales Department'),('421a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','Accounting','Accounting Department'),('421a55f4-7d82-47d9-b54c-a76916479548','2017-03-25 19:42:40','2017-03-25 19:42:40','Warehouse','Warehouse for orders and shippers'),('421a55f4-7d82-47d9-b54c-a76916479549','2017-03-25 19:42:40','2017-03-25 19:42:40','Human Resource','Please send your resume to here'),('421a55f4-7d82-47d9-b54c-a76916479550','2017-03-25 19:42:40','2017-03-25 19:42:40','IT Department','flavor working place');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128) NOT NULL,
  `last_name` varchar(128) NOT NULL,
  `department_id` varchar(60) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` VALUES ('00a11245-12fa-436e-9ccc-967417f8c30a','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail6@gmail.com','pwd6','Todd','Seanez','421a55f4-7d82-47d9-b54c-a76916479545','Todd Seanez work for All Departments'),('00e93fc3-53ff-4da4-8e72-faa5216f81bb','2017-03-25 02:17:06','2017-03-25 02:17:06','demo@example.com','demo','Richard','Steere','421a55f4-7d82-47d9-b54c-a76916479545','Richard Steere works for All Departments'),('150e591e-486b-48ee-be42-4aecba665020','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail23@gmail.com','pwd23','Cecilia','Boes','421a55f4-7d82-47d9-b54c-a76916479546','Cecilia Boes is Manager of Marketing Department'),('30a890e4-a62c-44f9-abc0-07e2c74021da','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail2@gmail.com','pwd2','David','Meador','421a55f4-7d82-47d9-b54c-a76916479547','David Meador is Manager of Accounting Department'),('32c11d3d-99a1-4406-ab41-7b6ccb7dd760','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail18@gmail.com','pwd18','Susan','Finney','421a55f4-7d82-47d9-b54c-a76916479548','Susan Finney is Warehouse Manager'),('3ea61b06-e22a-459b-bb96-d900fb8f843a','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail8@gmail.com','pwd8','Melissa','Ward','421a55f4-7d82-47d9-b54c-a76916479549','Melissa Ward is Manager of Human Resource'),('3fda0d5c-fea4-4920-bc91-6e6c6663d161','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail12@gmail.com','pwd12','Robert','Graham','421a55f4-7d82-47d9-b54c-a76916479550','Robert Graham is manager of Information Technology Department');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(128) NOT NULL,
  `first_name` varchar(128) NOT NULL,
  `last_name` varchar(128) NOT NULL,
  `department_id` varchar(60) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;

INSERT INTO `employees` VALUES ('426624f6-84a9-4ec4-84f3-7655dc70e86e','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail19@gmail.com','Gail','Mccarthy','421a55f4-7d82-47d9-b54c-a76916479546','Education includes a BA in psychology from Colorado State University. Gail Mccarthy also completed (The Art of the Cold Call).'),('5e181cc6-cac7-49e9-a7a1-3095b0f9010b','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail21@gmail.com','Rebecca','Stapleton','421a55f4-7d82-47d9-b54c-a76916479546','Rebecca Stapleton is a member of Toastmasters International. He received his BTS commercial and a Ph.D. in international marketing from the University of Dallas.'),('61302be9-4b31-4be0-92fc-d0dda253e167','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail13@gmail.com','Virginia','Lewis','421a55f4-7d82-47d9-b54c-a76916479546','Virginia Lewis is fluent in French and Italian and reads German. He joined the company as a sales representative'),('70b18dcc-08ef-4040-91cf-4075973d320a','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail9@gmail.com','Duane','Smiley','421a55f4-7d82-47d9-b54c-a76916479546','Duane Smiley has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. She was hired as a sales associate and was promoted to sales representative.'),('7231eaa1-400f-4cb5-a867-f5eba8adbb81','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail11@gmail.com','Betty','Hicks','421a55f4-7d82-47d9-b54c-a76916479546','Betty Hicks holds a BA in English literature from Concordia College and an MA from the American Institute of Culinary Arts. She was temporarily assigned to the London office'),('f9b11370-f316-492c-92da-014d7bce7213','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail29@gmail.com','Dawn','Kitchen','421a55f4-7d82-47d9-b54c-a76916479546','Dawn Kitchen has also taken the courses Multi-Cultural Selling and Time Management for the Sales Professional. He is fluent in Japanese and can read and write French'),('fa44780d-ac48-41ab-9dd0-ac54a15755cf','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail20@gmail.com','Leon','Sarro','421a55f4-7d82-47d9-b54c-a76916479546','Leon Sarro has degree in English at the University of Michigan and then joining the company.'),('7771bbe9-92ab-46d1-a636-864526361d7d','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail16@gmail.com','Lynn','Melton','421a55f4-7d82-47d9-b54c-a76916479547','Lynn Melton graduated from St. Andrews University, Scotland, with a BSC degree.'),('8394fd35-8a8a-479f-a398-48f53b4a6554','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail3@gmail.com','Emily','Dancy','421a55f4-7d82-47d9-b54c-a76916479547','Emily Dancy is a graduate of Sussex University (MA, economics) and the University of California at Los Angeles'),('85651506-c13c-4c2f-9c79-8fbebc048e39','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail15@gmail.com','Fredrick','Morasca','421a55f4-7d82-47d9-b54c-a76916479547','Fredrick Morasca is fluent in Japanese and can read and write French, Portuguese, and Spanish.'),('887dcd8d-d5ee-48de-9626-73ff4ea732fa','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail27@gmail.com','Walter','Olsen','421a55f4-7d82-47d9-b54c-a76916479548','Walter Olsen served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan and then joining the company.'),('91e27a07-1f47-43c9-b851-60c6882abcd3','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail5@gmail.com','Olivia','Hampton','421a55f4-7d82-47d9-b54c-a76916479548','Olivia Hampton received a BA in psychology from the University of Washington.'),('9e7b2291-3bff-43b9-9241-8ff685e7a6dd','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail24@gmail.com','Carol','Hass','421a55f4-7d82-47d9-b54c-a76916479548','Carol Hass completed a course in business French. He reads and writes French.'),('9eec6c06-5918-4867-833a-face490d4715','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail1@gmail.com','Jacqueline','Watkins','421a55f4-7d82-47d9-b54c-a76916479548','Jacqueline Watkins is fluent in Japanese and can read and write French, Portuguese, and Spanish.'),('aa92d1ff-f0ad-4ba3-9c20-2afef207bf70','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail10@gmail.com','John','Hooten','421a55f4-7d82-47d9-b54c-a76916479549','John Hooten completing his degree in English at the University of Michigan and then joining the company.'),('b6160096-c503-4909-a674-7bfbddc8cc45','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail25@gmail.com','Melida','Wright','421a55f4-7d82-47d9-b54c-a76916479549','Melida Wright received a BA in psychology from the University of Washington. She has also completed a course in business French.'),('c81d66a3-f0fe-44e9-9f31-cb3c6f27db4e','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail22@gmail.com','Gina','Jauregui','421a55f4-7d82-47d9-b54c-a76916479549','Gina has completed the courses Successful Telemarketing and International Sales Management.'),('cf1780e6-d294-4113-8749-1c728b9e3f81','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail4@gmail.com','Hazel','Kyung','421a55f4-7d82-47d9-b54c-a76916479549','Hazel Kyung is graduate of Sussex University (MA, economics) and the University of California at Los Angeles'),('d622edfa-fc35-4732-b5ec-a15d794267ec','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail7@gmail.com','Roy','Grant','421a55f4-7d82-47d9-b54c-a76916479549','Roy Grant spent 6 months in an orientation program at the Seattle office.'),('df668e22-e344-4c89-a050-e5ad211cbaa6','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail14@gmail.com','Leo','Minnick','421a55f4-7d82-47d9-b54c-a76916479550','Leo Minnick has worked on DevOps for 5 years'),('dfc6b9a5-6673-4f1b-83cd-0dfa800c0d08','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail26@gmail.com','James','Diaz','421a55f4-7d82-47d9-b54c-a76916479550','James Diaz has a EE degree in University of Southern California'),('dfed3ea3-c133-47e8-8cfa-312eecbcc56d','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail0@gmail.com','Georgia','Boshard','421a55f4-7d82-47d9-b54c-a76916479550','Georgia Boshard is website designer, frontend Engineer'),('f33e2624-520b-4bc2-b6a0-190ee1d41855','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail17@gmail.com','Tracy','Tillman','421a55f4-7d82-47d9-b54c-a76916479550','Tracy Tillman is a software enginerr, she is senior python programmer.');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-25 19:42:51

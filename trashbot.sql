-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: trashbot
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Job`
--

DROP TABLE IF EXISTS `Job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Job` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_status` varchar(12) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1779 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Job`
--

LOCK TABLES `Job` WRITE;
/*!40000 ALTER TABLE `Job` DISABLE KEYS */;
INSERT INTO `Job` VALUES (1,'complete','2024-11-03 07:22:22'),(1775,'complete','2024-11-23 12:55:37'),(1776,'complete','2024-11-23 12:55:38'),(1777,'inprogress','2024-11-23 12:56:46'),(1778,'inprogress','2024-11-23 12:57:04');
/*!40000 ALTER TABLE `Job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `JobErrorLog`
--

DROP TABLE IF EXISTS `JobErrorLog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `JobErrorLog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `robot_id` int DEFAULT NULL,
  `aruco_id` int DEFAULT NULL,
  `job_id` int DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `Error_type` varchar(12) DEFAULT NULL,
  `image_path` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `job_id` (`job_id`),
  KEY `robot_id` (`robot_id`),
  CONSTRAINT `JobErrorLog_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `Job` (`id`),
  CONSTRAINT `JobErrorLog_ibfk_2` FOREIGN KEY (`robot_id`) REFERENCES `Robot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `JobErrorLog`
--

LOCK TABLES `JobErrorLog` WRITE;
/*!40000 ALTER TABLE `JobErrorLog` DISABLE KEYS */;
INSERT INTO `JobErrorLog` VALUES (1,1,1,1,'2024-11-03 07:47:37','aruco_error','./test_image/Screenshot from 2024-11-03 16-10-26.png');
/*!40000 ALTER TABLE `JobErrorLog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `JobLog`
--

DROP TABLE IF EXISTS `JobLog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `JobLog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `robot_id` int DEFAULT NULL,
  `navigation_point_id` int DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `job_status` varchar(12) DEFAULT NULL,
  `job_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_joblog_job` (`job_id`),
  KEY `fk_joblog_robot` (`robot_id`),
  KEY `fk_joblog_user` (`user_id`),
  KEY `fk_joblog_navigation` (`navigation_point_id`),
  CONSTRAINT `fk_joblog_job` FOREIGN KEY (`job_id`) REFERENCES `Job` (`id`),
  CONSTRAINT `fk_joblog_navigation` FOREIGN KEY (`navigation_point_id`) REFERENCES `NavigationPoint` (`id`),
  CONSTRAINT `fk_joblog_robot` FOREIGN KEY (`robot_id`) REFERENCES `Robot` (`id`),
  CONSTRAINT `fk_joblog_user` FOREIGN KEY (`user_id`) REFERENCES `RobotUser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6622 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `JobLog`
--

LOCK TABLES `JobLog` WRITE;
/*!40000 ALTER TABLE `JobLog` DISABLE KEYS */;
INSERT INTO `JobLog` VALUES (6608,1,NULL,5,'2024-11-23 12:55:37','pending',1775),(6609,1,0,5,'2024-11-23 12:55:37','allocated',1775),(6610,1,0,5,'2024-11-23 12:55:37','inprogress',1775),(6611,1,NULL,1,'2024-11-23 12:55:38','pending',1776),(6612,1,1,1,'2024-11-23 12:55:38','allocated',1776),(6613,1,1,1,'2024-11-23 12:55:38','inprogress',1776),(6614,1,1,1,'2024-11-23 12:56:46','complete',1776),(6615,1,1,8,'2024-11-23 12:56:46','pending',1777),(6616,1,1,8,'2024-11-23 12:56:46','allocated',1777),(6617,1,1,8,'2024-11-23 12:56:49','inprogress',1777),(6618,1,0,5,'2024-11-23 12:57:04','complete',1775),(6619,1,0,9,'2024-11-23 12:57:04','pending',1778),(6620,1,0,9,'2024-11-23 12:57:04','allocated',1778),(6621,1,0,9,'2024-11-23 12:57:07','inprogress',1778);
/*!40000 ALTER TABLE `JobLog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NavigationPoint`
--

DROP TABLE IF EXISTS `NavigationPoint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NavigationPoint` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(13) DEFAULT NULL,
  `x_coord` decimal(10,6) DEFAULT NULL,
  `y_coord` decimal(10,6) DEFAULT NULL,
  `z_orien` decimal(10,6) DEFAULT NULL,
  `w_orien` decimal(10,6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NavigationPoint`
--

LOCK TABLES `NavigationPoint` WRITE;
/*!40000 ALTER TABLE `NavigationPoint` DISABLE KEYS */;
INSERT INTO `NavigationPoint` VALUES (1,'basket_1',1.290028,-0.003381,-0.055201,0.999111),(2,'basket_2',0.840462,-0.739715,-0.727163,0.686464),(3,'basket_3',0.779708,-1.262948,0.667785,0.744354),(4,'basket_4',0.248580,-2.396516,0.997498,0.070690),(5,'basket_5',1.251284,-3.195752,-0.694113,0.719866),(6,'basket_6',1.417877,-2.101801,0.044670,0.999002),(7,'init_pos',-0.002500,-0.434729,-0.030959,0.999521),(8,'trash_room_1',-0.167296,-1.126767,0.090697,0.995879),(9,'trash_room_2',-0.112112,-0.692158,0.078968,0.996877),(10,'charging_1',-0.186793,-0.359778,0.088418,0.996083),(11,'charging_2',-0.132544,0.090852,0.051749,0.998660);
/*!40000 ALTER TABLE `NavigationPoint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Robot`
--

DROP TABLE IF EXISTS `Robot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Robot` (
  `id` int NOT NULL,
  `name` varchar(8) DEFAULT NULL,
  `current_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Robot`
--

LOCK TABLES `Robot` WRITE;
/*!40000 ALTER TABLE `Robot` DISABLE KEYS */;
INSERT INTO `Robot` VALUES (0,'robot_1','normal'),(1,'robot_2','normal');
/*!40000 ALTER TABLE `Robot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RobotStatusLog`
--

DROP TABLE IF EXISTS `RobotStatusLog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RobotStatusLog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `robot_id` int DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `robot_status` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `job_id` (`job_id`),
  KEY `robot_id` (`robot_id`),
  CONSTRAINT `RobotStatusLog_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `Job` (`id`),
  CONSTRAINT `RobotStatusLog_ibfk_2` FOREIGN KEY (`robot_id`) REFERENCES `Robot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RobotStatusLog`
--

LOCK TABLES `RobotStatusLog` WRITE;
/*!40000 ALTER TABLE `RobotStatusLog` DISABLE KEYS */;
INSERT INTO `RobotStatusLog` VALUES (1,1,1,'2024-11-03 07:40:58','normal');
/*!40000 ALTER TABLE `RobotStatusLog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RobotUser`
--

DROP TABLE IF EXISTS `RobotUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RobotUser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_number` varchar(20) NOT NULL,
  `role` varchar(20) NOT NULL,
  `password_hash` char(64) NOT NULL,
  `password_salt` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_number` (`employee_number`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RobotUser`
--

LOCK TABLES `RobotUser` WRITE;
/*!40000 ALTER TABLE `RobotUser` DISABLE KEYS */;
INSERT INTO `RobotUser` VALUES (1,'test','admin','48f4e93b094344c07e8ec78e2378adbed97998bfd6f773689b7b7d3febfb946d','d9509c8fc287c56553c95e8c5a45d11c'),(6,'1234','user','235d264814d5ada0137efc8470a83f63c6056fe006302341b941d0bc7a64cbe5','66946c007c97511caf055f484c09540a');
/*!40000 ALTER TABLE `RobotUser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Userbasket`
--

DROP TABLE IF EXISTS `Userbasket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Userbasket` (
  `user_id` int NOT NULL,
  `navigation_point_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`navigation_point_id`),
  KEY `navigation_point_id` (`navigation_point_id`),
  CONSTRAINT `Userbasket_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `RobotUser` (`id`),
  CONSTRAINT `Userbasket_ibfk_2` FOREIGN KEY (`navigation_point_id`) REFERENCES `NavigationPoint` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Userbasket`
--

LOCK TABLES `Userbasket` WRITE;
/*!40000 ALTER TABLE `Userbasket` DISABLE KEYS */;
INSERT INTO `Userbasket` VALUES (1,1),(6,1),(1,2),(1,3),(1,4),(1,5),(1,6);
/*!40000 ALTER TABLE `Userbasket` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-25  9:46:28

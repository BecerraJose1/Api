CREATE DATABASE  IF NOT EXISTS `api` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `api`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: api
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `file1`
--

DROP TABLE IF EXISTS `file1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `file1` (
  `idFile1` int NOT NULL AUTO_INCREMENT,
  `id_comprobante` int NOT NULL,
  `fecha_documento` date NOT NULL,
  `documento` varchar(15) NOT NULL,
  `id_cuenta` int NOT NULL,
  `id_cedula` int DEFAULT NULL,
  `id_c_costos` int DEFAULT NULL,
  `factura` varchar(15) DEFAULT NULL,
  `valor` int NOT NULL,
  `tipo` int NOT NULL,
  `concepto` longtext NOT NULL,
  `fecha_insert` datetime NOT NULL,
  `fecha_update` datetime DEFAULT NULL,
  PRIMARY KEY (`idFile1`),
  UNIQUE KEY `idFile1_UNIQUE` (`idFile1`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file1`
--

LOCK TABLES `file1` WRITE;
/*!40000 ALTER TABLE `file1` DISABLE KEYS */;
INSERT INTO `file1` VALUES (2,123,'2023-11-02','456789',789,101112,131415,'F12345',1000,1,'Compra de suministros','2023-11-02 15:45:00','2023-11-02 16:30:00');
/*!40000 ALTER TABLE `file1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-08 20:53:17

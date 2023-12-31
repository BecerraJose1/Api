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
-- Table structure for table `file3`
--

DROP TABLE IF EXISTS `file3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `file3` (
  `idfile3` int NOT NULL AUTO_INCREMENT,
  `cedula` double NOT NULL,
  `nombre1` varchar(100) NOT NULL,
  `nombre2` varchar(45) DEFAULT NULL,
  `apellido1` varchar(40) NOT NULL,
  `apellido2` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `id_ciudad` int DEFAULT NULL,
  `tipo_cedula` int DEFAULT NULL,
  PRIMARY KEY (`idfile3`),
  UNIQUE KEY `idfile3_UNIQUE` (`idfile3`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb3 COMMENT='cedula nit';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file3`
--

LOCK TABLES `file3` WRITE;
/*!40000 ALTER TABLE `file3` DISABLE KEYS */;
INSERT INTO `file3` VALUES (1,1017138782,'LUISA',NULL,'HINCAPIE','','CL 54 36A 54','3204650540','',NULL,13),(2,111213,'prueba',NULL,'','','prueba','','prueba@gmail.com',NULL,11),(3,11214,'PRUEBA PRUEBA',NULL,'PENDIENTE','','','','MEMO@HOTMAIL.COM',NULL,31),(4,1152206971,'ALEJANDRO',NULL,'ROJAS','ZAPATA','','3003144461','',NULL,13),(5,11789327,'CARLOS',NULL,'PALOMEQUE','','CL 54 36A 54','3103904827','',NULL,13),(6,15428685,'JUAN GUILLERMO CADAVID ARANGO',NULL,'','','CL 79 B SUR 54 55','2222','secontabilidad@gmail.com',NULL,31),(7,21332942,'FANY',NULL,'AGUIRRE','RODRIGUEZ','CL 54 36A 54','3108452507','',NULL,13),(8,21368953,'MARIA IDALY',NULL,'GIL','','CL 54 36A 54','3148816004','',NULL,13),(9,21386040,'MARTHA LUCIA',NULL,'LOPERA','','CL 54 36A 54','3042866780','',NULL,13),(10,21407034,'LUZ DARY',NULL,'MEJIA','','','3006535158','',NULL,13),(11,21776552,'GABRIELA',NULL,'QUINTERO','','CL 54 36A 54','3113209365','',NULL,13),(12,22114813,'LIGIA',NULL,'ARBELAEZ','','CL 54 36A 54','3006200491','',NULL,13),(13,22174032,'MARTHA',NULL,'RESTREPO','','CL 54 36A 54','3132356777','',NULL,13),(14,222222000000,'Consumidor Final',NULL,'','','Empresa','','ventasMostrardor@email.com',NULL,13),(15,2903889,'JAIME',NULL,'CELIS','','CL 54 36A 54','3146020150','',NULL,13),(16,32103053,'TERESITA',NULL,'MUÑOZ','ARANGO','CL 54 36A 54','3122395368','',NULL,13),(17,32205661,'MARTHA CECILIA',NULL,'VARGAS','','CL 54 36A 54','3014629403','',NULL,13),(18,32434608,'CELINA',NULL,'QUINTERO','','','3154801370','',NULL,13),(19,32465321,'LEONILA LOPEZ',NULL,'GALLEGO','','CL 54 36A 54','','',NULL,13),(20,32516067,'LUZ AMERICANA',NULL,'FERNANDEZ','','CL 54 36A 54','3155132185','',NULL,13),(21,32525711,'MARTHA',NULL,'OCHOA','','CL 54 36A 54','3147767425','ALEJACG2728@GMAIL.COM',NULL,13),(22,32542602,'MARTHA ELENA',NULL,'MEDINA','','CL 54 36A 54','3173458774','',NULL,13),(23,3303754,'JOSE',NULL,'OLMEDO','RAMIREZ','CL 54 36A 54','3003662420','',NULL,13),(24,3352828,'RODRIGO',NULL,'GIRALDO','','','','',NULL,13),(25,39176421,'SANDRA MILENA',NULL,'RIVERA','','CL 54 36A 54','3178650396','',NULL,13),(26,42994967,'GLORIA VIRGINIA',NULL,'LOPEZ','OSPINA','CL 54 36A 54','3193750766','',NULL,13),(27,43023145,'LUCIA',NULL,'GAVIRIA','','CL 54 36A 54','3216381854','',NULL,13),(28,43050415,'MARIA TERESA',NULL,'RAMIREZ','','CL 54 36A 54','3016430001','',NULL,13),(29,43061008,'NORA ELENA',NULL,'PATIÑO','RESTREPO','CL 54 36A 54','3005034706','',NULL,13),(30,43077781,'LUZ BIBIANA',NULL,'SILVA','','CL 54 36A 54','3178440955','',NULL,13),(31,43083662,'DIANA PATRICIA',NULL,'MADRID','','CL 54 36A 54','3113248575','ADOLFOMC2745@GMAIL.COM',NULL,13),(32,43095495,'ZORAIDA MARIA',NULL,'DAVILA','','','3015733645','',NULL,13),(33,43097993,'GLADYS',NULL,'CARDONA','','','3127889354','',NULL,13),(34,43208100,'MARIA EUGENIA',NULL,'ARRUBLA','','','3007846066','',NULL,13),(35,43300048,'GLORIA',NULL,'PALACIO','','CL 54 36A 54','3136369759','',NULL,13),(36,43514205,'INES',NULL,'MEJIA','OCHOA','CL 54 36A 54','3128970163','PENDIENTE@GMAIL.COM',NULL,13),(37,43546249,'BEATRIZ',NULL,'RIOS','','','3013773342','',NULL,13),(38,43546435,'GLADYS RAMIREZ',NULL,'','','CL 54 36A 54','3206323812','',NULL,13),(39,43817031,'YAZMIN',NULL,'CASTRILLON','','CL 54 36A 54','3173724804','',NULL,13),(40,43897360,'ALEJANDRA',NULL,'CADAVID','GAVIRIA','CR 65 89 01 APTO 7/','321854125','ALEJA@GMAIL.COM',NULL,13),(41,43970206,'NATALIA',NULL,'LOPEZ','','CL 54 36A 54','3013682427','',NULL,13),(42,43972193,'ISABEL',NULL,'CASTAÑO','','CL 54 36A 54','3128551280','',NULL,13),(43,43984823,'MARICEL CRISTINA',NULL,'RAMIREZ','','CL 54 36A 54','3183515692','',NULL,13),(44,524111,'JORGE IVAN',NULL,'MADRID','','CL 54 36A 54','','JORGEIMADRID2745@GMAIL.COM',NULL,13),(45,70033968,'GUSTAVO',NULL,'VELASQUEZ','MADRID','EDIFICIO','3137519944','JUANGUILLERMOMACP@GMAIL.COM',NULL,13),(46,70091911,'CARLOS ARTURO',NULL,'ESCOBAR','','','3012012685','',NULL,13),(47,70098699,'JORGE ALBERTO',NULL,'HOYOS','','CL 54 36A 54','3012012216','',NULL,13),(48,70099184,'JAVIER',NULL,'TANGARIFE','','CL 54 36A 54','3104266899','',NULL,13),(49,70108553,'OMAR',NULL,'OCAMPO','','CL 54 36A 54','3108440384','',NULL,13),(50,70564832,'SERGIO',NULL,'ESCUDERO','','','3003178526','',NULL,13),(51,70782485,'HECTOR',NULL,'VILLEGAS','','CL 54 36A 54','3006562996','',NULL,13),(52,71597171,'CARLOS',NULL,'CARDONA','','CL 54 36A 54','3007839195','',NULL,13),(53,71720242,'DAVID A',NULL,'OCHO','ZAPATA','','','',NULL,13),(54,72592910,'ADOLFO ALFREDO',NULL,'MADRID','CARDENAS','CL 54 36A 54 (405)','','ADOLFOMC2745@GMAIL.COM',NULL,13),(55,800088702,'EPS SURA',NULL,'','','MEDELLIN','','',NULL,31),(56,800130907,'SALUD TOTAL S.A.',NULL,'','','MEDELLIN','','',NULL,31),(57,800140949,'EPS CAFESALUD',NULL,'','','MEDELLIN','','',NULL,31),(58,800148514,'OLD MUTUAL',NULL,'','','CR 74 24 89','','',NULL,31),(59,800149496,'COLFONDOS',NULL,'','','MEDELLIN','','',NULL,31),(60,800170043,'PORVENIR S.A. CESANTIAS',NULL,'','','CR 74 24 89','','',NULL,31),(61,800170494,'FONDO DE CESANTIAS PROTECCION',NULL,'','','MEDELLIN','','',NULL,31),(62,800224808,'PORVENIR',NULL,'','','MEDELLIN','','',NULL,31),(63,800227940,'COLFONDOS',NULL,'','','MEDELLIN','','',NULL,31),(64,800229739,'PROTECCION',NULL,'','','MEDELLIN','','',NULL,31),(65,800231967,'HORIZONTE',NULL,'','','MEDELLIN','','',NULL,31),(66,800250119,'SALUCOOP',NULL,'','','MEDELLIN','','',NULL,31),(67,800251440,'EPS SANITAS S.A.',NULL,'','','MEDELLIN','','',NULL,31),(68,80150812,'DARWIN',NULL,'CARDONA','RAMIREZ','CL 54 36A 54','3202365040','',NULL,13),(69,804001273,'SOLSALUD E.P.S S.A',NULL,'','','Carrera 26 No. 30 - 70','','',NULL,31),(70,805000427,'COOMEVA',NULL,'','','MEDELLIN','','',NULL,31),(71,805001157,'S.O.S EPS',NULL,'','','MEDELLIN','','',NULL,31),(72,811044627,'SANTA MARIA DEL MAR',NULL,'','','CL 54 36A 54','3508973619','ADOLFOMC2745@GMAIL.COM',NULL,31),(73,82383148,'HERNAN',NULL,'RENTERIA','','CL 54 36A 54','3117426063','',NULL,13),(74,830009783,'CRUZ BLANCA',NULL,'','','MEDELLIN','','',NULL,31),(75,830074184,'SALUDVIDA SA ENTIDAD PROMOTORA DE SALUD',NULL,'','','CRA 2 N 22 - 24','','',NULL,31),(76,830118831,'ALIANSALUD ENTIDAD PROMOTORA DE SAL',NULL,'','','MEDELLIN','','',NULL,31),(77,8400551,'FRANCISCO JAVIER',NULL,'PALACIO','','CL 54 36A 54','3137655033','',NULL,13),(78,860002183,'SEGUROS DE VIDA COLPATRIA S.A',NULL,'','','Cra. 15 No 104 - 33 Piso 4','','',NULL,31),(79,860002184,'AXA COLPATRIA ARL',NULL,'','','CR 74 24 89','','',NULL,31),(80,860002400,'SEGUROS LA PREVISORA S.A.',NULL,'','','CL 57 9 07','300 5967976','contactenos@previsora.gov.co',NULL,31),(81,860011153,'ARP POSITIVA COMPAÑIA DE SEGUROS',NULL,'','','MEDELLIN','','',NULL,31),(82,860013816,'INSTITUTO DE SEGUROS SOCIALES I.S.S',NULL,'','','MEDELLIN','','',NULL,31),(83,890900841,'CAJA DE COMPENSACION FAMILIAR COMFAMA',NULL,'','','CR 45 # 49A - 16','','',NULL,31),(84,890900842,'PROGRAMA COMFENALCO ANTIOQUIA',NULL,'','','Carrera 50 # 53 - 43','','',NULL,31),(85,890903790,'ARL SURA',NULL,'','','Cl 49A 63-55','','',NULL,31),(86,890909246,'COOPERATIVA DE AHORRO Y CREDITO COBELEN',NULL,'','','Calle 30A 77 60','3205535878','servicioalasociado@cobelen.com',NULL,31),(87,899999284,'FONDO NACIONAL DE AHORRO',NULL,'','','MEDELLIN','','',NULL,31),(88,900156264,'NUEVA EPS S.A',NULL,'','','MEDELLIN','','',NULL,31),(89,900226715,'COOPERATIVA DE SALUD Y DESARROLLO INTEGRAL COOSALUD',NULL,'','','CRA 70 N 40B 32','','',NULL,31),(90,900336004,'COLPENSIONES',NULL,'','','MEDELLIN','','',NULL,31),(91,900336004,'COLPENSIONES',NULL,'','','CR 74 24 89','','',NULL,31),(92,900604350,'SAVIA SALUD EPS',NULL,'','','CRA. 53 A 42-101','','',NULL,31),(93,98567695,'CARLOS MARIO',NULL,'PATIÑO','RAMIREZ A602,P24','CL 54 36A 54','','',NULL,13),(94,9856769500,'CARLOS MARIO',NULL,'PATIÑO','A203,P4,,U1','CL23335','3005034706','',NULL,13),(95,9856769598,'CARLOS MARIO',NULL,'PATIÑO','P34,U25','CCCC','','',NULL,13),(96,9856769599,'CARLOS MARIO',NULL,'PATIÑO','RAMIREZ P35','CL','','',NULL,13),(97,98567699598,'CARLOS MARIO',NULL,'PATIÑO','RESTREPO P34,U25','EDIFICIO','','PENDIENTE@GMAIL.COM',NULL,13);
/*!40000 ALTER TABLE `file3` ENABLE KEYS */;
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

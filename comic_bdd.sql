CREATE DATABASE  IF NOT EXISTS `quadrinhos_sql` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `quadrinhos_sql`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: quadrinhos_sql
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `comics`
--

DROP TABLE IF EXISTS `comics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comics` (
  `comicID` int unsigned NOT NULL AUTO_INCREMENT,
  `tituloComic` varchar(255) NOT NULL,
  `editoraID` int unsigned NOT NULL,
  `equipeID` int unsigned NOT NULL,
  `activeYears` varchar(20) NOT NULL,
  `issueTitle` varchar(255) NOT NULL,
  `publishDate` date NOT NULL,
  `issueDescription` text NOT NULL,
  `Format` varchar(20) NOT NULL,
  `Rating_Age` int NOT NULL,
  `Price` decimal(5,2) NOT NULL,
  PRIMARY KEY (`comicID`),
  KEY `editoraID` (`editoraID`),
  KEY `equipeID` (`equipeID`),
  CONSTRAINT `comics_ibfk_1` FOREIGN KEY (`editoraID`) REFERENCES `editora` (`editoraID`) ON UPDATE CASCADE,
  CONSTRAINT `comics_ibfk_2` FOREIGN KEY (`equipeID`) REFERENCES `equipe_producao` (`equipeID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15552 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comics`
--

LOCK TABLES `comics` WRITE;
/*!40000 ALTER TABLE `comics` DISABLE KEYS */;
INSERT INTO `comics` VALUES (1,'A Returner\'s Magic Should Be Special',6,15,'2017-2024','A Returner\'s Magic Should Be Special Cap 231','2017-05-20','Por 10 anos, o prodígio mágico Desir e sua equipe têm lutado dentro do misterioso Labirinto das Sombras—e contra o fim do mundo. Grande parte da humanidade já pereceu, e justo quando Desir está prestes a ser morto, ele é enviado de volta 13 anos no passado. Apesar de conhecer o futuro amaldiçoado que se desenha à frente, Desir fortalece sua determinação ao perceber uma oportunidade de treinar seus amigos e se preparar melhor para enfrentar o Armagedom juntos, sem perder aqueles que amam.','Webtoon',14,8.57),(2,'Thor (2007) ',3,8,'2009-2015','Thor (2007) #602','2014-01-23','Os eventos cataclísmicos e catastróficos de THOR #600 abalaram Asgard. O que os amigos e irmãos de Thor farão para ajudá-lo? E qual poderia ser o próximo passo nos esquemas e maquinações sinistras do tortuoso Loki?','Comic',14,1.64),(3,'ANT-MAN: LAST DAYS 1 (2015)',1,3,'2015','ANT-MAN: LAST DAYS 1 (2015) #1','2015-08-26','When a local clairvoyant predicts the end of the world, a mysterious woman sends Scott on a vital mission! An old foe (okay, maybe more like annoyance) shows up - and Scott\'s going to regret it! What do you do when you think the world is about to end? What do you think? Doesn\'t anybody else remember 1999? You party! Everything dies? Pfft. Everything DANCES.','Comic',13,3.99),(4,'Avengers and Power Pack Assemble! (2006)',3,4,'2006','Avengers and Power Pack Assemble! (2006) #2','2006-05-24','When one of billionaire Tony Stark\'s greatest inventions is stolen, it\'s up to the invincible Iron Man to track it down... unless, of course, Power Pack beats him to the punch! But is Jack Power really looking to save the day or is he just hoping for a hefty reward? 32 PGS./0 ...$2.99','Comic',0,0.00),(5,'Black Panther: The Most Dangerous Man Alive (2010 - 2012)',4,5,'2010 - 2012','Black Panther: The Most Dangerous Man Alive (2010) #529','2012-02-08','• Kingpin vs. T’Challa in this status-quo changing series finale! • Guest-starring: Lady Bullseye! Typhoid Mary! Falcon! Luke Cage!','Comic',13,2.99),(6,'Captain America Theater of War: Operation Zero-Point (2008)',1,6,'2008','Captain America Theater of War: Operation Zero-Point (2008) #1','2008-10-29','The first in a series of specials covering the length and breadth of the larger-than-life legend of Captain America, as told by the industry\'s leading experts in the field! First up, it\'s 1944, and wouldn\'t you know it? Them sneaky Nazis have managed to crack the secrets of electro-magnetic physics...yeah, that\'s right: apples may fall down in the free world, but schnitzels are falling up in the skies over a mysterious lab in a Polish forest, thanks to a little help from a nearby forced-labor camp. Sure, we could send in the Marines, but why bother when we\'ve got Captain America?! But even Cap may be meeting his match against the lab\'s sadistic cybernetic commandant. Because everyone knows, the only thing worse than a Nazi is a Robot Nazi! 13 ...$3.99','Comic',13,3.99),(7,'Exiles (2001 - 2008)',1,7,'2001 - 2008','Exiles (2001) #3','2001-10-10','To ensure the stability of the time stream and the integrity of their home dimensions, The Exiles must ensure Jean Grey dies!','Comic',0,0.00),(8,'Foolkiller (2007 - 2008)',2,8,'2007 - 2008','Foolkiller (2007) #1','2007-10-24','Los Angeles Times best-selling author Gregg Hurwitz (The Crime Writer) and Lan Medina (Punisher) bring you a gritty, no-holds-barred crime thriller! Move over Frank Castle, there\'s a new vigilante in town. When the Foolkiller strikes, the punishment fits the crime. It\'s a grand display for all to see, the truth in all its brutal glory, our hidden secrets gutted and turned inside out for the front pages. A vigilante artist, a madman performer, the Foolkiller has been brutally introduced to the human joke, and he wants to make sure fools everywhere take note. What he reveals may not be what you want to see. Or what you want to admit. But he makes one thing certain: If you\'re a fool, you cannot hide. 32 PGS./Cardstock Cover/17 ...$3.99','Comic',17,3.99),(9,'Daredevil: Born Again (1986)',1,9,'1986','Daredevil: Born Again (1986) #227','1986-02-10','Daredevil faces his greatest challenge as Kingpin discovers his secret identity, leading to a series of events that will test the hero\'s resilience.','Comic',0,0.00),(10,'Fantastic Four (1961 - 1996)',2,10,'1961 - 1996','Fantastic Four (1961) #48','1966-03-10','The first appearance of the Silver Surfer and Galactus! The Fantastic Four must save Earth from the cosmic herald and the world-eater.','Comic',0,0.00),(11,'Ghost Rider (1973 - 1983)',1,11,'1973 - 1983','Ghost Rider (1973) #1','1973-09-01','Johnny Blaze makes a deal with the devil and transforms into the Ghost Rider, a supernatural entity with a flaming skull, seeking vengeance.','Comic',0,0.00),(12,'The Incredible Hulk (1962 - 1999)',2,12,'1962 - 1999','The Incredible Hulk (1962) #340','1988-02-10','Wolverine clashes with the Hulk in a battle of strength and ferocity, leading to unexpected consequences.','Comic',0,0.00),(13,'The Mighty Thor (1966 - 1996)',3,14,'1966 - 1996','The Mighty Thor (1966) #337','2024-01-22','The introduction of Beta Ray Bill, an alien warrior who proves worthy to wield Thor\'s enchanted hammer, Mjolnir.','Comic',0,6.48),(14,'Solo levelling',6,15,'2018-2021','Solo levelling 1º temporada','2024-01-22','Em um mundo onde caçadores – humanos que possuem habilidades mágicas – devem lutar contra monstros mortais para proteger a raça humana de certa aniquilação, um caçador notoriamente fraco chamado Sung Jinwoo se encontra em uma luta aparentemente interminável pela sobrevivência. Um dia, depois de sobreviver por pouco a uma masmorra dupla esmagadoramente poderosa que quase acaba com todo o seu grupo, um programa misterioso chamado Sistema o escolhe como seu único jogador e, por sua vez, dá a ele a habilidade extremamente rara de subir de nível em força, possivelmente além de qualquer limites conhecidos. Jinwoo então parte em uma jornada enquanto luta contra todos os tipos de inimigos, tanto homens quanto monstros, para descobrir os segredos das masmorras e a verdadeira fonte de seus poderes.','Webtoon',14,15.00),(15,'Dragon Ball',5,7,'2001-2024','Dragon Ball Vol. 8','2001-06-22','O exército Red Ribbon resolveu apelar para o temível Tao Paipai, o melhor matador do mundo! Agora, com a crueldade desse novo inimigo, Goku terá um bom motivo para reunir as sete Esferas do Dragão!','Mangá',12,26.18),(16,'A Saga Do Batman',5,9,'1986-2023','A Saga Do Batman Vol. 31','1986-03-13','E mais um arco escrito por Alan Grant, com arte de Tim Sale, surge um novo criminoso fantasiado em Gotham City, e ele já está sendo perseguido por alguém! Ao dar de cara com o Batman, Bruce Wayne se vê envolvido em uma trama repleta de vilões, com destaque para o terrível Mariposa Assassina, além das participações ativas do Homem-Gato e do Homem-Calendário! E mais: a origem secreta do Cara de Barro!','Comic',12,39.90),(17,'Guardians of the Galaxy',2,4,'2013-2015','Guardians of the Galaxy Vol. 1','2024-01-05','Há uma nova regra na galáxia: Ninguém toca na Terra! Mas por que a Terra de repente se tornou o planeta mais importante da galáxia? Isso é o que os Guardiões da Galáxia vão descobrir! Junte-se a Star-Lord, Gamora, Drax, Rocket Raccoon, Groot e - espere por isso - o Invencível Homem de Ferro enquanto embarcam em um dos capítulos mais explosivos e reveladores do Marvel NOW!','Comic',14,29.99);
/*!40000 ALTER TABLE `comics` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_comic_insert` BEFORE INSERT ON `comics` FOR EACH ROW BEGIN
    IF NEW.publishDate > NOW() THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A data de publicação não pode ser no futuro.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `editora`
--

DROP TABLE IF EXISTS `editora`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editora` (
  `editoraID` int unsigned NOT NULL AUTO_INCREMENT,
  `nomeEditora` varchar(50) NOT NULL,
  `paísEditora` varchar(45) NOT NULL,
  `anoCriacao` varchar(45) NOT NULL,
  PRIMARY KEY (`editoraID`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editora`
--

LOCK TABLES `editora` WRITE;
/*!40000 ALTER TABLE `editora` DISABLE KEYS */;
INSERT INTO `editora` VALUES (1,'Marvel Universe','EUA','1939'),(2,'MAX','EUA','2001'),(3,'Marvel Knights','EUA','1988'),(4,'Licensed Publishing','Canadá','1985'),(5,'Panini','Itália','1961'),(6,'D&C Media','Coreia do Sul','2012');
/*!40000 ALTER TABLE `editora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipe_producao`
--

DROP TABLE IF EXISTS `equipe_producao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipe_producao` (
  `equipeID` int unsigned NOT NULL AUTO_INCREMENT,
  `Writer` varchar(50) NOT NULL,
  `Penciler` varchar(45) NOT NULL,
  `coverArtist` varchar(45) NOT NULL,
  PRIMARY KEY (`equipeID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipe_producao`
--

LOCK TABLES `equipe_producao` WRITE;
/*!40000 ALTER TABLE `equipe_producao` DISABLE KEYS */;
INSERT INTO `equipe_producao` VALUES (1,'Tom Defalco, Ron Frenz','Ron Frenz','Ron Frenz'),(2,'Joe Kelly','Max Fiumara','Paolo Rivera'),(3,'Nick Spencer','Ramon Rosanas','Mark Brooks'),(4,'David Liss','Shawn Martinbrough','Francesco Francavilla'),(5,'Daniel Knauf','Mitch Breitweiser','Mitch Breitweiser'),(6,'Daniel Knauf','Mitch Breitweiser','Mitch Breitweiser'),(7,'Ed Brubaker','Sean Phillips','Sean Phillips'),(8,'Robin Furth, Peter David','Jonathan Marks','Nimit Malavia'),(9,'Robbie Thompson','Javier Rodriguez','Javier Rodriguez'),(10,'Judd Winick','Michael Mckone','Mike Mckone'),(11,'Nick Spencer','Roge Antonio','Mark Bagley'),(12,'Gregg Hurwitz','Lan Medina','Lan Medina'),(13,'Jeph Loeb','Tim Sale','Tim Sale'),(14,'Joe Casey','Eric Canete','Eric Canete'),(15,'Chugong','Jang Sung-Rak','Jang Sung-Rak');
/*!40000 ALTER TABLE `equipe_producao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-17  1:40:03

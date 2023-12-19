-- table parcours for test
USE datascientest;
DROP TABLE  IF EXISTS parcours;

CREATE TABLE parcours (
    id INTEGER NOT NULL, 
    name VARCHAR(255),
    PRIMARY KEY (id));
    
INSERT INTO parcours
VALUES
    (1,"AAA"),
    (2,"BBB");



-- context de examen
DROP TABLE  IF EXISTS Boissons;
CREATE TABLE Boissons
(
 BoissonId INTEGER NOT NULL,
 Nom VARCHAR(255),
 Contenance FLOAT,
 Prix FLOAT,
 PRIMARY KEY(BoissonId)
);

INSERT INTO Boissons
VALUES
    (1,"Coca",33,0.99),
    (2,"Perrier",100,2),
    (3,"Perrier",33,1),
    (4,"Vittel",150,1.5),
    (5,"Badoit",50,2);

DROP TABLE IF EXISTS Factures;
CREATE TABLE Factures
(
    FactureId INTEGER NOT NULL,
    BoissonId INTEGER,
    Heure FLOAT,
    PRIMARY KEY(FactureId)
);

INSERT INTO Factures
VALUES
    (1,1,7),
    (2,1,8),
    (3,4,12);



-- -- Creat envirement for part2 question 
DROP TABLE IF EXISTS people;
CREATE TABLE people 
(
  person_id VARCHAR(255),
  name VARCHAR(255),
  born INTEGER,
  died INTEGER,
  PRIMARY KEY (person_id)
);
-- SELECT VERSION();

DROP TABLE IF EXISTS titles;
CREATE TABLE titles (
  title_id VARCHAR(255) PRIMARY KEY,
  type VARCHAR(255),
  primary_title VARCHAR(255),
  original_title VARCHAR(255),
  is_adult INTEGER,
  premiered INTEGER,
  ended INTEGER,
  runtime_minutes INTEGER,
  genres VARCHAR(255)
);

DROP TABLE IF EXISTS crew;
CREATE TABLE crew (
  title_id VARCHAR(255), -- REFERENCES titles (title_id),
  person_id VARCHAR(255), -- REFERENCES people (person_id),
  category VARCHAR(255),
  job VARCHAR(255),
  characters VARCHAR(255)
);

DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings (
  title_id VARCHAR(255) PRIMARY KEY, -- REFERENCES titles (title_id),
  rating FLOAT,
  votes INTEGER
);

-- SET GLOBAL local_infile = true; -- use once for avoid error in using local infile

USE datascientest;
LOAD DATA LOCAL INFILE '/home/jayl/datascientestfile/sql/data/title.ratings.tsv' 
INTO TABLE ratings 
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(title_id, rating, votes);
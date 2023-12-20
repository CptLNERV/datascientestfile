-- table parcours for test
USE datascientest;
SET GLOBAL local_infile = true;


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
-- SELECT VERSION();




-- set titles table 
-- DROP TABLE IF EXISTS titles;
-- CREATE TABLE titles (
--   title_id VARCHAR(255) PRIMARY KEY,
--   type VARCHAR(255),
--   primary_title VARCHAR(255),
--   original_title VARCHAR(255),
--   is_adult INTEGER,
--   premiered INTEGER,
--   ended INTEGER,
--   runtime_minutes INTEGER,
--   genres VARCHAR(255)
-- );
-- SET GLOBAL local_infile = true; --
-- USE datascientest;
-- LOAD DATA LOCAL INFILE '/home/jayl/datascientestfile/sql/data/title.basics_1000.tsv' 
-- INTO TABLE titles 
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n' 
-- IGNORE 1 LINES
-- (title_id, type, primary_title,original_title,is_adult,premiered,ended,runtime_minutes,genres);





DROP TABLE IF EXISTS crew;
CREATE TABLE crew (
  title_id VARCHAR(255) PRIMARY KEY, -- REFERENCES titles (title_id),
  person_id VARCHAR(255), -- REFERENCES people (person_id),
  category VARCHAR(255),
  job VARCHAR(255),
  characters VARCHAR(255)
);
SET GLOBAL local_infile = true; --
USE datascientest;
LOAD DATA LOCAL INFILE '/home/jayl/datascientestfile/sql/data/title.principals_1000.tsv' 
INTO TABLE crew 
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(title_id,person_id,category,job,characters);


-- -- set ratings table ; excution once 
-- DROP TABLE IF EXISTS ratings;
-- CREATE TABLE ratings (
--   title_id VARCHAR(255) PRIMARY KEY, -- REFERENCES titles (title_id),
--   rating FLOAT,
--   votes INTEGER
-- );

-- SET GLOBAL local_infile = true; --
-- USE datascientest;
-- LOAD DATA LOCAL INFILE '/home/jayl/datascientestfile/sql/data/title.ratings_1000.tsv' 
-- INTO TABLE ratings 
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n' 
-- IGNORE 1 LINES
-- (title_id, rating, votes);


--  set people table 
-- USE datascientest;
-- DROP TABLE IF EXISTS people;
-- CREATE TABLE people (
--   person_id VARCHAR(255) PRIMARY KEY,   -- REFERENCES titles (person_id),
--   name VARCHAR(255), 
--   born INTEGER,
--   died INTEGER
-- );

-- LOAD DATA LOCAL INFILE '/home/jayl/datascientestfile/sql/data/name.basics_1000.tsv' 
-- INTO TABLE people 
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n' 
-- IGNORE 1 LINES
-- (person_id, name, born,died);



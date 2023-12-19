use datascientest;
-- select * from Boissons
-- select * from Factures

-- Question dans l'examen: Boissons n'ont pas vendus, use NOT IN
-- SELECT DISTINCT(Nom) 
-- FROM Boissons
-- WHERE Boissons.Nom NOT IN
--     /*avoir la list de nom vendu */
--     (
--     SELECT DISTINCT(b.Nom) 
--     FROM Boissons AS b
--     INNER Join Factures AS f
--     ON b.BoissonId = f.BoissonId
--     )



-- -- Question dans l'examen : Proportion de boissons vendus use GROUP BY
-- SELECT b.Nom,
-- ROUND(
--     COUNT(b.Nom) 
-- /(
--     SELECT COUNT(*)
--     FROM Factures
-- )*100
-- ,2) AS "Proportion(%)"

-- FROM Factures AS f
-- LEFT JOIN Boissons AS b
-- ON f.BoissonId = b.BoissonId
-- GROUP BY b.Nom


-- SELECT @@basedir;

select * from ratings
limit 10
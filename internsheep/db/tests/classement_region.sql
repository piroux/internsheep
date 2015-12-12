-- ================================================================
--                Supression des données
-- =================================================================

TRUNCATE propositions_stage CASCADE ;
TRUNCATE secteurs  CASCADE ; 
TRUNCATE contacts CASCADE ;
TRUNCATE entreprises  CASCADE ; 
TRUNCATE adresses  CASCADE ; 
TRUNCATE eleves CASCADE ;
TRUNCATE personnes CASCADE ;
TRUNCATE responsables_pedagogiques CASCADE ;
TRUNCATE appartient CASCADE ;
TRUNCATE consultations CASCADE ;
TRUNCATE affectations CASCADE ;

-- ================================================================
--                Creation desdonnees
-- =================================================================



--adresse
INSERT INTO adresses VALUES (  1 , 'TALENCE'     , 33400       , '30 avenue des facultés'  ) ;
INSERT INTO adresses VALUES (  2 , 'Bordeaux'     , 33000       , 'victoire'  ) ;
INSERT INTO adresses VALUES (  3 , 'Toulouse'     , 31000       , '30 avenue des facultés'  ) ;
INSERT INTO adresses VALUES (  4 , 'Corse'     , 92000       , '30 avenue des facultés'  ) ;
INSERT INTO adresses VALUES (  5 , 'TALENCE'     , 33400       , '30 avenue des facultés'  ) ;
BEGIN;

-- entreprise
INSERT INTO entreprises VALUES (  1 , 'ORANGE'     , 0123456789       , 'WWW.ORANGE.FR', 'SARL', 10000, 1  ) ;
INSERT INTO entreprises VALUES (  2 , 'BOUYGUES'     , 0123456789       , 'WWW.BOUYGUES.FR', 'SARL', 30000, 1  ) ;
INSERT INTO entreprises VALUES (  3 , 'FREE'     , 0123456789       , 'WWW.FREE.FR', 'SARL', 10000, 1  ) ;
INSERT INTO entreprises VALUES (  4 , 'NRJ'     , 0123456789       , 'WWW.NRJ.FR', 'SARL', 100, 1  ) ;

-- contact
INSERT INTO personnes VALUES (  6 , 'p6', 'p6','martin@gmail.fr', 061234239  ) ;
INSERT INTO contacts VALUES (  1 , 'DG', 6, 1 ) ;

INSERT INTO personnes VALUES (  9 , 'p6', 'p6','martin@gmail.fr', 061234239  ) ;
INSERT INTO contacts VALUES (  2 , 'DG', 9, 2 ) ;

INSERT INTO personnes VALUES (  10 , 'p6', 'p6','martin@gmail.fr', 061234239  ) ;
INSERT INTO contacts VALUES (  3 , 'DG', 10, 3 ) ;

INSERT INTO personnes VALUES (  11 , 'p6', 'p6','martin@gmail.fr', 061234239  ) ;
INSERT INTO contacts VALUES (  4 , 'DG', 11, 4 ) ;

INSERT INTO personnes VALUES (  12 , 'p6', 'p6','martin@gmail.fr', 061234239  ) ;
INSERT INTO contacts VALUES (  5 , 'DG', 12, 4 ) ;


-- proposition_id,sujet,annee,domaine,groupe ,date_debut ,date_fin,indemnit,contact_id, adresse_id

INSERT INTO propositions_stage VALUES ( 1, 'bsujet1', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,1, 1 ) ;
INSERT INTO propositions_stage VALUES ( 2, 'fsujet2', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,2, 2 ) ;
INSERT INTO propositions_stage VALUES ( 3, 'xsujet3', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,2, 3 ) ;
INSERT INTO propositions_stage VALUES ( 4, 'asujet4', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,4, 4 ) ;
INSERT INTO propositions_stage VALUES ( 5, 'asujet5', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,5, 5 ) ;





-- toutes les propositions en aquitaine par ordre alphabetique

SELECT proposition_id, sujet
FROM propositions_stage
INNER JOIN adresses
ON propositions_stage.adresse_id = adresses.adresse_id
INNER JOIN departements
ON departements.departement_id = trunc(CAST (adresses.code_postal as numeric) /1000)
INNER JOIN regions
ON regions.region_id = departements.region_id
WHERE regions.nom = 'Aquitaine'
ORDER BY propositions_stage.sujet ASC;

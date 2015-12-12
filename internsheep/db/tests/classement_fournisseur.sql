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
BEGIN;
-- eleves
INSERT INTO personnes VALUES (  1 , 'Martin', 'Martine','martine@yahoo.fr', 0612345678  ) ;
INSERT INTO eleves VALUES (  1 , 2, 'informatique', 1, 1 ) ;

INSERT INTO personnes VALUES (  2 , 'sebastien', 'lesage','sebastien@gmail.fr', 0641587963  ) ;
INSERT INTO eleves VALUES (  2 , 1, 'electronique', 1, 2 ) ;

INSERT INTO personnes VALUES (  3 , 'Eric', 'lepetit','eric@gmail.fr', 0641235896  ) ;
INSERT INTO eleves VALUES (  3 , 1, 'matmeca', 1, 3 ) ;

INSERT INTO personnes VALUES (  4 , 'Pivot', 'glissant','pivot@gmail.fr', 061258389  ) ;
INSERT INTO eleves VALUES (   4, 2, 'informatique', 1, 4 ) ;

INSERT INTO personnes VALUES (  5 , 'souf', 'legrand','souf@gmail.fr', 0612547859  ) ;
INSERT INTO eleves VALUES (  5 , 1, 'matmeca', 1, 5 ) ;

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


-- responsable pedagogique
INSERT INTO personnes VALUES (  7 , 'p7', 'Estelle','estelle@gmail.fr', 061254389  ) ;
INSERT INTO responsables_pedagogiques VALUES ( 7 ) ;

INSERT INTO personnes VALUES (  8 , 'p8', 'Estelle','estelle@gmail.fr', 061254389  ) ;
INSERT INTO responsables_pedagogiques VALUES ( 8 ) ;

-- proposition_id,sujet,annee,domaine,groupe ,date_debut ,date_fin,indemnit,contact_id, adresse_id

INSERT INTO propositions_stage VALUES ( 1, 'sujet1', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,1, 1 ) ;
INSERT INTO propositions_stage VALUES ( 2, 'sujet2', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,2, 1 ) ;
INSERT INTO propositions_stage VALUES ( 3, 'sujet3', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,2, 1 ) ;
INSERT INTO propositions_stage VALUES ( 4, 'sujet4', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,4, 1 ) ;
INSERT INTO propositions_stage VALUES ( 5, 'sujet5', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,5, 1 ) ;

-- probleme : un eleve peut avoir plusieurs propositions de stage
-- une proposition peut etre prise par plusieurs eleves
--	eleve_id,personne_id,	proposition_id

INSERT INTO affectations VALUES ( 1, 7, 1 ) ;
INSERT INTO affectations VALUES ( 2, 8, 2 ) ;
INSERT INTO affectations VALUES ( 3, 7, 3 ) ;
INSERT INTO affectations VALUES ( 4, 7, 4 ) ;
INSERT INTO affectations VALUES (5, 7, 5 ) ;

END;



-- classement des meilleurs fournisseurs de stages de l'enseirb

SELECT nom_entreprise , count(proposition_id)
FROM entreprises INNER JOIN contacts
ON entreprises.entreprise_id = contacts.entreprise_id
INNER JOIN propositions_stage
ON contacts.contact_id = propositions_stage.contact_id
GROUP BY entreprises.entreprise_id
ORDER BY count(proposition_id) DESC;

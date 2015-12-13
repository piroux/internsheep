-- ================================================================
--                Supression des données
-- =================================================================

TRUNCATE secteurs  CASCADE ;
TRUNCATE entreprises  CASCADE ;
TRUNCATE adresses  CASCADE ;
TRUNCATE eleves CASCADE ;
TRUNCATE personnes CASCADE ;
TRUNCATE contacts CASCADE ;
TRUNCATE responsables_pedagogiques CASCADE ;
TRUNCATE propositions_stage CASCADE ;
TRUNCATE appartient CASCADE ;
TRUNCATE consultations CASCADE ;
TRUNCATE affectations CASCADE ;

-- ============================================================
--    creation des donnees
-- ============================================================


-- secteurs
INSERT INTO secteurs(nom_secteur) VALUES ('banque'  ) ;
INSERT INTO secteurs(nom_secteur) VALUES ('transport aerien') ;
INSERT INTO secteurs(nom_secteur) VALUES ('economie') ;
INSERT INTO secteurs(nom_secteur) VALUES ('tourisme') ;
INSERT INTO secteurs(nom_secteur) VALUES ('transport ferroviaire');
INSERT INTO secteurs(nom_secteur) VALUES ('transport maritime');
INSERT INTO secteurs(nom_secteur) VALUES ('informatique');
INSERT INTO secteurs(nom_secteur) VALUES ('electronique');
INSERT INTO secteurs(nom_secteur) VALUES ('tourisme');




-- entreprises
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('TALENCE'     , 33400       , '30 avenue des facultes'  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('ORANGE'     , 0123456789       , 'http://WWW.ORANGE.FR', 'SARL', 10000, 1  ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LILLE'     , 59000    , '1, boulevard Vauban '  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('PINOTEAU'   , 0124569874, 'http://WWW.PINOTEAU.FR', 'SAS', 10, 2  ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('NANCY'     ,   54000 , ' 119 Avenue de Strasbourg'  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('DAVOY'      , 8109456987, 'http://WWW.DAVOY.FR', 'SA', 100, 3 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LYON'     ,   69100 , '45, avenue Albert Einstein  '  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('CAPGEMINI'      , 0234567891, 'http://WWW.CAPGEMINI.FR', 'SA', 200, 4 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('NICE'     ,   06000 , '35 Avenue Jean Médecin, '  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('ATOS'      , 0345678912, 'http://WWW.ATOS.FR', 'SA', 300, 5 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('PESSAC'     , 33600    , '20 avenue de bardanac'  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('SOPRA'      , 0567891234, 'http://WWW.SOPRA.FR', 'SA', 400, 6 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LYON'     ,   69100 , '45, avenue Albert Einstein  '  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('CGI'      , 0678912345, 'http://WWW.CGI.FR', 'SA', 500, 7 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('NICE'     ,   06000 , '35 Avenue Jean Médecin, '  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('THALES'      , 0789123456, 'http://WWW.THALES.FR', 'SA', 600, 8 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('PESSAC'     , 33600    , '20 avenue de bardanac'  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('COGNITEEV'      , 0891234567, 'http://WWW.COGNITEEV.FR', 'SA', 700, 9 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('PESSAC'     , 33600    , '20 avenue de bardanac'  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('SAFRAN'      , 0891534567, 'http://WWW.SAFRAN.FR', 'SA', 7000, 10 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('BORDEAUX'     , 33000       , '30 rue ste catherine'  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('SOLUCOM'      , 0891234537, 'http://WWW.SOLUCOM.FR', 'SA', 800, 11 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LYON'     ,   69100 , '45, avenue Albert Einstein  '  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('TOTAL'      , 0891234562, 'http://WWW.TOTAL.FR', 'SA', 4000, 12 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('BORDEAUX'     , 33000       , '30 rue ste catherine'  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('LECTRA'      , 0891234667, 'http://WWW.LECTRA.FR', 'SA', 6000, 13 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LYON'     ,   69100 , '45, avenue Albert Einstein  '  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('SMILE'      , 0899234567, 'http://WWW.SMILE.FR', 'SA', 8000, 14 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('MARSEILLE'     ,  13004  , '10, avenue Foch  '  ) ;
INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id) VALUES ('EUROLOGICIEL'      , 0891236567, 'http://WWW.EUROLOGICIEL.FR', 'SA', 7600, 15 ) ;

-- appartient
INSERT INTO appartient VALUES (  1 , 1 ) ;
INSERT INTO appartient VALUES (  2 , 1 ) ;
INSERT INTO appartient VALUES (  3 , 3 ) ;
INSERT INTO appartient VALUES (  2 , 2 ) ;
INSERT INTO appartient VALUES (  4 , 1 ) ;
INSERT INTO appartient VALUES (  5 , 2 ) ;
INSERT INTO appartient VALUES (  6, 4 ) ;
INSERT INTO appartient VALUES (  7 , 8 ) ;
INSERT INTO appartient VALUES (  8 , 9 ) ;
INSERT INTO appartient VALUES (  9 , 9 ) ;
INSERT INTO appartient VALUES (  1 , 10 ) ;
INSERT INTO appartient VALUES (  2 , 11 ) ;
INSERT INTO appartient VALUES (  3 , 12 ) ;
INSERT INTO appartient VALUES (  8 , 13) ;
INSERT INTO appartient VALUES (  5 , 14 ) ;
INSERT INTO appartient VALUES (  8 , 15) ;





BEGIN;
-- eleves
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('PARIS'     , 75056      , '40 avenue de Ségur, 75015'  ) ;
INSERT INTO personnes(nom, prenom, adresse_mail, numero_telephone) VALUES ('Martin', 'Martine','martine@yahoo.fr', 0612345678  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (2, 'informatique', 16, 1 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('RENNES'     , 35200    , '4 Avenue de la Vistule'  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('sebastien', 'lesage','sebastien@gmail.fr', 0641587963  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (1, 'electronique', 17, 2 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('NANCY'     ,   54000 , ' 119 Avenue de Strasbourg'  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Eric', 'lepetit','eric@gmail.fr', 0641235896  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (1, 'telecom', 18, 3 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('SAINT-ÉTIENNE'     , 42000   , '2 Avenue Grüner  '  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Pivot', 'glissant','pivot@gmail.fr', 061258389  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (2, 'informatique', 19, 4 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('SAINT-ÉTIENNE'     , 42000   , '2 Avenue Grüner  '  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('souf', 'legrand','souf@gmail.fr', 0612547859  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (1, 'matmeca', 20, 5 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('TALENCE'     , 33400       , '30 avenue des facultes'  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('said', 'baha','baha@gmail.fr', 0612357859  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (1, 'informatique', 21, 6 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('BERGERAC'     ,   24100 , ' 12 Avenue Pasteur'  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('karim', 'benkirane','karim@gmail.fr', 0613457859  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (1, 'telecom', 22, 7 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('SAINT-ÉTIENNE'     , 42000   , '2 Avenue Grüner  '  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('omar', 'saidi','omar@gmail.fr', 0612546899  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (1, 'matmeca', 23, 8 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('TALENCE'     , 33400       , '30 avenue des facultes'  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('hajar', 'refaeli','hajar@gmail.fr', 0612258859  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (1, 'electronique', 24, 9 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('BERGERAC'     ,   24100 , ' 12 Avenue Pasteur'  ) ;
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('karima', 'bouaissi','karima@gmail.fr', 0478547859  ) ;
INSERT INTO eleves(annee, departement, adresse_id, personne_id) VALUES (1, 'matmeca', 25, 10 ) ;



-- contact
INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Martin', 'Martin','martin@gmail.fr', 0612345789  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 11, 2 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Xavier', 'Lebeau','xavier@gmail.fr', 0234567891  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('SC', 12, 3 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Katrin', 'Kant','katrin@gmail.fr', 0123457895  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 13, 4 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Martini', 'Guti','guti@gmail.fr', 0623457897  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 14, 5 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Karim', 'Benzema','karim@gmail.fr', 0613457896  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 15, 6 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Antoine', 'beau','antoine@gmail.fr', 0612457896  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 16, 7 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Raphael', 'Nadal','nadal@gmail.fr', 0652357896  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 17, 8 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Fahd', 'Ettouhami','fahd@gmail.fr', 0987457896  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 18, 9 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Anouar', 'Ghazoul','ghazoul@gmail.fr', 0612526896  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 19, 10 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Saad', 'Ammor','saad@gmail.fr', 0611258896  ) ;
INSERT INTO contacts(fonction, personne_id, entreprise_id) VALUES ('DG', 20, 11 ) ;

-- reponsable_pedagogique

INSERT INTO personnes(nom, prenom, adresse_mail, numero_telephone) VALUES ('Pivot', 'Estelle','estelle@gmail.fr', 061254389  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 21 ) ;

INSERT INTO personnes(nom, prenom, adresse_mail, numero_telephone) VALUES ( 'Cristiano', 'alex','Cristiano@gmail.fr', 061253894  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 22 ) ;

INSERT INTO personnes(nom, prenom, adresse_mail, numero_telephone) VALUES ('Diego', 'Maradonna','diego@gmail.fr', 061254589  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 23 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Raphael', 'Haroche','Haroche@gmail.fr', 061254379  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 24 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Roger', 'Federer','roger@gmail.fr', 061254779  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 25 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Marc', 'Lacombe','marc@gmail.fr', 061242379  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 26 ) ;

INSERT INTO personnes(nom, prenom, adresse_mail, numero_telephone) VALUES ('Curtis', 'Jackson','Curtis@gmail.fr', 063694779  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 27 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Jean-Léon', 'Gerome','gerome@gmail.fr', 062574779  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 28 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Xavier', 'Niel','Niel@gmail.fr', 036254779  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 29 ) ;

INSERT INTO personnes(prenom, nom, adresse_mail, numero_telephone) VALUES ('Magnus', 'Maximus','Maximus@gmail.fr', 061254369  ) ;
INSERT INTO responsables_pedagogiques(personne_id) VALUES ( 30 ) ;
COMMIT;


--adresses
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('TALENCE'     , 33400       , '30 avenue des facultés'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('BORDEAUX'     , 33000       , '30 rue ste catherine'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('TOULOUSE'     , 31000       , '30 rue des lois'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('TALENCE'     , 33400       , '30 avenue des facultes'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('PARIS'     , 75056      , '40 avenue de Ségur, 75015'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('RENNES'     , 35200    , '4 Avenue de la Vistule'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LILLE'     , 59000    , '1, boulevard Vauban '  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('PESSAC'     , 33600    , '20 avenue de bardanac'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('NICE'     ,   06000 , '35 Avenue Jean Médecin, '  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('BERGERAC'     ,   24100 , ' 12 Avenue Pasteur'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('STRASBOURG'     ,  67100  , 'Avenue de Colmar '  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('NANCY'     ,   54000 , ' 119 Avenue de Strasbourg'  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('MARSEILLE'     ,  13004  , '10, avenue Foch  '  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('SAINT-ÉTIENNE'     , 42000   , '2 Avenue Grüner  '  ) ;
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LYON'     ,   69100 , '45, avenue Albert Einstein  '  ) ;


-- propositions de stage
INSERT INTO adresses(ville, code_postal, adresse) VALUES ('TALENCE'     , 33400       , '30 avenue des facultes'  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('creation application sur transport', 2015, 'informatique', 'groupe1', DATE '2015-12-01',DATE '2016-01-01',1000,1, 26 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('BORDEAUX'     , 33000       , '30 rue ste catherine'  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('creation application C', 2015, 'informatique', 'groupe2', DATE '2016-12-01',DATE '2017-01-01',10002,1, 27 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('TALENCE'     , 33400       , '30 avenue des facultes'  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('creation application C++', 2015, 'telecom', 'groupe3', DATE '2017-12-01',DATE '2018-01-01',1002,2, 28 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('MARSEILLE'     ,  13004  , '10, avenue Foch  '  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('creation application Java', 2015, 'telecom', 'groupe4', DATE '20118-12-01',DATE '2019-01-01',10005,3, 29 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LILLE'     , 59000    , '1, boulevard Vauban '  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('magnetisme', 2015, 'electronique', 'groupe7', DATE '2020-12-01',DATE '2021-01-01',10008,4, 30 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('SAINT-ÉTIENNE'     , 42000   , '2 Avenue Grüner  '  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('electromagnetisme', 2015, 'electronique', 'groupe8', DATE '2021-12-01',DATE '2022-01-01',10001,5, 31 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('PARIS'     , 75056      , '40 avenue de Ségur, 75015'  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('creation site web', 2015, 'telecom', 'groupe9', DATE '2021-12-01',DATE '2022-01-01',10001,6, 32 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('LYON'     ,   69100 , '45, avenue Albert Einstein  '  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('VHDL', 2015, 'electronique', 'groupe10', DATE '2022-12-01',DATE '2023-01-01',10001,8, 33 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('BORDEAUX'     , 33000       , '30 rue ste catherine'  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ('Analogique', 2015, 'electronique', 'groupe11', DATE '2023-12-01',DATE '2024-01-01',10001,8, 34 ) ;

INSERT INTO adresses(ville, code_postal, adresse) VALUES ('PARIS'     , 75056      , '40 avenue de Ségur, 75015'  ) ;
INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id) VALUES ( 'Decoupage reseaux', 2015, 'telecom', 'groupe12', DATE '2024-12-01',DATE '2025-01-01',10001,8, 35 ) ;


--consultations
INSERT INTO consultations VALUES ( 1,1 ) ;
INSERT INTO consultations VALUES ( 2,2 ) ;
INSERT INTO consultations VALUES ( 3,3 ) ;
INSERT INTO consultations VALUES ( 4,4 ) ;
INSERT INTO consultations VALUES ( 5,5 ) ;
INSERT INTO consultations VALUES ( 6,6 ) ;
INSERT INTO consultations VALUES ( 7,7 ) ;
INSERT INTO consultations VALUES ( 8,8 ) ;
INSERT INTO consultations VALUES ( 9,9 ) ;
INSERT INTO consultations VALUES ( 10,10 ) ;




-- affectations
INSERT INTO affectations VALUES ( 1, 4, 1 ) ;
INSERT INTO affectations VALUES ( 2, 4, 2 ) ;
INSERT INTO affectations VALUES ( 3, 4, 3 ) ;
INSERT INTO affectations VALUES ( 4, 5, 4 ) ;
INSERT INTO affectations VALUES ( 5, 6, 5 ) ;

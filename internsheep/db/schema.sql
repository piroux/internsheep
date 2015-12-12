--CREATE_DATABASE stages;

DROP TABLE IF EXISTS secteurs  CASCADE;
DROP TABLE IF EXISTS entreprises  CASCADE;
DROP TABLE IF EXISTS adresses  CASCADE;
DROP TABLE IF EXISTS eleves CASCADE;
DROP TABLE IF EXISTS personnes CASCADE;
DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS responsables_pedagogiques CASCADE;
DROP TABLE IF EXISTS propositions_stage CASCADE;
DROP TABLE IF EXISTS consultations CASCADE;
DROP TABLE IF EXISTS affectations CASCADE;
DROP TABLE IF EXISTS appartient CASCADE;

DROP TABLE IF EXISTS regions CASCADE;
DROP TABLE IF EXISTS departements CASCADE;


CREATE TABLE adresses
(
	adresse_id	serial		not null,
	ville 	   	char(100)	not null,
	code_postal	char(5)     	,
	adresse   	char(200)   	,
	PRIMARY KEY (adresse_id)
);


CREATE TABLE personnes
(
	personne_id	serial		not null,
	nom          	char(30)     	not null,
	prenom       	char(30)  	not null,
	adresse_mail 	char(30)         ,
	numero_telephone char(30)	     	 ,
	PRIMARY KEY    (personne_id)
);


CREATE TABLE secteurs
(
	secteur_id	serial		not null,
	nom_secteur     char(40)        not null,
	PRIMARY KEY (secteur_id)
);


CREATE TABLE entreprises
(
	entreprise_id	serial		 not null,
	nom_entreprise 	char(40)	 not null,
	numero_telephone char(30)		 	,
	site_web	 char(150)		,
	type_entreprise	 char(50)		,
	nombre_salarie	 int			,
	adresse_id	 int		references adresses(adresse_id),
	PRIMARY KEY 	 (entreprise_id)
);

CREATE INDEX ON entreprises (adresse_id);


CREATE TABLE appartient
(
	secteur_id	int		not null references secteurs(secteur_id),
	entreprise_id	int		not null references entreprises(entreprise_id),
	PRIMARY KEY	(secteur_id,entreprise_id)
);


CREATE TABLE eleves
(
	eleve_id	serial		not null,
	annee 	  	int		    ,
	departement	char(50)     	    ,
	adresse_id   	int  	  	references adresses(adresse_id)    ,
	personne_id	int    		not null  references personnes(personne_id),
	PRIMARY KEY (eleve_id)
);

CREATE INDEX ON eleves (adresse_id);
CREATE INDEX ON eleves (personne_id);


CREATE TABLE contacts
(
	contact_id     serial		not null,
	fonction       char(40)    	not null,
	personne_id    int	   	not null references personnes(personne_id),
	entreprise_id  int	   	not null references entreprises(entreprise_id),
	PRIMARY KEY  (contact_id)
);

CREATE INDEX ON contacts (personne_id);
CREATE INDEX ON contacts (entreprise_id);


CREATE TABLE responsables_pedagogiques
(
	responsable_id     serial		not null,
	personne_id    int   not null references personnes(personne_id),
	PRIMARY KEY (responsable_id)
);


CREATE TABLE propositions_stage
(
	proposition_id    serial		not null,
	sujet             char(150)      not null,
	annee             int     	,
	domaine           char(50)      ,
	groupe            char(50)      ,
	date_debut        date          ,
	date_fin          date          ,
	indemnite         int    	,
	contact_id        int	     	not null references contacts(contact_id),
	adresse_id        int	     	not null  references adresses(adresse_id),
	PRIMARY KEY(proposition_id)
);

CREATE INDEX ON propositions_stage (contact_id);
CREATE INDEX ON propositions_stage (adresse_id);


CREATE TABLE consultations
(
	eleve_id		int			not null,
	proposition_id  int    		not null,
	PRIMARY KEY (eleve_id , proposition_id)
);


CREATE TABLE affectations
(
	eleve_id		int			UNIQUE not null references eleves(eleve_id),
	responsable_id 	int 		not null references responsables_pedagogiques(responsable_id),
	proposition_id  int    		not null references propositions_stage(proposition_id),
	PRIMARY KEY (proposition_id)
);

CREATE INDEX ON affectations (responsable_id);


CREATE TABLE regions (
  region_id 	     int		NOT NULL,
  nom char	     (100) 		NOT NULL,
  PRIMARY KEY  (region_id)
);


CREATE TABLE departements (
  departement_id	int NOT NULL,
  region_id			int NOT NULL references regions(region_id),
  nom				char(50) NOT NULL,
  PRIMARY KEY  (departement_id)
);


-- ===================================
--            Triggers et contraintes
-- ===================================


-- une personne doit être un contact un eleve ou un responsable
 CREATE OR REPLACE FUNCTION inclusion() RETURNS trigger AS $$
 BEGIN
	IF (
 	   (SELECT count(*)
  	   FROM
	   ((SELECT personne_id FROM personnes)
    	   EXCEPT ALL
  	   (SELECT personne_id FROM eleves
  	   UNION ALL
  	   SELECT personne_id FROM contacts
  	   UNION ALL
  	   SELECT personne_id FROM responsables_pedagogiques)
  	   )
	   as inclusion)
   	   != 0)
	THEN
    	RAISE EXCEPTION 'creation de personne qui n est ni un contact ni un responsable ni un eleve';
	END IF;
    return NULL;
    END;
 $$ LANGUAGE plpgsql;

CREATE CONSTRAINT TRIGGER incl AFTER INSERT OR UPDATE OR DELETE
ON personnes
INITIALLY DEFERRED
FOR EACH ROW
EXECUTE PROCEDURE inclusion();


-- une personne ne peut avoir qu'un seul role : eleve ou contact ou responsable
 CREATE OR REPLACE FUNCTION intersection() RETURNS trigger AS $intersec$
  BEGIN
	 IF (
	   ( SELECT count(*)
  	    FROM
	    ((SELECT personne_id FROM eleves
	    INTERSECT ALL
	    SELECT personne_id FROM contacts)
	    UNION ALL
	   (SELECT personne_id FROM eleves
	    INTERSECT ALL
	    SELECT personne_id FROM responsables_pedagogiques)
	    UNION ALL
	    (SELECT personne_id FROM contacts
	    INTERSECT ALL
	    SELECT personne_id FROM responsables_pedagogiques)) as sbq)
  	   != 0)
	THEN
    	RAISE EXCEPTION 'cette personne est deja un eleve, un contact ou un responsable';
 	END IF;
   return NULL;
   END;
   $intersec$ LANGUAGE plpgsql;



CREATE TRIGGER intersec1 AFTER INSERT OR UPDATE OR DELETE
ON eleves
FOR EACH ROW
EXECUTE PROCEDURE intersection();

CREATE TRIGGER intersec2 AFTER INSERT OR UPDATE OR DELETE
ON contacts
FOR EACH ROW
EXECUTE PROCEDURE intersection();

CREATE TRIGGER intersec3 AFTER INSERT OR UPDATE OR DELETE
ON responsables_pedagogiques
FOR EACH ROW
EXECUTE PROCEDURE intersection();

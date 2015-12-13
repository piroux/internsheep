/* 1)
select*
from entreprises inner join appartient on
appartient.entreprise_id = entreprises.entreprise_id
*/

/*
2)
select nombre_salarie
from entreprises
where nombre_salarie> 2
and nombre_salarie<1000;
*/

/*3)
select *
from entreprises inner join adresses on
entreprises.adresse_id = adresses.adresse_id
and adresses.ville = 'TALENCE';
*/

/*
--4)
select fonction
from contacts;
5)
select sujet
from propositions_stage;
*/


/* 6)
select annee
from eleves inner join affectations on
eleves.eleve_id = affectations.eleve_id
inner join responsables_pedagogiques on
affectations.personne_id = responsables_pedagogiques.personne_id;
*/


/*
7)
select departement, AVG(date_fin - date_debut) as DUREE
from affectations inner join propositions_stage on
propositions_stage.proposition_id = affectations.proposition_id
inner join eleves on
affectations.eleve_id = eleves.eleve_id
group by eleves.departement;
*/

/*
8)

select annee , count(*) as nombre_propositions
from propositions_stage
group by annee;
*/

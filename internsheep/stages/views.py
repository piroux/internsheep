# -*- encoding: utf-8 -*-

from flask import Blueprint, current_app, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask.ext.wtf import Form
from flask.ext.classy import FlaskView, route
from wtforms import fields, validators, widgets

from . import stages_bp

from . import models
from ..geo.models import *
from ..organisations.models import *
from ..personnels.models import *

from ..base.views import InternsheepView, flash_errors

################################################################################
# Eleves
################################################################################

class PropositionForm(Form):
    sujet = fields.StringField(u'Sujet', [validators.DataRequired(), validators.Length(max=150)])
    annee = fields.IntegerField(u'Année', [validators.DataRequired(), validators.NumberRange(min=1000, max=3000)])
    domaine = fields.StringField(u'Domaine', [validators.Length(max=50)])
    groupe = fields.StringField(u'Groupe', [validators.Length(max=50)])
    date_debut = fields.DateField(u'Date Debut')
    date_fin = fields.DateField(u'Date Fin')
    indemnite = fields.IntegerField(u'Indemnite', [validators.NumberRange(min=0)])
    eleve_id = fields.SelectField(u'Eleve', coerce=int)
    responsable_id = fields.SelectField(u'Responsable', coerce=int)
    contact_id = fields.SelectField(u'Contact', coerce=int, validators=[validators.DataRequired()])
    ville = fields.StringField(u'Ville', [validators.DataRequired(), validators.Length(max=100)])
    code_postal = fields.StringField(u'Code Postal', [validators.DataRequired(), validators.Length(max=5)])
    adresse = fields.StringField(u'Adresse', [validators.DataRequired(), validators.Length(max=200)])
    submit = fields.SubmitField(u'Valider')

class PropositionView(InternsheepView):
    section_name = 'Stages'
    object_name = 'proposition'
    route_base = object_name + 's'
    object_form = PropositionForm
    object_model = models

    choices_handler = {
        'eleve_id': lambda self: [(0, u'Non affecté')] + ([(self._form.eleve_id.data, str_eleve(self._form.eleve_id.data))] if self._form.eleve_id.data else []) + [(eleve['eleve_id'], str_eleve(eleve['eleve_id'])) for eleve in list_eleves_non_affectes()],
        'responsable_id': lambda self: [(0, u'Non affecté')] + [(responsable['responsable_id'], str_responsable(responsable['responsable_id'])) for responsable in list_responsables()],
        'contact_id': lambda self: [(contact['contact_id'], str_contact(contact['contact_id'])) for contact in list_contacts()]
    }

PropositionView.register(stages_bp)

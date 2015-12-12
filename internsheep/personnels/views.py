# -*- encoding: utf-8 -*-

from flask import Blueprint, current_app, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask.ext.wtf import Form
from flask.ext.classy import FlaskView, route
from wtforms import fields, validators, widgets

from . import personnels_bp

from . import models
from ..organisations.models import *

from ..base.views import InternsheepView, flash_errors


################################################################################
# Personnes
################################################################################

class PersonneForm(Form):
    nom = fields.StringField(u'Nom', [validators.DataRequired(), validators.Length(max=30)])
    prenom = fields.StringField(u'Prénom', [validators.DataRequired(), validators.Length(max=30)])
    adresse_mail = fields.StringField(u'Adresse Mail', [validators.Optional(), validators.Email(), validators.Length(max=30)])
    numero_telephone = fields.StringField(u'Téléphone', [validators.Optional(), validators.Length(max=30)])

################################################################################
# Eleves
################################################################################

class EleveForm(PersonneForm):
    annee = fields.IntegerField(u'Année', [validators.DataRequired(), validators.NumberRange(min=1, max=4)])
    departement = fields.SelectField(u'Filière', [validators.DataRequired()], choices=[
        (u'I', u'Informatique'), (u'E', u'Electronique'),
        (u'M', u'Matmeca'), (u'T', u'Télécommunication'),
        (u'X', u'Autre')])
    ville = fields.StringField(u'Ville', [validators.DataRequired(), validators.Length(max=100)])
    code_postal = fields.StringField(u'Code Postal', [validators.DataRequired(), validators.Length(max=5)])
    adresse = fields.StringField(u'Adresse', [validators.DataRequired(), validators.Length(max=200)])
    submit = fields.SubmitField(u'Valider')

class EleveView(InternsheepView):
    section_name = 'Personnels'
    object_name = 'eleve'
    route_base = object_name + 's'
    object_form = EleveForm
    object_model = models

EleveView.register(personnels_bp)

################################################################################
# Contacts
################################################################################

class ContactForm(PersonneForm):
    fonction = fields.StringField(u'Fonction', [validators.Length(max=40), validators.DataRequired()])
    entreprise_id = fields.SelectField(u'Entreprise',
        coerce=int,
        validators=[validators.DataRequired()])
    submit = fields.SubmitField(u'Valider')

class ContactView(InternsheepView):
    section_name = 'Personnels'
    object_name = 'contact'
    route_base = object_name + 's'
    object_form = ContactForm
    object_model = models

    choices_handler = {
        'entreprise_id': lambda self: [(entreprise['entreprise_id'], entreprise['nom_entreprise']) for entreprise in list_entreprises()]
    }

    #@route('/edit/<int:_id>', methods=['GET', 'POST'])
    #def edit(self, _id):
    #    one = self.model_get(_id)
    #    if one is None:
    #        flash("L'objet {} numero {} n'existe pas".format(self.object_name, _id), 'danger')
    #        return redirect(url_for('.{}:list'.format(self.object_title)))
    #    else:
    #        form = self.object_form(**one)
    #        form.entreprise_id.choices = [(entreprise['entreprise_id'], entreprise['nom_entreprise']) for entreprise in list_entreprises()] ####
    #        if request.method == 'POST':
    #            if form.validate_on_submit():
    #                self.model_update(_id, **form.data)
    #                flash(u'Edition réussie de l\'objet {}'.format(self.object_name), 'success')
    #                return redirect(url_for('.{}:list'.format(self.object_title)))
    #            else:
    #                current_app.logger.warning(form.errors)
    #                flash_errors(form)
    #    return render_template('generic/add.html', form=form,
    #        sectname=self.section_name, objname=self.object_name, action='Edition')

ContactView.register(personnels_bp)

################################################################################
# Responsables
################################################################################

class ResponsableForm(PersonneForm):
    submit = fields.SubmitField(u'Valider')

class ResponsableView(InternsheepView):
    section_name = 'Personnels'
    object_name = 'responsable'
    route_base = object_name + 's'
    object_form = ResponsableForm
    object_model = models

ResponsableView.register(personnels_bp)

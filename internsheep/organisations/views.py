# -*- encoding: utf-8 -*-

from flask import Blueprint, current_app, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask.ext.wtf import Form
from flask.ext.classy import FlaskView, route
from wtforms import fields, validators, widgets

from . import organisations_bp

from . import models

from ..base.views import InternsheepView, flash_errors


################################################################################
# Entreprises
################################################################################

class EntrepriseForm(Form):
    nom_entreprise = fields.StringField(u'Nom de l\'entreprise', [validators.DataRequired(), validators.Length(max=40)])
    site_web = fields.StringField(u'Website', [validators.Optional(), validators.URL(require_tld=True), validators.Length(max=150)])
    type_entreprise = fields.SelectField(u'Raison sociale', [validators.DataRequired()], choices=[
        (u'SA', u'Société Anonyme'), (u'SARL', u'Société à Responsabilité Limitée'),
        (u'SAS', u'Société par Actions Simplifiée'), (u'SNC', u'Société en Nom Collectif'),
        (u'X', u'Autre')])
    nombre_salarie = fields.IntegerField(u'Nb salariés', [validators.NumberRange(min=1)])
    adresse_id = fields.IntegerField(u'Adresse')
    ville = fields.StringField(u'Ville', [validators.DataRequired(), validators.Length(max=100)])
    code_postal = fields.StringField(u'Code Postal', [validators.DataRequired(), validators.Length(max=5)])
    adresse = fields.StringField(u'Adresse', [validators.DataRequired(), validators.Length(max=200)])
    numero_telephone = fields.StringField(u'Téléphone', [validators.Optional(), validators.Length(max=30)])
    secteurs = fields.SelectMultipleField(u'Secteurs d\'activités',
        coerce=int,
        validators=[validators.optional()])
    submit = fields.SubmitField(u'Valider')

class EntrepriseView(InternsheepView):
    section_name = 'Organisations'
    object_name = 'entreprise'
    route_base = object_name + 's'
    object_form = EntrepriseForm
    object_model = models

    choices_handler = {
        'secteurs': lambda self: [(secteur['secteur_id'], secteur['nom_secteur']) for secteur in self.object_model.list_secteurs()]
    }

    #@route('/add', methods=['GET', 'POST'])
    #def add(self):
    #    form = self.object_form()
    #    form.secteurs.choices = [(secteur['secteur_id'], secteur['nom_secteur']) for secteur in models.list_secteurs()] ####
    #    if form.validate_on_submit():
    #        self.model_create(**form.data)
    #        flash(u'Ajout réussi de l\'objet {}'.format(self.object_name), 'success')
    #        return redirect(url_for('.{}:list'.format(self.object_title)))
    #    if request.method == 'POST':
    #        current_app.logger.warning(form.errors)
    #        flash_errors(form)
    #    return render_template('generic/add.html', form=form,
    #        sectname=self.section_name, objname=self.object_name, action='Ajout')

    #@route('/edit/<int:_id>', methods=['GET', 'POST'])
    #def edit(self, _id):
    #    one = self.model_get(_id)
    #    if one is None:
    #        flash("L'objet {} numero {} n'existe pas".format(self.object_name, _id), 'danger')
    #        return redirect(url_for('.{}:list'.format(self.object_title)))
    #    else:
    #        form = self.object_form(**one)
    #        form.secteurs.choices = [(secteur['secteur_id'], secteur['nom_secteur']) for secteur in models.list_secteurs()] ####
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

    @route('/', methods=['GET'])
    def list(self):
        listall = self.model_list()
        listagg = models.list_aggregate_entreprises_secteurs()
        for o in listall:
            o['edit_url'] = url_for('.{}:edit'.format(self.object_title), _id=o['{}_id'.format(self.object_name)])
            o['delete_url'] = url_for('.{}:delete'.format(self.object_title), _id=o['{}_id'.format(self.object_name)])
            o['liste_secteurs'] = [agg['nom_secteur'] for agg in listagg[o['entreprise_id']]] if o['entreprise_id'] in listagg else [] ####
        add_url = url_for('.{}:add'.format(self.object_title))
        return render_template('generic/list.html', listall=listall, add_url=add_url,
            sectname=self.section_name, objname=self.object_name, action='Liste')

EntrepriseView.register(organisations_bp)

################################################################################
# Secteurs
################################################################################

class SecteurForm(Form):
    nom_secteur = fields.StringField(u'Nom du secteur', [validators.Length(max=40)])
    submit = fields.SubmitField(u'Valider')

class SecteurView(InternsheepView):
    section_name = 'Organisations'
    object_name = 'secteur'
    route_base = object_name + 's'
    object_form = SecteurForm
    object_model = models

    @route('/', methods=['GET'])
    def list(self):
        listall = self.model_list()
        listagg = models.list_aggregate_secteurs_entreprises()
        for o in listall:
            o['edit_url'] = url_for('.{}:edit'.format(self.object_title), _id=o['{}_id'.format(self.object_name)])
            o['delete_url'] = url_for('.{}:delete'.format(self.object_title), _id=o['{}_id'.format(self.object_name)])
            o['liste_entreprises'] = [agg['nom_entreprise'] for agg in listagg[o['secteur_id']]] if o['secteur_id'] in listagg else [] ####
        add_url = url_for('.{}:add'.format(self.object_title))
        return render_template('generic/list.html', listall=listall, add_url=add_url,
            sectname=self.section_name, objname=self.object_name, action='Liste')

SecteurView.register(organisations_bp)

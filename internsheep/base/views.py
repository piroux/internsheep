# -*- encoding: utf-8 -*-

from flask import Blueprint, current_app, request, session, g, redirect, url_for, \
     abort, render_template, flash

from flask.ext.classy import FlaskView, route

from utils import flash_errors

import ipdb

class InternsheepView(FlaskView):

    # To be overwritten
    section_name = 'Main'
    object_name = ''
    object_form = None
    object_model = None


    # Defferred accesses
    object_title = property(lambda self: '{}View'.format(self.object_name.title()))

    model_create = property(lambda self: getattr(self.object_model, 'create_{}'.format(self.object_name)))
    model_update = property(lambda self: getattr(self.object_model, 'update_{}'.format(self.object_name)))
    model_get = property(lambda self: getattr(self.object_model, 'get_{}'.format(self.object_name)))
    model_delete = property(lambda self: getattr(self.object_model, 'delete_{}'.format(self.object_name)))
    model_list = property(lambda self: getattr(self.object_model, 'list_{}s'.format(self.object_name)))

    choices_handler = {} # (field_name for choices : deffered handler for choices)

    def _fetch_choices(self, form):
        if self.choices_handler:
            for choice_fieldname, choice_handler in self.choices_handler.items():
                getattr(form, choice_fieldname).choices = choice_handler(self)
                print getattr(form, choice_fieldname).choices

    @route('/add', methods=['GET', 'POST'])
    def add(self):
        form = self.object_form()
        self._form = form
        print "self.choices_handler:", self.choices_handler
        self._fetch_choices(form)
        if form.validate_on_submit():
            self.model_create(**form.data)
            flash(u'Ajout réussi de l\'objet {}'.format(self.object_name), 'success')
            return redirect(url_for('.{}:list'.format(self.object_title)))
        if request.method == 'POST':
            current_app.logger.warning(form.errors)
            flash_errors(form)
        return render_template('generic/add.html', form=form,
            sectname=self.section_name, objname=self.object_name, action='Ajout')


    @route('/', methods=['GET'])
    def list(self):
        listall = self.model_list()
        for o in listall:
            o['edit_url'] = url_for('.{}:edit'.format(self.object_title), _id=o['{}_id'.format(self.object_name)])
            o['delete_url'] = url_for('.{}:delete'.format(self.object_title), _id=o['{}_id'.format(self.object_name)])
        add_url = url_for('.{}:add'.format(self.object_title))
        return render_template('generic/list.html', listall=listall, add_url=add_url,
            sectname=self.section_name, objname=self.object_name, action='Liste')


    @route('/edit/<int:_id>', methods=['GET', 'POST'])
    def edit(self, _id):
        one = self.model_get(_id)
        if one is None:
            flash("L'objet {} numero {} n'existe pas".format(self.object_name, _id), 'danger')
            return redirect(url_for('.{}:list'.format(self.object_title)))
        else:
            form = self.object_form(**one)
            self._form = form
            self._fetch_choices(form)
            if request.method == 'POST':
                if form.validate_on_submit():
                    self.model_update(_id, **form.data)
                    flash(u'Edition réussie de l\'objet {}'.format(self.object_name), 'success')
                    return redirect(url_for('.{}:list'.format(self.object_title)))
                else:
                    current_app.logger.warning(form.errors)
                    flash_errors(form)
        return render_template('generic/add.html', form=form,
            sectname=self.section_name, objname=self.object_name, action='Edition')


    @route('/delete/<int:_id>', methods=['GET'])
    def delete(self, _id):
        one = self.model_get(_id)
        params = {}
        if one is None:
            flash("L'objet {} numero {} n'existe pas".format(self.object_name, _id), 'danger')
            return redirect(url_for('.{}:list'.format(self.object_title)))
        else:
            if request.args.get('confirm', ''):
                self.model_delete(_id)
                flash(u'Suppression réussie de l\'objet {}'.format(self.object_name), 'success')
                return redirect(url_for('.{}:list'.format(self.object_title)))
            else:
                params['delete_url'] = url_for('.{}:delete'.format(self.object_title), _id=_id)
        return render_template('generic/delete.html',
            sectname=self.section_name, objname=self.object_name, action='Suppression',
            **params)

# -*- encoding: utf-8 -*-

from flask import Blueprint, current_app, request, session, g, redirect, url_for, \
     abort, render_template, flash


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'warning')

# -*- encoding: utf-8 -*-

from flask import Blueprint, current_app, request, session, g, redirect, url_for, \
     abort, render_template, flash


main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def lol():
    return redirect('stages/propositions/')

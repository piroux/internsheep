# -*- encoding: utf-8 -*-

from flask import Blueprint, current_app, request, session, g, redirect, url_for, \
     abort, render_template, flash

from . import main_bp


@main_bp.route('/')
def lol():
    return redirect('stages/propositions/')

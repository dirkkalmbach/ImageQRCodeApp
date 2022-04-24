from flask import Blueprint, render_template, redirect, url_for
from project import db

userdata_blueprint = Blueprint('userdata',
                              __name__,
                              template_folder='templates/userdata')

@userdata_blueprint.route('/qr', methods=['GET', 'POST'])
def qr():

    return render_template('qr.html')


@userdata_blueprint.route('/create', methods=['GET', 'POST'])
def create():

    return render_template('create.html')

@userdata_blueprint.route('/get', methods=['GET', 'POST'])
def get():

    return render_template('get.html')
from flask import Blueprint, render_template, redirect, url_for
from project import db

qrcode_blueprint = Blueprint('qrcode',
                              __name__,
                              template_folder='templates/qrcode')

@qrcode_blueprint.route('/basicqr', methods=['GET', 'POST'])
def basic_qr():

    return render_template('basicqr.html')


@qrcode_blueprint.route('/imageqr', methods=['GET', 'POST'])
def image_qr():

    return render_template('imageqr.html')
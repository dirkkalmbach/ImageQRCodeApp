from flask import Blueprint, render_template, redirect, url_for

from project import db
from project.qrcode.forms import BasicQR
from werkzeug.utils import secure_filename

import os
import io
import segno


qrcode_blueprint = Blueprint('qrcode',
                              __name__,
                              template_folder='templates/qrcode')


@qrcode_blueprint.route('/basicqr', methods=['GET', 'POST'])
def qr():
    url="www.myexample.org"
    scale=4
    error="L"
    form = BasicQR()

    if form.validate_on_submit():
        url = form.qr_content.data
        scale = form.size.data
        error = form.error.data

    if scale=="":
        scale=4

    # Color Setting   
    # main:
    data_light="white"#None#"brown"
    data_dark="black"#None#"red"
    # separator squares:
    dark="green"#'black'
    light="white" #None=transparent

    # small
    alignment_light=light
    alignment_dark="yellow"
    finder_light="orange"
    separator=light #space around separator squares
    version_dark="blue"
    version_light="blue"
    # background:
    quiet_zone=None#'green' #surrounding background
    border=4
    
    
    qrcode = segno.make(url, micro=None, error=error)
    return render_template('basicqr.html', form=form, qr_content=url, scale=int(scale), 
                            error=error, qrcode=qrcode, 
                            data_light=data_light, data_dark=data_dark, 
                            dark=dark, light=light, alignment_dark=alignment_dark, alignment_light=alignment_light,
                            finder_light=finder_light,
                            separator=separator,
                            version_dark=version_dark,
                            version_light=version_light,
                            quiet_zone=quiet_zone,
                            border=border)






@qrcode_blueprint.route('/imageqr', methods=['GET', 'POST'])
def image_qr():

    return render_template('imageqr.html')


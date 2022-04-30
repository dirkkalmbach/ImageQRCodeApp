from flask import Blueprint, render_template, redirect, url_for, make_response, session, request, flash

from project import db
from project.qrcode.forms import BasicQR, ColoursForm
from werkzeug.utils import secure_filename
from base64 import b64decode
import os
import io
import segno
from segno import helpers


qrcode_blueprint = Blueprint('qrcode',
                              __name__,
                              template_folder='templates/qrcode')


@qrcode_blueprint.route('/basicqr', methods=['GET', 'POST'])
def qr():
    y="not downloaded"
    url="www.myexample.org"
    scale=4
    error="L"
    form = BasicQR()
    form2 = ColoursForm()
    format = "png"
    dpi = 72
    

    # COLOR SETTINGS
    # separator squares
    dark='red'
    light="green" #None=transparent
    # main
    data_light="white"#None#"brown"
    data_dark="black"#None#"red"
    # background:
    quiet_zone=None#'green' #surrounding background
    border=4
    # small sqare 
    alignment_light="orange"
    alignment_dark="red"
    # 3 big squares
    finder_light="orange"
    finder_dark="red"
    separator=light #space around separator squares
    # not sure where these are ???
    version_dark="blue"
    version_light="blue"

    if form.is_submitted():
        url = form.qr_content.data
        scale = form.size.data
        error = form.error.data
        format = form.format.data
        #dpi = form.dpi.data
        #mask = int(form.mask.data) #! I dont know default (default is found by algo)
        dark = form2.dark_color.data
        light = form2.light_color.data
        data_light = form2.data_light.data
        data_dark = form2.data_dark.data
        #quiet_zone = form2.quiet_zone.data
        #alignment_light = form2.alignment_light.data
        #alignment_dark = form2.alignment_dark.data
        #border = int(form.border.data)
        finder_light = form2.finder_light.data
        finder_dark = form2.finder_dark.data
        separator = form2.separator.data
        version_dark = form2.version_dark.data
        version_light = form2.version_light.data
        test = form.test.data
        flash(f"You typed {test} with datatype {type(test)} 🧐")
    if scale=="":
        scale=4

    qrcode = segno.make(url, micro=None, error=error)
    session['dict'] = {'url' : url, 'scale' : int(scale),
            'micro' : None,
            'error' : error,
            'data_light' : data_light, 'data_dark' : data_dark,
            'dark' : dark, 'light' : light, 
            'alignment_dark' : alignment_dark, 'alignment_light' : alignment_light,
            'finder_light' : finder_light, 'finder_dark' : finder_dark,
            'separator' : separator,
            'version_dark' : version_dark, 'version_light' : version_light,
            'quiet_zone' : quiet_zone, 'border' : border,
            'format' : format, 
            'dpi' : dpi,
            }
        
    return render_template('basicqr.html', form=form, form2=form2, format=format,
                            qr_content=url, scale=int(scale), 
                            error=error, qrcode=qrcode, 
                            data_light=data_light, data_dark=data_dark, 
                            dark=dark, light=light, alignment_dark=alignment_dark, alignment_light=alignment_light,
                            finder_light=finder_light, finder_dark=finder_dark,
                            separator=separator,
                            version_dark=version_dark,
                            version_light=version_light,
                            quiet_zone=quiet_zone,
                            border=border)



@qrcode_blueprint.route('/wifiqr', methods=['GET', 'POST'])
def wifi_qr():
    flash("not")
    form = BasicQR()
    ssid = "MYWIFINAME"
    password = "***********"
    security = "WPA"
    scale = 4
    format="png"
    if form.is_submitted():
        ssid = form.ssid.data
        password = form.password.data
        security = form.security.data
        format = form.format.data
        scale = form.size.data
        flash("pressed")
    if scale=="":
        scale=4
    
    session['dict'] = {'ssid' : ssid, 'scale' : int(scale),
        'micro' : None,
        'password' : password,
        'security' : security,
        'format' : format, 
        }

    config = helpers.make_wifi_data(ssid=ssid, password=password, security='WPA')
    qr = segno.make(config, error='h')
    return render_template('wifiqr.html', form=form, qr=qr, ssid=ssid, password=password, security=security, scale=int(scale), format=format)


@qrcode_blueprint.route('/imageqr', methods=['GET', 'POST'])
def image_qr():
    flash("not")
    form = BasicQR()
    if form.is_submitted():
        flash("pressed button")
    return render_template('imageqr.html', form=form)

@qrcode_blueprint.route('/download-wifiqr/')
def download_wifiqr():  
    #running this on qrcode/basicqr/download let qr-code download
    #url="www.myexample.org"
    dict = session['dict']
    config = helpers.make_wifi_data(ssid=dict['ssid'], password=dict['password'], security=dict['security'])
    qr = segno.make(config, error='h')

    if dict["format"]=="png":
        data_uri = qr.png_data_uri( 
            scale=dict['scale'])
        header, encoded = data_uri.split(",", 1)
        encoded = b64decode(encoded)
        # make downloadable
        response = make_response(encoded)
        cd = 'attachment; filename=mywifiqr.png'
        response.headers['Content-Disposition'] = cd 
        response.mimetype='image/png'
    elif dict["format"]=="svg":
        data_uri = qr.png_data_uri( 
                scale=dict['scale'])
        header, encoded = data_uri.split(",", 1)
        encoded = b64decode(encoded)
        # make downloadable
        response = make_response(encoded)
        cd = 'attachment; filename=mywifiqr.svg'
        response.headers['Content-Disposition'] = cd 
        response.mimetype='image/svg'
    else:
        pass #throw an error

    return response


@qrcode_blueprint.route('/download/')
def download_qr():  
    #running this on qrcode/basicqr/download let qr-code download
    #url="www.myexample.org"
    dict = session['dict']
    qr = segno.make(dict["url"], micro=dict['micro'], error=dict['error'])
    if dict["format"]=="png":
        data_uri = qr.png_data_uri( dpi=dict['dpi'],
            data_light=dict['data_light'], data_dark=dict['data_dark'],
            dark=dict['dark'], light=dict['light'], alignment_dark=dict['alignment_dark'], alignment_light=dict['alignment_light'],
            finder_light=dict['finder_light'], finder_dark=dict['finder_dark'], 
            version_dark=dict['version_dark'], version_light=dict['version_light'],
            quiet_zone=dict['quiet_zone'], separator=dict['separator'],
            border=dict['border'], 
            scale=dict['scale'])
        header, encoded = data_uri.split(",", 1)
        encoded = b64decode(encoded)
        # make downloadable
        response = make_response(encoded)
        cd = 'attachment; filename=myqr.png'
        response.headers['Content-Disposition'] = cd 
        response.mimetype='image/png'

    elif dict["format"]=="svg":
        data_uri = qr.svg_data_uri( 
            data_light=dict['data_light'], data_dark=dict['data_dark'],
            dark=dict['dark'], light=dict['light'], alignment_dark=dict['alignment_dark'], alignment_light=dict['alignment_light'],
            finder_light=dict['finder_light'], finder_dark=dict['finder_dark'], 
            version_dark=dict['version_dark'], version_light=dict['version_light'],
            quiet_zone=dict['quiet_zone'], separator=dict['separator'],
            border=dict['border'], 
            scale=dict['scale'])

        header, encoded = data_uri.split(",", 1)
        #encoded = b64decode(encoded)
        # make downloadable
        response = make_response(encoded)
        cd = 'attachment; filename=myqr.svg'
        response.headers['Content-Disposition'] = cd 
        response.mimetype='image/svg'
    else:
        pass #throw an error

    return response

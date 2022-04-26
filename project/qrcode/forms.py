from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class BasicQR(FlaskForm):
    '''
    Form Class for basic QR-code parameters.
    '''
    qr_content = StringField('Your QR-Code Content')
    size = StringField("Size")
    error = SelectField('Error Tolerance', choices=[('L', 'low'), ('M', 'medium'), ('Q', 'high'), ('H', 'very high')])
    format = SelectField('Image Format', choices=[('png', 'png'), ('svg', 'svg'), ('jpg', 'jpg')])

    submit = SubmitField('Create')

class DownloadQR(FlaskForm):
    '''
    Form Class for Download QR.
    '''
    submit = SubmitField('Download')
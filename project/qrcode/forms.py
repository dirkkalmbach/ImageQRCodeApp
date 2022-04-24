from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class BasicQR(FlaskForm):
    '''
    Form Class for basic QR-code parameters.
    '''
    qr_content = StringField('Your QR-Code Content')
    size = StringField("Size")
    error = SelectField('Error Tolerance', choices=[('L', 'low'), ('M', 'medium'), ('Q', 'high'), ('H', 'very high')])
    #scale = SelectField('Size', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

    submit = SubmitField('Create')
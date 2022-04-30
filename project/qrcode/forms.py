from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, RadioField
from wtforms.widgets.html5 import ColorInput
from wtforms.validators import InputRequired, Length

class BasicQR(FlaskForm):
    '''
    Form Class for basic QR-code parameters.
    '''
    qr_content = StringField('Your QR-Code Content')
    size = StringField("Size")
    error = SelectField('Error Tolerance', choices=[('L', 'low'), ('M', 'medium'), ('Q', 'high'), ('H', 'very high')])
    format = SelectField('Image Format', choices=[('png', 'png'), ('svg', 'svg'), ('jpg', 'jpg')])
    dpi = IntegerField("Resolution") #🧐 this field stops showing qr-codes
    border = IntegerField("Frame Size")
    submit = SubmitField(label='Create')
    test = StringField("test")
    mask = SelectField('Mask Format', choices=[("99", 'let computer find best pattern'),("0", 'pattern 00'), ("1", 'mask pattern 01'), ("2", 'mask pattern 10')])
    ssid = StringField('SSID', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    password = StringField('password', validators=[InputRequired(),
                                             Length(min=4, max=63)])
    security = SelectField('Security', choices=[("WPA", 'WPA'),("WEP", 'WEP'), ("nopass", "I don't know")])

    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])


class ColoursForm(FlaskForm):
    """Used when editing scoreboard colours"""
    dark_color = StringField(widget=ColorInput(), label="dark")
    light_color = StringField(widget=ColorInput(), label="light")
    data_light = StringField(widget=ColorInput(), label="data light")
    data_dark = StringField(widget=ColorInput(), label="data dark")
    quiet_zone = StringField(widget=ColorInput(), label="quiet zone")
    alignment_light = StringField(widget=ColorInput(), label="alignment_light")
    alignment_dark = StringField(widget=ColorInput(), label="alignment_dark")
    finder_light = StringField(widget=ColorInput(), label="outer squares (foreground)")
    finder_dark = StringField(widget=ColorInput(), label="outer squares (background)")
    separator = StringField(widget=ColorInput(), label="seperator")
    version_light = StringField(widget=ColorInput(), label="version_light")
    version_dark = StringField(widget=ColorInput(), label="version_dark")


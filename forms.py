from wtforms import Form, StringField, TextField, PasswordField, HiddenField
from wtforms.fields.html5 import EmailField

def length_honeypot(form, field):
  if (len(field.data) > 0):
    raise validators.ValidationError('El campo debe estar vacio')

class Formulario(Form):
  Rname = TextField('Nombre')
  RlastName = TextField('Apellido')
  Remail = EmailField('Correo')
  Rpass = PasswordField('Contraseña')
  RCpass = PasswordField('Repetir contraseña')
  email = EmailField('Correo')
  password = PasswordField('Contraseña')
  honeypot = HiddenField('', [length_honeypot])
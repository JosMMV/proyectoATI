from wtforms import Form, StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField

class Formulario(Form):
  Rname = TextField('Nombre')
  RlastName = TextField('Apellido')
  Remail = EmailField('Correo')
  Rpass = PasswordField('Contraseña')
  RCpass = PasswordField('Repetir contraseña')
  email = EmailField('Correo')
  password = PasswordField('Contraseña')
  
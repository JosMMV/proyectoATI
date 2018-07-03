from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash
from pymongo import *
import forms
from flask_wtf.csrf import CSRFProtect
 
app = Flask(__name__, template_folder = 'templates', static_folder = 'static')
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

# MongoDB Connection with PyMongo
client = MongoClient()

db = client.proyectoATI
usuarios = db.user
imagenes = db.image

# Routes Definition
@app.route('/')
def index():
	users = usuarios.aggregate([
	{"$match":
		{
			"conf": True
		}

	},
  {"$lookup":
    {
      "from": "image",
      "localField": "images._id_image",
      "foreignField": "_id_image",
      "as": "user_images"
    }
  }
	])
	return render_template('index.html', usuarios = users)

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
	return redirect(url_for('login'))

@app.route('/login')
def login():
	if 'username' in session:
		return redirect(url_for('home'))
	else:
		form = forms.Formulario()
		return render_template('login.html', form = form)

@app.route('/register', methods = ['POST'])
def register():
	name = request.form['Rname']
	last_name = request.form['RlastName']
	email = request.form['Remail']
	password = request.form['Rpass']
	maxs_id = usuarios.find({},{"_id_user":1}).sort([("_id_user",-1)]).limit(1)
	max_id = maxs_id[0]["_id_user"]
	max_id += 1
	usr = {"_id_user":max_id, "first_name":name, "last_name":last_name, "email":email, "password":password}
	usuarios.insert(usr)
	session['username'] = email
	return redirect(url_for('home'))

@app.route('/logon', methods=['POST'])
def logon():
	form = forms.Formulario(request.form)
	email = form.email.data
	password = form.password.data
	usr = usuarios.find_one({ "email": email })
	if usr:
		if usr["password"] == password:
			session['username'] = email
			return redirect(url_for('home'))
	flash('Ha ingresado sus datos incorrectos. Favor intente nuevamente.')
	return redirect(url_for('login'))

@app.route('/home', methods=['POST','GET'])
def home():
	if 'username' in session:
		username = session['username']
		users = usuarios.aggregate([
		{"$lookup":
			{
				"from": "image",
				"localField": "images._id_image",
				"foreignField": "_id_image",
				"as": "user_images"
			}
		}
		])
		return render_template('index.html', usr = username, loged = True, usuarios = users)
	else:
		users = usuarios.aggregate([
		{"$match":
			{
				"conf": True
			}

		},
		{"$lookup":
			{
				"from": "image",
				"localField": "images._id_image",
				"foreignField": "_id_image",
				"as": "user_images"
			}
		}
		])
		return render_template('index.html', usuarios = users)

@app.route('/profile')
def photos():
	if 'username' in session:
		username = session['username']
		print (username)
		user = usuarios.aggregate([
		{"$match":
			{
				"email": username
			}
		},
		{"$lookup":
			{
				"from": "image",
				"localField": "images._id_image",
				"foreignField": "_id_image",
				"as": "user_images"
			}
		}
		])
		new_user = list(user)
		print (new_user[0]["first_name"])
		print (new_user)
		return render_template('photos.html', user = new_user)

if __name__ == '__main__':
	app.debug = True
	app.run()
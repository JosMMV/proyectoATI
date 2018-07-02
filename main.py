from flask import Flask, render_template, request
from pymongo import *
import forms
 
app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

# MongoDB Connection with PyMongo
client = MongoClient()

db = client.proyectoATI
usuarios = db.user
imagenes = db.image

# Routes Definition
@app.route('/')
def index():
	form = forms.Formulario()
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
	return render_template('login.html', usuarios = users, form = form)

@app.route('/login')
def login():
	return render_template('login.html')

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
	return render_template('index.html', usr = usr, loged = True)

@app.route('/home', methods=['POST'])
def home():
	email = request.form['email']
	password = request.form['password']

	usr = usuarios.find_one({ "email": email })
	if usr:
		if usr["password"] == password:
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
			return render_template('index.html', usr = usr, loged = True, usuarios = users)
	form = forms.Formulario()
	return render_template('login.html', error = True, form = form)

@app.route('/photos')
def photos():
	users = request.args.get('usuarios','none')
	usr = request.args.get('usuario','none')
	return render_template('photos.html',usr = usr, usuarios = users)

if __name__ == '__main__':
	app.debug = True
	app.run()
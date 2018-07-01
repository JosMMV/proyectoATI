from flask import Flask, render_template, request
from pymongo import *
 
app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

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
	return render_template('login.html', usuarios = users)

@app.route('/login')
def login():
	return render_template('login.html')

#@app.route('/register', methods = ['POST'])
#def register():
	

@app.route('/home', methods=['POST'])
def home():
	user = request.form['email']
	password = request.form['pass']

	usr = usuarios.find_one({ "user_name": user })
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
	return render_template('login.html', error = True)


if __name__ == '__main__':
	app.debug = True
	app.run()
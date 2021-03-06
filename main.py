from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash
from pymongo import *
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
import forms
import facebook
import tweepy
 
app = Flask(__name__, template_folder = 'templates', static_folder = 'static')
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

#-----------Twitter-----------------------
CONSUMER_KEY = '7ZuCuDzEhVOFc9EWcHSJ4UMu'
CONSUMER_SECRET = 'F3pxpMu0YuNB6s19tspeEeU5SfSwRYCwkleVPdshYyixw7xF8Z'
ACCESS_TOKEN = '815655552-icBvaDwQiPUw9ujidRj9jJ4vlWa4dOyAF75pnOzj'
ACCESS_TOKEN_SECRET = '0q5sBtP7DMEmZ1lnykU114ApD7pnX4kyB1FgnGscv8l4G'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = None

# MongoDB Connection with PyMongo
client = MongoClient()

db = client.proyectoATI
usuarios = db.user
imagenes = db.image

# Routes Definition

@app.route('/twitter',methods=['POST'])
def twitter_login():
	global api
	api = tweepy.API(auth)
	user = api.me()
	return user.screen_name

@app.route('/t_login', methods=['POST'])
def t_login():
	userT  = request.form['userNameT']

	#Iniciamos con Twitter
	user = usuarios.find_one({ "userNameT": userT })

	if user is None:
		return render_template('index.html', error = 5, data = newPost("Publico",None))
	else:
		session['username'] = user['userName']
		session['nombre'] = user["nombre"]+" "+user["apellido"]
		return render_template('inicio.html', user = session['nombre'], data = newPost(None,user["userName"]))

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
	validate_user = usuarios.find_one({"email":email})
	if validate_user:
		flash('El correo suministrado ya se encuentra registrado.')
		return redirect(url_for('login'))
	else:
		maxs_id = usuarios.find({},{"_id_user":1}).sort([("_id_user",-1)]).limit(1)
		max_id = maxs_id[0]["_id_user"]
		max_id += 1
		passwordHashed = generate_password_hash(password)
		usr = {"_id_user":max_id, "first_name":name, "last_name":last_name, "email":email, "password":passwordHashed}
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
		if check_password_hash(usr["password"], password):
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
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.debug = True
	app.run()
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image


app = Flask(__name__)

# routes
@app.route("/", methods=['GET', 'POST'])
def kuch_bhi():
	img_path_1 = 'static/cat.jpg'
	img_path_2 = 'static/dog.jpg'
	return render_template("home.html", img_path_1 = img_path_1, img_path_2 = img_path_2)

if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
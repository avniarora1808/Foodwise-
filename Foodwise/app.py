# Import libraries
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from tempfile import mkdtemp
from training import predict
from recipe_api import get_recipe
from nlp import extract
import sys
import os

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template('about.html')

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        #print('get filesss')
        uploaded_file = request.files['file']
        bytes_string = uploaded_file.read()
        value = predict(bytes_string, uploaded_file.filename)
        #print(value)
        session["prediction"] = value
        #print(session["prediction"])
        return render_template("prediction.html", 
                in1 = value[0], in2 = value[1], in3 = value[2], in4 = value[3], in5 = value[4])
    else:
        # return render_template("recipe.html")
        return render_template("prediction.html")

@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    if request.method == "POST":
        five_ingredients = []
        for i in range(1, 6):
            if request.form.get(str(i)):
                five_ingredients.append(request.form.get(str(i)))
        #print(five_ingredients)
        value = get_recipe(five_ingredients)
        return render_template("results.html", recipe=value)
    else:
        return render_template("recipe.html")

@app.route("/results", methods=["GET","POST"])
def results():
    if request.method == "POST":
        return render_template("results.html")
    else: 
        return render_template("results.html")

@app.route("/result2", methods=["GET","POST"])
def results2():
    if request.method == "POST":
        return render_template("results.html")
    else:
        arr = session["prediction"]
        #print("Value is", arr)
        value = get_recipe(arr)
        #print(value)
        return render_template("results.html", recipe=value)

@app.route("/nlp", methods=["GET","POST"])
def nlp():
    if request.method == "POST":
        #print(request.form['paragraph_text'])
        str = request.form['paragraph_text']
        # Vectorization (removing punctuation)
        for char in str:
            if char in "?.!/;:":
                str = str.replace(char, '')
        #print(str)
        freq = extract(str) # Extract keywords from NLP and cleanse keywords
        freq = freq[:3] # Number of keywords taken (highest predictio nvalue)
        value = get_recipe(freq)
        return render_template("results.html", recipe=value)
    else:
        return render_template("results.html")

if __name__ == '__main__':
    # Make sure to specify host for Azure and port in .env
    app.run(host="0.0.0.0", port=os.environ.get("PORT") if os.environ.get("PORT") else 80, debug=True)

#using html templates in flask
#lets import flask
from flask import Flask
#Lets import render_template also
from flask import render_template
#Let create new app
app = Flask(__name__)
#Lets create new route
@app.route('/')
#Lets create a function
def index():

    return render_template('index.html')
    #Lets create a template folder and index.html file but first
    # complete this program

app.run(debug=True, port=8080)

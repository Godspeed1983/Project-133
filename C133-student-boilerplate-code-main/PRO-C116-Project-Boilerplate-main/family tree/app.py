# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Abc" # write your name
    age = "22" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def a():

    name = "Abc" # write your name
    age = "22" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def b():

    name = "Abc" # write your name
    age = "22" # write your age

    return render_template('mother.html' , name = name , age = age)
# define the route to friends webpage
@app.route("/friend")
def c():

    name = "Abc" # write your name
    age = "22" # write your age

    return render_template('friend.html' , name = name , age = age)
# add other routes, if you want



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

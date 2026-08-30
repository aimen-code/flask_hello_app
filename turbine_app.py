from flask import Flask, render_template
from flask import request

app = Flask(__name__)

user = {"password": "admin"}

@app.route('/')

def home():

    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])

def login():

    if request.method == 'POST':

        password = request.form['password']

        if password == user['password']:

            return render_template('home.html')
        
        else:

            return render_template('login.html',message="Invalid password")
    return render_template('login.html')

if __name__ == '__main__':
    
    app.run ( debug=True ,  host='0.0.0.0',port=4000)
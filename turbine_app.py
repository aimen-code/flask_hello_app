from flask import Flask, render_template

from flask import request,redirect,url_for,session

import os

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("secret_key")

user = {"password": "admin"}



@app.route('/login', methods=['get','POST'])

def login():

    if session.get('logged in'):
                
        return redirect(url_for('home'))

    
    if request.method == 'POST':

        password = request.form['password']

        if password == user['password']:

            session['logged in'] = True

            return redirect(url_for('home'))
        
        else:

            return render_template('login.html',message="Invalid password")
        
    
        
    return render_template('login.html')

    

        

@app.route('/home')

def home():

    if not session.get('logged in'):

        return redirect(url_for('login'))
    
    return render_template('home.html')

@app.route('/logout')

def logout():

    session.clear()

    return redirect(url_for('login'))


if __name__ == '__main__':
    
    app.run ( debug=True ,  host='0.0.0.0',port=4000)
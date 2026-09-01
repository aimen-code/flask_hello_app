from flask import Flask, render_template
from flask import request,redirect,url_for

app = Flask(__name__)

user = {"password": "admin"}

# @app.route('/')
# def index():
#     return render_template('login.html')

@app.route('/login', methods=['get','POST'])

def login():

    if request.method == 'POST':

        password = request.form['password']

        if password == user['password']:

            return redirect(url_for('home'))
        
        else:

            return render_template('login.html',message="Invalid password")
    return render_template('login.html')

@app.route('/home')

def home():

    return render_template('home.html')



if __name__ == '__main__':
    
    app.run ( debug=True ,  host='0.0.0.0',port=4000)
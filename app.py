from flask import Flask, redirect, request,url_for,render_template, sessions
from datetime import timedelta
app = Flask(__name__,template_folder=templates)

app.secret_key='blabla'
app.permanent_session_lifetime= timedelta(minutes=3)

@app.route('/registration', methods = ['POST','GET'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        mail = request.form['mail']
        password = request.form['password']
        return render_template('registration.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        mail = request.form['mail']
        password = request.form['password']
        user = request.form['nameuser']
        sessions['user']= user
        return redirect(url_for('user'))
    else:
        if 'user' in sessions:
            return redirect(url_for('user'))

    return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in sessions:
        user = sessions['user']
        return f"hello{user}"


if __name__ == '__main__':
    app.run()

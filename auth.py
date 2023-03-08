from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', '__name__')


@auth.route('/login', methods=['POST', 'GET'])
def login():
  data = request.form
  return render_template("login.html")


@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
  if (request.form == 'POST'):
    email = request.form.get('email')
    psw = request.form.get('password')
    psw2 = request.form.get('psw-repeat')

    if ('@' not in email):
      flash('Email is not valid', category='e')
    elif (psw != psw2):
      flash('Must have same password', category='e')
    else:
      flash('Acount created!', category='s')
  return render_template("signup.html")


@auth.route('/logout')
def logout():
  return "<h1>logout</h>"

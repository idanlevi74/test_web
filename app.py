from flask import Flask, render_template
from views import views
from auth import auth

app = Flask(__name__)

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
##############################################################
"""
#from .views import views
#from .auth import auth
app = Flask(__name__)


#app.register_blueprint(views, url_prefix='/')
#app.register_blueprint(auth, url_prefix='/')


@app.route("/")
def hll():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

"""

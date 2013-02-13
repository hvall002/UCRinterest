import flask
import settings

#Views
from main import Main
from login import Login
from remote import Remote
from interests import Interests
from userprofile import userProfile
from upload import Upload

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Different routes listed here
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                methods=['GET'])
#Specify URL path ( <page> )
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=['GET', 'POST'])
app.add_url_rule('/interests/',
                 view_func=Interests.as_view('interests'),
                 methods=['GET', 'POST'])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                methods=['GET', 'POST'])
#app.add_url_rule('/upload/',
#                 view_func=Upload.as_view('upload'),
#                methods=['GET', 'POST'])
app.add_url_rule('/userProfile/',
                 view_func=userProfile.as_view('userProfile'),
                methods=['GET'])

# handle 404 errors
#   renders 404 html page and returns the error
@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
app.run()
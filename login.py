import flask, flask.views

users = {'pinterest':'cs180',
         'eddie':'pokemon',
         'porygon':'digital8'}

    
class Login(flask.views.MethodView):
    def get(self):
        return flask.render_template('login.html')
    
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('login'))
        required = ['username', 'passwd', 'gender', 'birthday']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('login')) #send user to different path
        username = flask.request.form['username']
        gender = flask.request.form['gender']
        birthday = flask.request.form['birthday']
        passwd = flask.request.form['passwd']
        if username in users and users[username] == passwd:
            flask.session['username'] = username
            flask.session['passwd'] = passwd
            flask.session['gender'] = gender
            flask.session['birthday'] = birthday
            #
            return flask.redirect(flask.url_for('interests'))
            #
        else:
            flask.flash("Incorrect username/password")
        return flask.redirect(flask.url_for('login'))

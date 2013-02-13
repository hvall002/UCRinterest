import flask, flask.views

class Interests(flask.views.MethodView):
    def get(self):
        return flask.render_template('interests.html')
    
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('index'))
        required = ['inter1', 'inter2', 'inter3', 'inter4', 'inter5']
        inter1 = flask.request.form['inter1']
        inter2 = flask.request.form['inter2']
        inter3 = flask.request.form['inter3']
        inter4 = flask.request.form['inter4']
        inter5 = flask.request.form['inter5']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('interests')) #send user to different path
        flask.session['inter1'] = inter1
        flask.session['inter2'] = inter2
        flask.session['inter3'] = inter3
        flask.session['inter4'] = inter4
        flask.session['inter5'] = inter5
        return flask.redirect(flask.url_for('interests'))
import flask, flask.views
import os

class Upload(flask.views.MethodView):
    def get(self):
        return flask.render_template('upload.html')
    
    def post(self):
        filename = photos.save(request.files['photos'])
        rec = Photo(filename=filename, user=g.user.id)
        rec.store()
        flash("Photo has been uploaded.")
        return flask.redirect(flask.url_for('upload'))
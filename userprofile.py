import flask, flask.views
import os

class userProfile(flask.views.MethodView):
    def get(self):
        return flask.render_template('userProfile.html')
    


#import flask, flask.views, jinja2
#import os
#from jinja2 import Environment, PackageLoader
#
#env = Environment(autoescape=True,
#    loader=jinja2.FileSystemLoader('templates'))
#
#class userProfile(flask.views.MethodView):
#    def get(self):
#        names = { 'first': 'This is a new title', 'second': 'Second title'}
#        arrays={
#            'myheader': 'This is the first title',
#            'title': names
#        }
#        template = env.get_template('userProfile.html')
#        #self.response.out.write(template.render(template_values))
#        return flask.render_template(arrays)
import cgi
import json
import datetime
import urllib
import webapp2
import logging
	
from google.appengine.ext import db
from google.appengine.api import users

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Feedback(db.Model):
  reserved = db.IntegerProperty()
  unit = db.StringProperty()
  runid = db.StringProperty()
  author = db.StringProperty()
  browser = db.StringProperty()
  timestamp = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            self.redirect('/menu')
        else:
            self.redirect('/login')

class Login(webapp2.RequestHandler):
    def get(self):
        url = users.create_login_url('/')

        template_values = {
          'url': url
        }
        
        template = jinja_environment.get_template('templates/login.html')
        self.response.out.write(template.render(template_values))

class Menu(webapp2.RequestHandler):
    def get(self):
            template_values = {
            }
         
            template = jinja_environment.get_template('templates/menu.html')
            self.response.out.write(template.render(template_values))

class Filler(webapp2.RequestHandler):
    def get(self):
            template_values = {
            }
         
            template = jinja_environment.get_template('templates/filler.html')
            self.response.out.write(template.render(template_values))
        

class Stats(webapp2.RequestHandler):
    def get(self):

        feedbacks = Feedback.all()
 
        template_values = {
            'feedbacks': feedbacks
        }

        template = jinja_environment.get_template('templates/stats.html')
        self.response.out.write(template.render(template_values))


class Heartbeat(webapp2.RequestHandler):
    def post(self):
        fb = Feedback()
        args = json.loads(self.request.body)
        fb.reserved = args['reserved']
        fb.unit = args['unit']
        fb.runid = args['runid']
        fb.author = users.get_current_user().user_id()
        fb.browser = self.request.headers.get('user_agent')
        fb.put()

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/login', Login),
                               ('/menu', Menu),
                               ('/filler', Filler),
                               ('/stats', Stats),
                               ('/heartbeat', Heartbeat)],
                              debug=True)

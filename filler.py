import cgi
import datetime
import urllib
import webapp2
	
from google.appengine.ext import db
from google.appengine.api import users

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

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

        # TODO: get data from db and show it on the page

        template_values = {
        }

        template = jinja_environment.get_template('templates/stats.html')
        self.response.out.write(template.render(template_values))


class Heartbeat(webapp2.RequestHandler):
  def post(self):
    pass # TODO: process heartbeat and show data

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/login', Login),
                               ('/menu', Menu),
                               ('/filler', Filler),
                               ('/stats', Stats),
                               ('/heartbeat', Heartbeat)],
                              debug=True)

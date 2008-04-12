#!/usr/bin/env python
"""
First file for "The Firm" - a web-based game where you try and build an
IT consulting company.
"""

import os
import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

# Switch this sometime, when we're done
DEBUG = True

class OurRequestHandler(webapp.RequestHandler):
    """
    Our version of the request handler - sets up some basic variables,
    and handles render nicely
    """
    def initialize(self, request, response):
        """
        Setup variables on self that we're likely to want for all requests
        """
        webapp.RequestHandler.initialize(self, request, response)
        self.args = {
            'user' : users.get_current_user(),
            'request' : self.request,
        }
        
    def render(self, templateName):
        """
        Render the appropriate template with args
        """
        path = os.path.dirname(__file__)
        templateName = os.path.join(path, '..', 't', templateName)
        return self.response.out.write(template.render(templateName, self.args))

class MainPage(OurRequestHandler):
    def get(self):
        """ Main page """
        self.render('index.html')

def main():
    app = webapp.WSGIApplication([('/', MainPage),], debug=DEBUG)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()

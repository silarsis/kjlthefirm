#!/usr/bin/env python
"""
First file for "The Firm" - a web-based game where you try and build an
IT consulting company.
"""

import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('Hello %s' % user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

def main():
    app = webapp.WSGIApplication([('/', MainPage),], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()

"""
Classes to define people and companies - operating entities

Created by Kevin Littlejohn on 2008-04-12.
Copyright (c) 2008 Obsidian Consulting Group. All rights reserved.
"""

from google.appengine.ext import db

class Company(db.Model):
    """ Companies, the base trading entity, made up of people """
    name = db.StringProperty(required=True)
    # Remember, there's a self.Person_set that gives all people
    def delete(self):
        """ Only delete if the people have gone """
        if self.Person_set:
            raise KeyError("Cannot delete until all members are removed")
        return db.Model.delete(self)

class Person(db.Model):
    """ The very model of a modern major *ahem* """
    user = db.UserProperty(required=True)
    name = db.StringProperty(required=True)
    company = db.ReferenceProperty(reference_class=Company)

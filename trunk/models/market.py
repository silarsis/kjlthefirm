"""
Classes to define the marketplaces and their participants

Created by Kevin Littlejohn on 2008-04-12.
Copyright (c) 2008 Obsidian Consulting Group. All rights reserved.
"""

from google.appengine.ext import db
from models.person import Company

class Tender(db.Model):
    """ Tenders, requests for work """
    name = db.StringProperty(required=True)
    origin = db.ReferenceProperty(reference_class=Company)
    state = db.CategoryProperty(required=True,
        choices=['advertised', 'decided', 'awarded', 'withdrawn'])
    adDeadline = db.DateProperty()
    decideDeadline = db.DateProperty()
    completeDeadline = db.DateProperty()

class Market(db.Model):
    """ A marketplace, where tenders are advertised """
    name = db.StringProperty(required=True)
    def delete(self):
        """ Remove everyone from the market then delete """
        for mpart in self.MarketParticipants_set:
            mpart.delete()
        for tpart in self.MarketTenders_set:
            tpart.delete()

class MarketContents(db.Model):
    """ Many to Many relationship between markets and tenders """
    market = db.ReferenceProperty(required=True, reference_class=Market)
    tender = db.ReferenceProperty(required=True, reference_class=Tender)

class MarketParticipants(db.Model):
    """ Many to Many relationship between markets and companies """
    market = db.ReferenceProperty(required=True, reference_class=Market)
    company = db.ReferenceProperty(required=True, reference_class=Company)
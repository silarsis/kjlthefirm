"""
Classes to define skills held by people and required by tenders

Created by Kevin Littlejohn on 2008-04-12.
Copyright (c) 2008 Obsidian Consulting Group. All rights reserved.
"""

from google.appengine.ext import db
from models.person import Person
from models.market import Tender

class Skill(db.Model):
    """ Tenders, requests for work """
    name = db.StringProperty(required=True)
    category = db.CategoryProperty(required=True,
        choices=['WebFramework', 'Language', 'OS', 'Database'])
    def delete(self):
        """ Remove all references to this skill """
        for pskill in self.PersonSkill_set:
            pskill.delete()
        for tskill in self.TenderSkill_set:
            tskill.delete()

class PersonSkill(db.Model):
    """ Many to Many relationship between people and skills """
    person = db.ReferenceProperty(required=True, reference_class=Person)
    skill = db.ReferenceProperty(required=True, reference_class=Skill)
    level = db.RatingProperty()

class PersonSkill(db.Model):
    """ Many to Many relationship between tenders and skills """
    tender = db.ReferenceProperty(required=True, reference_class=Tender)
    skill = db.ReferenceProperty(required=True, reference_class=Skill)
    level = db.RatingProperty()
    time = db.IntegerProperty(required=True)
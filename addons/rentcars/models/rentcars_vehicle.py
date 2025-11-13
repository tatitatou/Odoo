#-*- coding: utf-8 -*-

from odoo import fields, models

class Vehicle(models.Model):
    _name = 'rentcars.vehicle'
    _description = 'Description of vehicle'

    active=fields.Boolean("Actif ?", default=True)

    immatriculation = fields.Char("Numberplate")
    date_purchased = fields.date(string="Purchase date")
    model = fields.Char("Model")
    thumbnail = fields.Binary("Thumbnail")
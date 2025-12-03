# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Option(models.Model):
     _name = 'rentcars.option'
     _description = 'Options of vehicle'
     active=fields.Boolean("Actif ?", default=True)
     name = fields.Char("Name")
     category = fields.Selection([("security", "security"), ("comfort", "comfort"), ("aestheticism", "aestheticism")])
     description= fields.Char("Description")
     vehicle_ids = fields.Many2many(comodel_name="rentcars.vehicle",relation="rentcars_vehicle_rentcars_option_rel",column1="vehicle_id",column2="option_id", string="Vehicle With option")

#-*- coding: utf-8 -*-

from odoo import fields, models, api
import re
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class Vehicle(models.Model):
    _name = 'rentcars.vehicle'
    _description = 'Description of vehicle'

    active=fields.Boolean("Actif ?", default=True)

    immatriculation = fields.Char("Numberplate")
    date_purchased = fields.Date(string="Purchase date")
    model = fields.Char("Model")
    thumbnail = fields.Binary("Thumbnail")

    garage_id = fields.Many2one("rentcars.garage",string="garage")
    option_ids = fields.Many2many("rentcars.option",string="Option of vehicle")
    
    age_vehicle = fields.Integer(compute="_age_vehicle", string="Age of vehicle (years)")
    
    def _check_immatriculation(self):
        self.ensure_one()
        pattern = re.compile("\w{2}[0-9]{3}\w{2}$")
        return pattern.match(self.immatriculation)
    
    def button_check_immatriculation(self):
        for vehicle in self:
            if not vehicle.immatriculation:
                raise (ValidationError("Please provide a numberplate for this car"))
            if vehicle.immatriculation and not vehicle._check_immatriculation():
                raise ValidationError("%s Numberplate is invalid" % (vehicle.immatriculation))
        return True
    
    @api.depends('date_purchased')
    def _age_vehicle(self):
        for vehicle in self:
            TODAY = date.today()
            vehicle.age_vehicle=relativedelta(TODAY,vehicle.date_purchased).years
            
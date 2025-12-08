from odoo import models, fields

class Salle(models.Model):
    _name = 'ecole.salle'
    _description = 'Salle'

    code = fields.Char(string="Code", required=True)
    salle = fields.Char(string="Salle")
    bloc = fields.Char(string="Bloc")

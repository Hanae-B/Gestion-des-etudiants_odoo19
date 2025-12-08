from odoo import models, fields

class Module(models.Model):
    _name = 'ecole.module'
    _description = 'Module'

    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="NomModule", required=True)
    description = fields.Text(string="Description")

    filiere_id = fields.Many2one('ecole.filiere', string="Filière")
    salle_id = fields.Many2one('ecole.salle', string="Salle")


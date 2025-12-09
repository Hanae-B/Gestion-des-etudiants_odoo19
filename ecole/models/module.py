from odoo import models, fields

class Module(models.Model):
    _name = 'ecole.module'
    _description = 'Modèle pour la gestion des modules'

    _rec_name = 'NomModule'
    ID_Module = fields.Integer(string="ID Module")
    codeModule = fields.Char(string="Code Module")
    NomModule = fields.Char(string="Nom du Module", required=True)
    
    description = fields.Text(string="Description")
    filiere_id = fields.Many2one('ecole.filiere', string="Filière")
    salle_id = fields.Many2one('ecole.salle', string="Salle")

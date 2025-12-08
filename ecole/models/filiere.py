from odoo import models, fields

class Filiere(models.Model):
    _name = 'ecole.filiere'
    _description = 'Filière'

    name = fields.Char(string="Intitulé", required=True)
    code = fields.Char(string="Code")
   # Code temporaire pour débloquer la base
    cycle = fields.Selection([('Ingénieur', 'Ingénieur'), ('Préparatoire', 'Préparatoire')], string="Cycle")
    etudiant_ids = fields.One2many('ecole.etudiant', 'filiere_id', string="Étudiants")
    module_ids = fields.One2many('ecole.module', 'filiere_id', string="Modules")
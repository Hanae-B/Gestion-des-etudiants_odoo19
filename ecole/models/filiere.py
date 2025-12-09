from odoo import models, fields

class Filiere(models.Model):
    _name = 'ecole.filiere'
    _description = 'Modèle pour la gestion des filières'

    _rec_name = 'intitule'
    ID_filiere = fields.Integer(string="ID Filière")
    intitule = fields.Char(string="Intitulé", required=True)
    code = fields.Char(string="Code Filière")
    cycle = fields.Char(string="Cycle", default='Ingénieur', readonly=True)

    def changerCycle(self):
        for record in self:
            if record.cycle == 'Ingénieur':
                record.cycle = 'Préparatoire'
            else:
                record.cycle = 'Ingénieur'
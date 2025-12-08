from odoo import models, fields

class Etudiant(models.Model):
    _name = 'ecole.etudiant'
    _description = 'Etudiant'

    num_apogee = fields.Char(string="NuméroApogée", required=True)
    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)

    email = fields.Char(string="Email")
    tel = fields.Char(string="Téléphone")
    ville = fields.Char(string="Ville")
    photo = fields.Binary(string="Photo")

    filiere_id = fields.Many2one('ecole.filiere', string="Filière")

from odoo import models, fields

class EnsahEmployee(models.Model):
    _name = 'ensah.employee'
    _description = 'Ensah Employee'
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prenom', required=True)
    matricule = fields.Char(string='Matricule', required=True)
    fonction = fields.Char(string='Fonction')
    telephone = fields.Char(string='Téléphone')
    adresse = fields.Char(string='Adresse')
    email = fields.Char(string='Email')
    date_embauche = fields.Date(string='Date d\'Embauche')  

    prime_ids = fields.One2many('ensah.prime', 'employee_id', string='Primes')
    conges_ids = fields.One2many('ensah.conge', 'employee_id', string='Congés')

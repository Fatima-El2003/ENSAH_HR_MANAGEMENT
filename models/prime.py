from odoo import models, fields

class EnsahPrime(models.Model):
    _name = 'ensah.prime'
    _description = 'Ensah Prime'

    note_prime = fields.Char(string='Note Prime')
    commentaire = fields.Text(string='Commentaire')
    date = fields.Date(string="Prime Date") 
    trimestre = fields.Integer(string='Trimestre')
    salaire_principal = fields.Float(string='Salaire Principal')
    salaire_brut_mensuel = fields.Float(string='Salaire Brut Mensuel')
    employee_id = fields.Many2one('ensah.employee', string='Employé', required=True)

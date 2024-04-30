# from odoo import models, fields, api


# # membuat menu instruktur dengan id 'insruktur', nama 'Instruktur'
# class Instruktur(models.Model):
#     _name = 'instruktur'
#     _description = 'Instruktur'
#     # pengambilan data partner_id dari 'res.partner'(data modul bawaan dari odoo)
#     _inherits = {'res.partner':'partner_id'}

#     # menjabarkan parter_id, knp m2o? karena data res.partner(banyak/besar) untuk partner_id(diambil 1 data)
#     partner_id = fields.Many2one(comodel_name='res.partner',string='Partner ID',required=True, ondelete='casecade')
#     keahlian_ids = fields.Many2many(comodel_name='keahlian', string='Keahlian')



# class Keahlian(models.Model):
#     _name = 'keahlian'
#     _description = 'Keahlian'

#     name= fields.Char(string="Keahlian",required=True)


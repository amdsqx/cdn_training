from odoo import models, fields, api


# omod shortcut untuk class model
# # class model untuk instruktur
class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'Instruktur'
    # inherits untuk pengambilan data bernama partner_id dari res.partner(bawaan dari modul odoo)
    _inherits = {'res.partner':'partner_id'}

    # extrak partner_id dari inherits res.partner,m2o artinya data banyak diambil sebagian, string 'Partner ID' judul, required=True artinya jika tidak diisi maka error, ondelete='caseade' artinya jika data dihapus maka data induk tidak ikut terhapus
    partner_id = fields.Many2one(comodel_name='res.partner',string='Partner ID',required=True, ondelete='casecade')
    # keahlian_ids diperoleh dari models keahlian & data keahlian diperoleh dari inputan lokal
    keahlian_ids = fields.Many2many(comodel_name='keahlian', string='Keahlian')


# omod shortcut untuk class model
# class model untuk keahlian instruktur dengan nama id 'keahlian' & dengan judul 'Keahlian'
class Keahlian(models.Model):
    _name = 'keahlian'
    _description = 'Keahlian'

    # membuat tabel dengan data lokal dengan tipe data char & berjudul 'Keahlian'
    name= fields.Char(string="Keahlian",required=True)


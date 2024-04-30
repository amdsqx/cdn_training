from odoo import models, fields, api
from datetime import timedelta

# class model untuk training course
class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'tabel Training Course'

    name = fields.Char(string='Nama Kursus')
    keterangan = fields.Text(string='keterangan')
    user_id = fields.Many2one(comodel_name='res.users', string='Penanggung jawab', required=True)
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Session')

    # validasi untuk cek jika nama sudah ada maka tidak bisa membuat data baru dengan nama yang sama
    _sql_constraints = [("name_course_uniq", "uniq(name)", "Data sudah ada!"), ]


# class model untuk training sesi
class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Sesi Training',required=True, tracking=True)
    course_id = fields.Many2one(comodel_name='training.course', string='ID Kursus',required=True, tracking=True)
    start_date = fields.Date(string='Tanggal Mulai',required=True, tracking=True)
    duration = fields.Integer(string='Durasi (day)', tracking=True)
    seets = fields.Integer(string='Jumlah Peserta', required=True, default='1', tracking=True)
    instruktur_id = fields.Many2one(comodel_name='instruktur', string='Nama Instruktur', tracking=True)   
    alamat = fields.Char(string='Alamat', related='instruktur_id.street', tracking=True)
    no_hp = fields.Char(string='No Hp', related='instruktur_id.mobile', tracking=True)
    email = fields.Char(string='Email', related='instruktur_id.email', tracking=True)
    jenis_kel = fields.Selection(string='Jenis Kelamin', related='instruktur_id.jenis_kelamin', tracking=True)
    peserta_ids = fields.Many2many(comodel_name='peserta', string='Peserta', tracking=True)
    jml_peserta = fields.Integer(compute='_compute_jml_peserta', string='Jumlah Peserta', tracking=True)
    state = fields.Selection(string='Status', selection=[('draf', 'Draft'), ('progres', 'Sedang Berlangsung'),('done', 'Selesai')], default='draf',tracking=True)
    end_date = fields.Date(string='End Date', compute='_compute_end_date')


    @api.depends('peserta_ids')
    def _compute_jml_peserta(self):
        for rec in self:
            rec.jml_peserta = len(rec.peserta_ids)



    def action_konfirmasi(self):
        self.state='progres'

    def action_selesai(self):
        self.state='done'

    def action_draf(self):
        self.state='draf'

    def action_konfirmasi(self):
        self.state='progres'

    def action_selesai(self):
        self.state='done'

    def action_draf(self):
        self.state='draf'

    @api.depends('start_date','duration')
    def _compute_end_date(self):
        for rec in self:
            rec.end_date =  rec.start_date + waktu(days=rec.duration)
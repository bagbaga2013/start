from odoo import models, fields

class MyHotel(models.Model):
    _name = 'my.hotel'
    _description = 'Hotel'
    _log_access = False
    
    name = fields.Char(string='اسم الفندق', required=True)
    code = fields.Char(string='كود الفندق')
    city = fields.Char(string='المدينة')
    address = fields.Text(string='العنوان')
    phone = fields.Char(string='رقم الهاتف')
    email = fields.Char(string='البريد الإلكتروني')
    rating = fields.Selection([
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
    ], string='التقييم')
    active = fields.Boolean(default=True)

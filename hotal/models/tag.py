from odoo import models, fields

class MyTag(models.Model):
     _name = 'my.tag'
     _description = 'Tag'
    #_inherit = ['sale.order']
     _inherit = 'my.hotel'
     namee = fields.Char(string='الوسم', required=True)
     test1 = fields.Many2one('hotel.room', string='الفندق' ) 
     #def  action_confirm(self):
      #   print("kkkkkkkkkkkkkkk")
      #  return res
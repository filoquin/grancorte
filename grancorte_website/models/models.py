# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class grancorte_website(models.Model):
#     _name = 'grancorte_website.grancorte_website'
#     _description = 'grancorte_website.grancorte_website'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

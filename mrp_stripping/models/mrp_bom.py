# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MrpBom(models.Model):
    _inherit = 'mrp.bom'
    
    type = fields.Selection(selection_add=[('stripping', 'Stripping')])

    @api.constrains
    def stripping_one_product(self):
    	if self.type=="stripping" and len(self.bom_line_ids) !=1:
	        raise UserError(_('stripping list require only one line.'))
 

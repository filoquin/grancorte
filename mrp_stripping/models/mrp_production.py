# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class MrpProduction(models.Model):

    _inherit = 'mrp.production'

    product_id = fields.Many2one(
        'product.product', 'Product',
        domain="[('bom_ids', '!=', False), ('bom_ids.active', '=', True), ('bom_ids.type', 'in',['normal','stripping']), ('type', 'in', ['product', 'consu']), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        readonly=True, required=True, check_company=True,
        states={'draft': [('readonly', False)]})

    bom_id = fields.Many2one(
        'mrp.bom', 'Bill of Material',
        readonly=True, states={'draft': [('readonly', False)]},
        domain="""[
        '&',
            '|',
                ('company_id', '=', False),
                ('company_id', '=', company_id),
            '&',
                '|',
                    ('product_id','=',product_id),
                    '&',
                        ('product_tmpl_id.product_variant_ids','=',product_id),
                        ('product_id','=',False),
        ('type', 'in' ,['normal','stripping'])]""",
        check_company=True,
        help="Bill of Materials allow you to define the list of required components to make a finished product.")

    """@api.onchange('bom_id')
    def _onchange_bom_id(self):
        _logger.info('stripping')

        if self.bom_id.type == 'stripping':
            _logger.info('stripping')
            self.product_qty = self.bom_id.product_qty
            self.product_uom_id = self.bom_id.product_uom_id.id
            self.move_raw_ids = []
            #self.move_raw_ids = [(2, move.id) for move in self.move_raw_ids.filtered(lambda m: m.bom_line_id)]
            self.picking_type_id = self.bom_id.picking_type_id or self.picking_type_id
            return 
        else: 
            _logger.info('no stripping')
            super(MrpProduction,self)._onchange_bom_id()
            return""" 


    def _generate_finished_moves(self):
        if self.bom_id.type == 'stripping':

            _logger.info(' stripping')
            moves_values = []
            #moves_values = [self._get_finished_move_value(self.product_id.id, self.product_qty, self.product_uom_id.id)]
            for byproduct in self.bom_id.byproduct_ids:
                #product_uom_factor = self.product_uom_id._compute_quantity(self.product_qty, self.bom_id.product_uom_id)
                product_uom_factor = 1 
                qty = byproduct.product_qty * (product_uom_factor / self.bom_id.product_qty)
                move_values = self._get_finished_move_value(byproduct.product_id.id,
                    qty, byproduct.product_uom_id.id, byproduct.operation_id.id,
                    byproduct.id)
                moves_values.append(move_values)
            moves = self.env['stock.move'].create(moves_values)
            return moves
        else: 
            _logger.info('no stripping')
            return super(MrpProduction,self)._generate_finished_moves()

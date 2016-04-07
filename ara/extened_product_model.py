# -*- coding: utf-8 -*-
from openerp import models, fields, api

class ExtendedProduct(models.Model):
	_inherit = 'product.product'
	recycling_method_id = fields.Many2one('ara.recyclingmethod', 'Recycling Method')

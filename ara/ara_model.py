# -*- coding: utf-8 -*-

from openerp import models, fields, api

class RecyclingMethod(models.Model):
	_name = 'ara.recyclingmethod'
	name = fields.Char('Recycling Method', required=True)

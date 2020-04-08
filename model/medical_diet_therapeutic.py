# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_diet_therapeutic(models.Model):
    _name = 'medical.diet.therapeutic'

    name = fields.Char(string='Tipo de dieta',required=True)
    code = fields.Char(string='Codigo',required=True)
    description = fields.Text(string='Descripción',required=True)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s

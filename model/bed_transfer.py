# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
#translado de cama !!!!!!!!!!!!!!!!!!!!
from odoo import models, fields, api, _
from datetime import date

class bed_transfer(models.Model):
    _name = 'bed.transfer'

    name = fields.Char("Nombre")
    date = fields.Datetime(string='Fecha')
    bed_from = fields.Char(string='Desde')
    bed_to = fields.Char(string='A')
    reason = fields.Text(string='Razón')
    inpatient_id = fields.Many2one('medical.inpatient.registration',string='Paciente hospitalizado')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s

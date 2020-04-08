# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_family_disease(models.Model):
    _name = 'medical.family.disease'
    _rec_name = 'medical_pathology_id'

    medical_pathology_id = fields.Many2one('medical.pathology', 'Enfermedad',required=True)
    relative = fields.Selection([('m', 'Madre'), ('f', 'Padre'), ('b', 'Hermano'), ('s', 'Hermana'), ('a', 'tía'), ('u', 'tío'), ('ne', 'Sobrino'), ('ni', 'Sobrina'), ('gf', 'Abuelo'), ('gm', 'Abuela')],string="Familiar")
    metrnal = fields.Selection([('m', 'Maternal'),('p', 'Paternal')],string="Maternal")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
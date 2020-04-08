# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from datetime import date,datetime
from odoo import api, fields, models, _


class medical_patient_disease(models.Model):
    _name = "medical.patient.disease"
    _rec_name = 'patient_id'

    pathology_id = fields.Many2one('medical.pathology','Enfermedad', required=True)
    disease_severity =  fields.Selection([('1_mi', 'Leve'),('2_mo', 'Moderado'),('3_sv', 'Severo')],'Gravedad')
    status =  fields.Selection([('c', 'Crónico'),('s', 'Status quo'),('h', 'Curado'),('i', 'Mejorando'),('w', 'Empeoramiento')],'Estado de la enfermedad')
    is_infectious = fields.Boolean('Enfermedad infecciosa')
    is_active = fields.Boolean('Enfermedad activa')
    short_comment = fields.Char('Observaciones')
    diagnosis_date = fields.Date('Fecha de diagnóstico')
    healed_date = fields.Date('Curado')
    age = fields.Integer('Edad cuando se diagnostica')
    doctor_id = fields.Many2one('medical.physician','Medico')
    is_allergic = fields.Boolean('Enfermedad alérgica')
    allergy_type =  fields.Selection([('da', 'Alergia a un medicamento'),('fa', 'Alergia alimentaria'),('ma', 'Alergia miscelánea'),('mc', 'Contraindicación miscelánea')],'Tipo de alergia')
    pregnancy_warning = fields.Boolean('Advertencia de embarazo')
    week_of_pregnancy = fields.Integer('Contratado en la semana de embarazo#')
    is_on_treatment = fields.Boolean('Actualmente en tratamiento')
    treatment_description = fields.Char('Descripción del tratamiento')
    date_start_treatment = fields.Date('Inicio del tratamiento.')
    date_stop_treatment = fields.Date('Fin del tratamiento')
    patient_id = fields.Many2one('medical.patient',string="Paciente")
    extra_info = fields.Text('Informacion adicional')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
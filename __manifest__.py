# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{

    "name" : "Sistema hospitalario base Gabriel",
    "version" : "13.0.0.1",
    "currency": 'PES',
    "summary": "Aplicaciones básicas Sistema de gestión hospitalaria Gestión de la atención sanitaria Clínica Aplicaciones de gestión gestionar la clínica gestionar Hospital del paciente gestionar Sistema de asistencia sanitaria Gestión del paciente Gestión del hospital Gestión de la asistencia sanitaria Gestión de la clínica hospital Solicitud de prueba de laboratorio",
    "category": "Industries",
    "description": """ """ ,
    "depends" : ["base", "sale_management", "stock", "account"],
    "data": [
            'security/hospital_groups.xml',
            'data/ir_sequence_data.xml',
            'views/assets.xml',
            'views/login_page.xml',
            'views/main_menu_file.xml',
            'wizard/medical_appointments_invoice_wizard.xml',
            'wizard/create_prescription_invoice_wizard.xml',
            'wizard/create_prescription_shipment_wizard.xml',
            'views/medical_medicament.xml',
            'views/medical_drug_route.xml',
            'wizard/medical_lab_test_create_wizard.xml',
            'wizard/medical_lab_test_invoice_wizard.xml',
            'views/medical_prescription_order.xml',
            'views/medical_directions.xml',
            'views/medical_dose_unit.xml',
            'views/medical_patient_evaluation.xml',
            'views/medical_family_disease.xml',
            'views/medical_inpatient_registration.xml',
            'views/medical_inpatient_medication.xml',
            'views/medical_insurance_plan.xml',
            'views/medical_appointment.xml',
            'views/medical_insurance.xml',
            'views/medical_patient_lab_test.xml',
            'views/medical_lab_test_units.xml',
            'views/medical_lab.xml',
            'views/medical_neomatal_apgar.xml',
            'views/medical_pathology_category.xml',
            'views/medical_pathology_group.xml',
            'views/medical_pathology.xml',
            'views/medical_patient_disease.xml',
            'views/medical_patient_medication.xml',
            'views/medical_patient_medication1.xml',
            'views/medical_patient_pregnancy.xml',
            'views/medical_patient_prental_evolution.xml',
            'views/medical_patient.xml',
            'views/medical_physician.xml',
            'views/medical_preinatal.xml',
            'views/medical_prescription_line.xml',
            'views/medical_puerperium_monitor.xml',
            'views/medical_rcri.xml',
            'views/medical_rounding_procedure.xml',
            'views/medical_test_critearea.xml',
            'views/medical_test_type.xml',
            'views/medical_vaccination.xml',
            'views/res_partner.xml',
            'report/report_view.xml',
            'report/appointment_recipts_report_template.xml',
            'report/medical_view_report_document_lab.xml',
            'report/medical_view_report_lab_result_demo_report.xml',
            'report/newborn_card_report.xml',
            'report/patient_card_report.xml',
            'report/patient_diseases_document_report.xml',
            'report/patient_medications_document_report.xml',
            'report/patient_vaccinations_document_report.xml',
            'report/prescription_demo_report.xml',
            'security/ir.model.access.csv',
	     ],
    "author": "Gabriel Pabon",
    "website": "none",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images":["static/description/Banner.png"],
    "live_test_url":'https://youtu.be/fk9dY53I9ow',

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'exemplo de odoo basico'

    name = fields.Char(required=True,size=20,string="Título")
    descripcion = fields.Text(string="A descripción")
    alto_en_cms = fields.Integer(string="Alto en cms:")
    ancho_en_cms = fields.Integer(string="Ancho en cms:")
    longo_en_cms = fields.Integer(string="Longo en cms:")



#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'modelo con distintos tipos de datos'


     name = fields.Char(string="Título:",size=20,required=True)
     descripcion = fields.Text(string="A Descripción:")
     alto_en_cms = fields.Integer(string="Alto en cms:")
     ancho_en_cms = fields.Integer(string="Ancho en cms:")
     longo_en_cms = fields.Integer(string="Longo en cms:")
     volume = fields.Float(string="Volume m3:",digits=(6,2),store=True,compute="_volume")
     peso = fields.Float(string="Peso en Kgs:",digits=(6,2),default=2.7)
     autorizado = fields.Boolean(default=False, string="¿Autorizado?:")
     sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')], string="Sexo:")

     @api.depends ('alto_en_cms','ancho_en_cms','longo_en_cms')
     def _volume(self):
         for rexistro in self:
             rexistro.volume = (float(rexistro.alto_en_cms) * float(rexistro.ancho_en_cms) * float(rexistro.longo_en_cms)) /1000000
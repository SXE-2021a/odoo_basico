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
    peso = fields.Float(digits=(6,2),default=2.7,string="Peso en KG.s:")
    volume = fields.Float(digits=(6, 7), compute="_volume", store=True, string="Volume m3")
    literal = fields.Char(store=False)
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')],string="Sexo:")

    @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(rexistro.ancho_en_cms) / 1000000

    @api.onchange('alto_en_cms')
    def _avisoAlto(self):
         for rexistro in self:
             if rexistro.alto_en_cms > 7:
                 rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
             else:
                 rexistro.literal = ""

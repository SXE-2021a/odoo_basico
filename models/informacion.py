# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class informacion(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'modelo con distintos tipos de datos'
     _sql_constraints = [('nomeUnico', 'unique(name)', 'Non se pode repetir o Titulo')]


     name = fields.Char(string="Título:",size=20,required=True)
     descripcion = fields.Text(string="A Descripción:")
     alto_en_cms = fields.Integer(string="Alto en cms:")
     ancho_en_cms = fields.Integer(string="Ancho en cms:")
     longo_en_cms = fields.Integer(string="Longo en cms:")
     volume = fields.Float(string="Volume m3:",digits=(6,2),store=True,compute="_volume")
     peso = fields.Float(string="Peso en Kgs:",digits=(6,2),default=2.7)
     densidade = fields.Float(string="Densidade KG/m3:", digits=(6, 4), store=True, compute="_densidade")
     autorizado = fields.Boolean(default=False, string="¿Autorizado?:")
     sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')], string="Sexo:")
     foto = fields.Binary(string='Foto')
     adxunto_nome = fields.Char(string="Nome Adxunto")
     adxunto = fields.Binary(string="Arquivo adxunto")
     literal = fields.Char(store=False)

     @api.depends ('alto_en_cms','ancho_en_cms','longo_en_cms')
     def _volume(self):
         for rexistro in self:
             rexistro.volume = (float(rexistro.alto_en_cms) * float(rexistro.ancho_en_cms) * float(rexistro.longo_en_cms)) /1000000

     @api.depends('peso', 'volume')
     def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = float(rexistro.peso) / float(rexistro.volume)
            else:
                rexistro.densidade = 0

     @api.onchange('alto_en_cms')
     def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cms > 7:
                rexistro.literal = 'O campo alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
            else:
                rexistro.literal = ""


     @api.constrains('')  # Ao usar ValidationError temos que importar a libreria ValidationError
     def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 4:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pedido(models.Model):
     _name = 'odoo_basico.pedido'
     _description = 'modelo para pedido'

     name = fields.Char(required=True, size=20, string="Identificador de Pedido")
     partner_id = fields.Many2one('res.partner', domain="[]", string="Cliente do Pedido:")
     fecha = fields.Date(string="Fecha do Pedido:")
     # Os campos One2many Non se almacenan na BD
     lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')

     def actualizadorSexo(self):
         informacion_ids = self.env['odoo_basico.informacion'].search([('autorizado', '=', False)])
         for rexistro in informacion_ids:
             self.env['odoo_basico.informacion']._cambia_campo_sexo(rexistro)
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lineapedido(models.Model):
     _name = 'odoo_basico.lineapedido'
     _description = 'modelo para lineapedido'

     descripcionLineaPedido = fields.Text(string="A descripción da Linea")
     # Os campos Many2one crean un campo na BD
     pedido_id = fields.Many2one('odoo_basico.pedido',ondelete="cascade", required=True)
     peso = fields.Float(string="Peso en Kgs:", digits=(6, 2), default=2.7)
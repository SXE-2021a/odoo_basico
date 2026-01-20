# -*- coding: utf-8 -*-

from odoo import models, fields, api

class persoa (models.Model):
   _inherit = 'res.partner' # como  non lle proporcioamos  _name facemos herdanza por extensión (herdanza de clase)
                            # por tanto non se crea unha nova táboa e os atributos engadense na táboa pai
                            # No xml temos que extender as vistas da clase pai

   apelidos = fields.Char(required=True,size=60,string="Apelidos")
   visible = fields.Boolean(string="¿Visible?", default=False)

   # O campo visible serve para visualizar só  os rexistros  que nos interesan domain="[('visible', '=','True')]"
   # Engadimos na relación many2one ou many2many unha condición

   # Temos que dar permisos en ir.model.access.csv para o model res_partner.
   # Engadir a liña:
   # odoo_basico_res_partner,odoo_basico.res_partner,model_res_partner,base.group_user,1,1,1,1
   @api.depends('apelidos', 'name')
   def _compute_display_name(self):
       for rexistro in self:
           if rexistro.apelidos:
               rexistro.display_name = f"{rexistro.apelidos} {rexistro.name}"
           else:
               rexistro.display_name = rexistro.name
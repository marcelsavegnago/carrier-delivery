# -*- coding: utf-8 -*-
# #############################################################################
#
#    Brazillian Carrier Correios Sigep WEB
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author Luis Felipe Mileo <mileo@kmee.com.br>
#
#    Sponsored by Europestar www.europestar.com.br
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm


from pysigep_web.pysigepweb.webservice_atende_cliente import WebserviceAtendeCliente
from pysigep_web.pysigepweb.webservice_calcula_preco_prazo import \
    WebserviceCalculaPrecoPrazo
from pysigep_web.pysigepweb.webservice_rastreamento import WebserviceRastreamento
from pysigep_web.pysigepweb.tag_nacional import TagNacionalPAC41068
from pysigep_web.pysigepweb.tag_plp import TagPLP
from pysigep_web.pysigepweb.tag_remetente import TagRemetente
from pysigep_web.pysigepweb.tag_dimensao_objeto import *
from pysigep_web.pysigepweb.tag_objeto_postal import *
from pysigep_web.pysigepweb.tag_correios_log import TagCorreiosLog
from pysigep_web.pysigepweb.diretoria import Diretoria
from pysigep_web.pysigepweb.endereco import Endereco
from pysigep_web.pysigepweb.pysigep_exception import ErroConexaoComServidor
from pysigep_web.pysigepweb.etiqueta import Etiqueta


class ShippingResponse(orm.Model):
    _name = 'shipping.response'

    def generate_tracking_no(self, cr, uid, ids, context={}, error=True):
        pass

    def _compute_volume(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for obj in ids:
            res[obj] = 0.00
        return res

    def _compute_weight(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for obj in ids:
            res[obj] = 0.00
        return res

    def _compute_weight_net(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for obj in ids:
            res[obj] = 0.00
        return res

    def shipment_confirm(self, cr, uid, ids, context=None):
        print 'ARROZ ARROZS'

        company_id = self.pool.get('res.users').browse(cr, uid, uid).company_id

        for ship in self.browse(cr, uid, ids):

            partner_id = ship.partner_id

            remetente_endereco = Endereco(logradouro=company_id.street,
                                          numero=company_id.number,
                                          bairro=company_id.district,
                                          cep=int(company_id.zip.replace('-', '')),
                                          cidade=company_id.l10n_br_city_id.name,
                                          uf=company_id.state_id.code,
                                          complemento=company_id.street2)

            destinatario_endereco = Endereco(logradouro=partner_id.street,
                                             numero=partner_id.number,
                                             bairro=partner_id.district,
                                             cep=int(partner_id.zip.replace('-', '')),
                                             cidade=partner_id.l10n_br_city_id.name,
                                             uf=partner_id.state_id.code,
                                             complemento=partner_id.street2)

            obj_tag_plp = TagPLP(company_id.sigepweb_main_post_card_number)

            obj_remetente = TagRemetente(cliente.nome,
                                         company_id.sigepweb_main_contract_number,
                                         cartao_postagem.codigo_admin,
                                         remetente_endereco,
                                         Diretoria(Diretoria.DIRETORIA_DR_PARANA),
                                         telefone=6112345008, email='cli@mail.com.br')


            picking_ids = ship.picking_line
            print picking_ids





    _columns = {
        'user_id': fields.many2one('res.users',
                                   'Responsible',
                                   readonly=True,
                                   states={'draft': [('readonly', False)]}),

        'name': fields.char('Reference', required=True, readonly=True),

        'carrier_tracking_ref': fields.char('Tracking Ref.', readonly=True),

        'carrier_id': fields.many2one('res.partner', string='Carrier',
                                      readonly=True,
                                      states={'draft': [('readonly', False)]}),

        'partner_id': fields.many2one('res.partner', string='Partner',
                                          readonly=True,
                                          states={'draft': [('readonly', False)]}),

        'carrier_responsible': fields.char('Carrier Responsible'),

        'date': fields.date('Date', require=True, readonly=True,
                            states={'draft': [('readonly', False)]}),

        'note': fields.text('Description / Remarks', readonly=True,
                            states={'draft': [('readonly', False)]}),

        'company_id': fields.many2one('res.company', 'Company'),

        'contract_id': fields.many2one('sigepweb.contract',
                                        string='Contract',
                                        domain="[('rescompany_id', '=',company_id)]"),

        'post_card_id': fields.many2one('sigepweb.post.card',
                                         string='Post Cards',
                                         domain="[('contract_id', '=', contract_id)]"),

        'state': fields.selection(
            [('draft', 'Draft'),
             ('confirmed', 'Confirmed'),
             ('in_transit', 'In Transit'),
             ('done', 'Done'),
             ('cancel', 'Cancel')
             ],
            required=True,),
        'picking_line': fields.many2many(
            'stock.picking.out',
            'shipping_stock_picking_rel',
            'response_id',
            'picking_id',
            'Pickings',
            readonly=True,
            states={'draft': [('readonly', False)]},
            domain=[
                ('type', '=', 'out'),
                ('state', '=', 'done'),
                # ('carrier_id', '=', 'picking_line.carrier_id.partner_id'),
                # ('shipping_group', '=', False),
                ],
        ),
        # 'departure_picking_ids': fields.one2many('stock.picking.out',
        #                                          'shipping_response_id',
        #                                          'Departure Pickings',
        #     # readonly=True,
        #     # states={'draft': [('readonly', False)]}
        # ),
        'volume': fields.function(_compute_volume,
                                  type='float',
                                  string=u'Nº Volume',
                                  readonly=True,
                                  store=True,),
        'weight': fields.function(_compute_weight,
                                  type='float',
                                  string="Weight",
                                  readonly=True, store=True,),
        'weight_net': fields.function(_compute_weight_net,
                                      type='float',
                                      string="Net Weight",
                                      readonly=True, store=True,),
    }
    _defaults = {
        'user_id': lambda obj, cr, uid, context: uid,
        'state': 'draft',
        # 'selected': False,
        'name': '/',
    }



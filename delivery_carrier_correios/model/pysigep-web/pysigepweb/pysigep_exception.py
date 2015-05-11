# -*- coding: utf-8 -*-
# #############################################################################
#
#    Brazillian Carrier Correios Sigep WEB
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author: Michell Stuttgart <michell.stuttgartx@kmee.com.br>
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


class SigepWEBBaseException(Exception):

    def __init__(self, msg, *args):
        self.message = msg.format(args)

    def __str__(self):
        return repr(self.message)


class ErroSemConecaoComInternet(SigepWEBBaseException):

    def __init__(self, msg, *args):
        self.message = u'Falha na conexão com a Internet'

    def __str__(self):
        return repr(self.message)


class ErroConexaoComServidor(SigepWEBBaseException):

    def __str__(self):
        return repr(self.message)


class ErroTamanhoParamentroIncorreto(SigepWEBBaseException):
    def __str__(self):
        return repr(self.message)


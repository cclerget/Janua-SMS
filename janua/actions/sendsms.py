# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#
# Copyright (c) 2016 Cédric Clerget - HPC Center of Franche-Comté University
#
# This file is part of Janua-SMS
#
# http://github.com/mesocentrefc/Janua-SMS
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from janua.actions.action import Action
from janua.actions.action import argument
from janua.ws import json_error, json_success
from janua.ws.services import urlconfig

class SendSms(Action):
    """
    Send SMS

    Sample request send to all my contacts with special group 'all':

    .. code-block:: javascript

       POST /sendsms HTTP/1.1
       Host: janua.mydomain.com
       Content-Type: application/json

       {
         "message": "Test",
         "to": "all"
       }

    Sample response:

    .. code-block:: javascript

       HTTP/1.1 200

       {
         "message": "SMS message has been queued",
         "success": true
       }

    """

    category = '__INTERNAL__'

    def console(self):
        return self.send_sms(message=self.message(), to=self.to())

    @urlconfig('/sendsms')
    def web(self):
        success, message = self.send_sms(message=self.message(), to=self.to())
        if success:
            return json_success(message)
        else:
            return json_error(message)

    @argument(required=True)
    def message(self):
        """Your message"""
        return str()

    @argument(required=True)
    def to(self):
        """Recipient(s)"""
        return str()

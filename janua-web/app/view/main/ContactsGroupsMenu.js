/**
 * Copyright (c) 2016 Cédric Clerget - HPC Center of Franche-Comté University
 *
 * This file is part of Janua-SMS
 *
 * http://github.com/mesocentrefc/Janua-SMS
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation v2.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
Ext.define('JanuaWeb.view.main.ContactsGroupsMenu', {
    extend: 'Ext.menu.Menu',

    alias: 'widget.ContactsGroupsMenu',

    controller: 'main',

    plain: true,
    items: [{
        text: 'Import contacts/groups',
        handler: 'onImportContactGroup'
    }, {
        text: 'Export contacts/groups',
        handler: 'onExportContactGroup'
    }]
});
# -*- encoding: utf-8 -*-
##############################################################################
#
#    Donation Mass module for Odoo
#    Copyright (C) 2014-2015 Barroux Abbey (www.barroux.org)
#    Copyright (C) 2014-2015 Akretion France (www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
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


{
    'name': 'Donation Mass',
    'version': '0.1',
    'category': 'Religion',
    'license': 'AGPL-3',
    'summary': 'Ability to create mass from donation lines',
    'author': 'Barroux Abbey, Akretion, Odoo Community Association (OCA)',
    'website': 'http://www.barroux.org',
    'depends': ['donation', 'mass'],
    'data': [
        'mass_view.xml',
        'donation_view.xml',
        'donation_mass_data.xml',
        ],
    'demo': ['donation_mass_demo.xml'],
    'test': ['test/donation_mass.yml'],
}

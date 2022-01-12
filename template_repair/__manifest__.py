##############################################################################
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    'name': 'repair',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summary': "Proyecto para Repair",
    'author': "jeo Software",
    'website': 'http://github.com/marionumza/cl-repair',
    'license': 'AGPL-3',
    'depends': [
        'standard_depends_ce'
        ],
    'installable': True,

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'EE',

    # Config to write in odoo.conf
    'config': [

        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
                'workers = 5',
                'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
                'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
                'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
                'limit_memory_hard = 2684354560',
    ],

    'port': '8069',

    'git-repos': [
        'https://github.com/marionumza/cl-repair.git',
        #'git@github.com:jobiols/odoo-jeo-ce.git',
        #'git@github.com:jobiols/odoo-private-addons.git',

        # OCA
        'https://github.com/OCA/l10n-spain OCA-l10n-spain',
        'https://github.com/OCA/account-financial-reporting OCA-account-financial-reporting',
        'https://github.com/OCA/server-ux OCA-server-ux',
        'https://github.com/OCA/account-invoicing OCA-account-invoicing',
        'https://github.com/OCA/queue OCA-queue',
        'https://github.com/OCA/account-financial-tools OCA-account-financial-tools',
        'https://github.com/OCA/connector OCA-connector',
        'https://github.com/OCA/community-data-files OCA-community-data-files',
        'https://github.com/OCA/reporting-engine OCA-reporting-engine',
        'https://github.com/OCA/bank-payment OCA-bank-payment',
        'https://github.com/OCA/edi OCA-edi',
        'https://github.com/OCA/account-fiscal-rule OCA-account-fiscal-rule',
        'https://github.com/OCA/server-env OCA-server-env',
        'https://github.com/OCA/mis-builder OCA-mis-builder',
        'https://github.com/OCA/partner-contact OCA-partner-contact',
        'https://github.com/OCA/intrastat-extrastat OCA-intrastat-extrastat',
        'https://github.com/marionumza/repair.git repair',

        
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0e',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}

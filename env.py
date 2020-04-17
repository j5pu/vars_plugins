#!/usr/bin/env python3
# Copyright 2019 Zijian Guo <guozijian@unitedstack.com>, <guozijn@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

DOCUMENTATION = '''
    vars: uos_net_vars
    short_description: Parsing vars from csv file
    description:
        - Load YAML variable into ansible host corresponding to "hostname" in csv_vars/servers.csv file.
    options:
      _valid_extensions:
        default: [".csv"]
'''
import os
from ansible.plugins.vars import BaseVarsPlugin
from ansible.utils.vars import combine_vars

EXCLUDE = [
    "HOME",
    "LC_CTYPE",
    "LOGNAME",
    "OLDPWD",
    "PWD",
    "SHLVL",
    "SSH_AUTH_SOCK",
    "SUDO_COMMAND",
    "SUDO_GID",
    "SUDO_UID",
    "SUDO_USER",
    "TERM",
    "TERM_PROGRAM_VERSION",
    "TERM_SESSION_ID",
    "TMPDIR",
    "USER",
    "USERNAME",
    "XPC_FLAGS",
    "XPC_SERVICE_NAME",
    "_",
    "__CF_USER_TEXT_ENCODING"
           ]


class VarsModule(BaseVarsPlugin):
    def get_vars(self, loader, path, entities, cache=True):
        if not isinstance(entities, list):
            entities = [entities]

        super(VarsModule, self).get_vars(loader, path, entities)

        data = {}
        for entity in entities:
            if entity.name == 'all':
                data = combine_vars(os.environ, entity.vars)

        return data

# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


{
  'variables': {
    'system_include_path_apr%': '/usr/include/apr-1.0',
  },

      'targets': [
        {
          'target_name': 'include',
          'type': 'none',
          'direct_dependent_settings': {
            'include_dirs': [
              '<(system_include_path_apr)',
            ],
            'defines': [
              # We need to define _LARGEFILE64_SOURCE so <sys/types.h>
              # provides off64_t.
              '_LARGEFILE64_SOURCE',
              'HAVE_CONFIG_H',
              'LINUX=2',
              '_REENTRANT',
              '_GNU_SOURCE',
            ],
          },
        },
        {
          'target_name': 'apr',
          'type': 'none',
          'dependencies': [
            'include',
          ],
          'export_dependent_settings': [
            'include',
          ],
          'link_settings': {
            'libraries': [
              '-lapr-1',
            ],
          },
        },
      ],
}


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
#
# Based on Chromium's icu.gyp.

{
      'targets': [
        {
          'target_name': 'system_icu',
          'type': 'none',
          'direct_dependent_settings': {
            'defines': [
              'USE_SYSTEM_ICU',
            ],
            'cflags+': [
              '<!@(icu-config --cppflags-searchpath)'
            ],
          },
          'link_settings': {
            'ldflags': [
              '<!@(icu-config --ldflags)',
            ],
            'libraries': [
              '<!@(icu-config --ldflags-libsonly)',
            ],
          },
        },
        {
          'target_name': 'icudata',
          'type': 'none',
          'dependencies': ['system_icu'],
          'export_dependent_settings': ['system_icu'],
        },
        {
          'target_name': 'icuuc',
          'type': 'none',
          'dependencies': ['system_icu'],
          'export_dependent_settings': ['system_icu'],
        },
      ],
}

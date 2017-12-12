# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'gtest',
      'type': 'static_library',
      'sources': [
        '/usr/src/gtest/src/gtest-all.cc',
      ],
      'include_dirs': [
        '/usr/src/gtest',
      ],
    },
    {
      'target_name': 'gtest_main',
      'type': 'static_library',
      'dependencies': [
        'gtest',
      ],
      'sources': [
        '/usr/src/gtest/src/gtest_main.cc',
      ],
    },
    {
      'target_name': 'gtest_prod',
      'type': 'none',
      'dependencies': [
        'gtest',
      ]
    },
  ],
}

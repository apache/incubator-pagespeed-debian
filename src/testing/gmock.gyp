# Copyright (c) 2009 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'gmock',
      'type': 'static_library',
      'sources': [
        '/usr/src/gmock/src/gmock-all.cc'
      ],
      'include_dirs': [
        '/usr/src/gmock',
      ],
    },
  ],
}

#!/bin/sh
#
# This script uses gyp to generate Makefiles for mod_pagespeed built against
# the following system libraries:
#   apr, aprutil, apache httpd headers, icu, libjpeg_turbo, libpng, zlib.
#
# Besides the -D use_system_libs=1 below, you may need to set (via -D var=value)
# paths for some of these libraries via these variables:
#   system_include_path_httpd, system_include_path_apr,
#   system_include_path_aprutil.
#
# for example, you might run
# ./generate.sh -Dsystem_include_path_apr=/usr/include/apr-1 \
#               -Dsystem_include_path_httpd=/usr/include/httpd
# to specify APR and Apache include directories.
#
# Also, BUILDTYPE=Release can be passed to make (the default is Debug).
echo "Generating src/Makefile"
src/build/gyp_chromium -D use_system_libs=1 $*

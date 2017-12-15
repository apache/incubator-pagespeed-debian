#!/bin/sh

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
cd $SCRIPT_DIR

## checking for quilt in packaging-dev
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' packaging-dev|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
  echo "Installing packaging-dev."
  sudo apt-get --force-yes --yes install packaging-dev
fi

## apply patches using quilt

# configure quilt
export QUILT_PATCHES=$SCRIPT_DIR/debian/patches

echo "Applying patches.."
quilt push -a

## build source
echo "Building source.."
./generate.sh
cd src
make BUILDTYPE=Release -j4


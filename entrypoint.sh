#!/bin/sh -l

apt-get update
apt-get install cmake python3 git -y
git clone --depth 1 https://github.com/jayanta525/apindex-v2.git
cd apindex-v2
cmake . -DCMAKE_INSTALL_PREFIX=/usr
make install
cd ..
rm -rf apindex-v2/
apindex $1/.

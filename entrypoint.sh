#!/bin/sh -l

sudo apt-get update
sudo apt-get install cmake python3 -y
git clone --depth 1 https://github.com/jayanta525/apindex-v2.git
cd apindex-v2
cmake . -DCMAKE_INSTALL_PREFIX=/usr
sudo make install
cd ..
rm -rf apindex-v2/
apindex $1/.

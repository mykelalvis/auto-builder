#!/bin/sh
#./remove-autobuild.sh
python setup.py sdist
cd dist
tar xzvf ./auto-builder-1.0.tar.gz
cd auto-builder-1.0/
sudo python setup.py install


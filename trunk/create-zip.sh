#!/bin/sh
mkdir -p auto_builder/ply
cp ply/*py auto_builder/ply 
cp __init__.py conf.py auto_builder.py manifest.py generator.py dependencies.py auto_builder/
zip -r auto-builder.zip auto_builder/
rm -rf auto_builder


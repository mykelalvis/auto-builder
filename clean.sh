#!/bin/sh
find ./ | grep -e ".*pyc$" -e ".*out$"  | xargs rm

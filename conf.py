#####
#    !/usr/bin/env python

################################################################################
#
# Auto Builder configuration settings
#
################################################################################

jar_path = [
'../Minerva-SDK/lib/']

bundle_dirs = [
'org.aspectj.runtime_1.6.4.20090304172355',
'org.aspectj.weaver_1.6.4.20090304172355',
'org.syndeticlogic.gnu.io_2.1.7'
]

src_path = [
'../org.syndeticlogic.minerva',
'../org.syndeticlogic.minerva.adapters',
'../org.syndeticlogic.minerva.init',
'../org.syndeticlogic.minerva.tools'
]

do_not_package_libs = [
'com.springsource.org.junit_4.8.1.jar',
'org.syndeticlogic.gnu.io_2.1.7.jar'
]

################################################################################
#
# Package Manager configuration settings
#
################################################################################

#launchers = ['../Rifidi-SDK/launchers']
#config_top_dir = 'config'
#lib = 'lib'
#debian_dir = 'DEBIAN'
#deploy = 'deploy'
#platforms = 'platform-dep'
#configurations = ['ambient', 'edge']


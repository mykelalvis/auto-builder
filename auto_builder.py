#!/usr/bin/env python
#
#    This module contains the unit tests for the auto builder tools.
#
#    Authtor: James Percent (james@empty-set.net)
#    Copyright 2010, 2011 James Percent
# 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import logging
import logging.config
try:
    logging.config.fileConfig('logger.config')
except:
    pass
logging.config.string

import os
import sys
import conf
import manifest
import subprocess
import dependencies
import generator

from optparse import OptionParser
from os.path import join, abspath
from generator import AntGenerator, FileWriter
from dependencies import BinaryBundleFinder
from dependencies import SourceBundleFinder

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
#    
#class Dep:
#    def __init__(self, jars, src, target):
#        self.jars = jars
#        self.src = src
#        self.exports = {}
#        self.bundles = {}
#        self.required_jars = {}
#        self.target_platform = target
#        
#    def __add_package__(self, packages, package, bundle):
#        #package.name -> [(package, bundle), (package, bundle)]
#        if package.name in packages:
#                
#            inserted = False
#            for pentry, bentry in packages[package.name]:
#                index = packages[package.name].index((pentry, bentry))
#                assert index >= 0 and index <= len(packages[package.name])
#                    
#                if package.b_version.is_equal(pentry.b_version):
#                    if bundle.is_binary_bundle:
#                        packages[package.name].insert(index, (package, bundle))
#                    else:
#                        packages[package.name].insert(index+1, (package, bundle))
#                    inserted = True
#                    break
#                    
#                elif package.b_version.is_less(pentry.b_version):
#                    packages[package.name].insert(index, (package, bundle))
#                    inserted = True
#                    break
#                    
#            if inserted == False:
#                packages[package.name].append((package, bundle))
#                    
#        else:
#            packages[package.name] = [(package, bundle)]
#            
#    def __partially_order__(self, bundle):
#        ret = False
#        for dep_bundle in bundle.deps:
#            for dep_dep_bundle in dep_bundle.deps:
#                if dep_dep_bundle == bundle:
#                    print 'ERROR: circular dependencies are not supported.'
#                    assert False
#                        
#                #print 'bundle ', bundle, bundle.sym_name, '=', bundle.build_level                
#                #print 'dep bundle ', dep_bundle, dep_bundle.sym_name,'=', dep_bundle.build_level
#                
#                
#            if dep_bundle.build_level >= bundle.build_level and not dep_bundle.is_binary_bundle:
#                #print 'matched: ', bundle.sym_name, ' deps on ', dep_bundle.sym_name
#                bundle.build_level = dep_bundle.build_level + 1
#                ret = True
#        return ret      
#        
#    def sort(self):
#        #for bundle in src.bundles:
#        #    print bundle.sym_name, bundle.build_level
#        h4x0r = True
#        while h4x0r:
#            h4x0r = False
#            for bundle in self.src.bundles:
#                if self.__partially_order__(bundle):
#                    h4x0r = True
#                   
#        self.src.bundles = sorted(self.src.bundles, key=lambda bundle : bundle.build_level)
#        
#        for bundle in self.src.bundles:
#            #print bundle.sym_name, bundle.build_level
#            pass
#        
#        return True
#        
#    def resolve(self):
#        exports = {}
#        bundles = {}
#        for bundle in self.src.bundles:
#            print bundle.sym_name
#            assert not bundle.sym_name in bundles 
#            bundles[bundle.sym_name] = bundle
#                
#            for package in bundle.epackages:
#                self.__add_package__(exports, package, bundle)
#        #assert False
#        
#        #print bundles
#            
#        for bundle in self.jars.bundles:
#            #print '--->'+str(bundle.sym_name)+'<---', bundle
#            if not bundle.sym_name in bundles:
#                bundles[bundle.sym_name] = bundle
#            else:
#                #print 'Bundle '+str(bundle.sym_name)+' found both binary and src; using the src version (this should be an option)'
#                assert join(bundle.root, bundle.file) in self.target_platform
#                del self.target_platform[join(bundle.root,bundle.file)]
#                
#            #print bundle.display()
#            for package in bundle.epackages:
#                self.__add_package__(exports, package, bundle)
#        
#        #assert False
#        #print bundles
#        required_jars = {}
#        # package.name = [(pacakge, bundle), (package, bundle)]
#        for bundle in self.src.bundles:
#            
#            if bundle.fragment:
#                assert bundle.fragment_host.name in bundles
#              
#            for required_bundle_info in bundle.rbundles:
#                found = False
#                print 'required bundle', bundle.sym_name , required_bundle_info.name 
#                if required_bundle_info.name in bundles and \
#                    required_bundle_info.is_in_range(\
#                        bundles[required_bundle_info.name].version):
#                    found = True
#                    if bundle.fragment and bundle.sym_name == 'com.ambient.labtrack.test':
#                        print 'adding dep '+str(required_bundle_info.name)+\
#                              '-'+str(bundles[required_bundle_info.name].version),' to ',\
#                                      bundle.sym_name
#                    print 'Adding the dep bundle = ', required_bundle_info.name, bundles[required_bundle_info.name]
#                    
#                    bundle.add_dep(bundles[required_bundle_info.name])
#                    if bundles[required_bundle_info.name].is_binary_bundle:
#                        required_jars[bundles[required_bundle_info.name].sym_name] =\
#                        bundles[required_bundle_info.name]
#                        
#                if not found:
#                    print 'ERROR could not find matching required bundle ',\
#                        required_bundle_info.name, required_bundle_info
#                        
#            for package in bundle.ipackages:
#                found = False
#                version_found = []
#                if package.name in exports:
#                    for ex_package, ex_bundle in exports[package.name]:
#                        #if package.name == 'javax.jms':
#                            #import pdb
#                            #pdb.set_trace()
#                        if package.is_in_range(ex_package.b_version):
#                            found = True
#                            #print 'adding dep '+ex_bundle.sym_name+' to '+bundle.sym_name, 'because of package ', package.name
#                            bundle.add_dep(ex_bundle)
#                            if ex_bundle.is_binary_bundle:
#                                required_jars[ex_bundle.sym_name] = ex_bundle
#                        else:
#                            version_found.append(ex_package)
#                            #print ' pde build doesnt do the right thing either'
#                            
#                        #else:
#                            #import pdb
#                            #pdb.set_trace()
#                        #    if package.is_in_range(ex_package.b_version):
#                        #        pass
#                    if not found:
#                        found_str = ''
#                        for i in version_found:
#                            found_str += i.__str__() + ', '
#                            
#                        print 'ERROR: cannot find the correct version of '+package.name+\
#                        ' for '+bundle.sym_name+'; requires '+package.__str__()+\
#                        ' found = '+found_str
#                        return False
#                        
#                else:
#                    import re
#                    print re.match(r'javax.xml.namespace', str(exports))
#                    print 'ERROR: cannot resolve package: ', package.name\
#                    +' for bundle '+bundle.sym_name+'; skipping it'
#                    #return False
#                    
#        #print required_jars
#        #self.required_jars = required_jars
#        #assert False
#        return True
#        
                    
def set_logger_level(log_level):
    logger.setLevel(log_level)
    dependencies.set_logger_level(log_level)
    generator.set_logger_level(log_level)
    manifest.set_logger_level(log_level)

class Parameters:
    def __init__(self):
        self.args = None
        self.options = None
        self.parser = OptionParser(version="%prog 1.3.37")

        display_jars_help = 'Displays bundles found on the library_path.'
        display_src_help = 'Display source bundles found on the source_path.'
        check_dep_help = 'Validates dependencies without generating build artifacts.'
        build_gen_help = 'Validate dependencies and generate build artifacts.'
        loglevel_help = 'Set the logging level; valid values are debug, info, '\
                        'warn, error and critical'
        
        lib_path_help = 'A colon separated list of valid root directories to search '\
                        'for binary bundles (in PDE speak this equates to the search '\
                        'path to bundles in the target platform); overrides the '\
                        'library_path defined in conf.py.'
        
        src_path_help = 'A colon separated list of valid root directories to search '\
                        'for source bundles; overrides the '\
                        'source_path defined in conf.py.'
        
        project_name_help = 'Specifies the name to use in the generated '\
                                 'content; overrides the project_name defined '\
                                 'in conf.py'        
                
        #; if no options are given, '\
        #                 'then this command is executed; supported values'\
        #                 ' are: ant, make, maven; default value is: ant.'
        self.parser.add_option('-l', '--logging-level', dest='loglevel',
                               metavar='LEVEL', help=loglevel_help)
        self.parser.add_option("-j", "--display-jars", action="store_true",
                                default=False, dest="display_jars",
                                help=display_jars_help)
        self.parser.add_option("-d", "--display-src", action="store_true",
                                default=False, dest="display_src",
                                help=display_src_help)
        self.parser.add_option("-c", "--check-dep", action="store_true",
                               default=False, dest="check_dep",
                               help=check_dep_help)
        self.parser.add_option("-b", "--build-gen", action="store_true",
                               default=False, dest="build_gen",
                               help=build_gen_help)
        self.parser.add_option("-p", "--lib-path", default='', type=str,
                               dest="library_path", metavar="PATH", 
                               help=lib_path_help)
        self.parser.add_option("-s", "--source-path", default='', type=str,
                               dest="source_path", metavar="PATH", 
                               help=src_path_help)
        self.parser.add_option("-n", "--project-name", default='', type=str,
                               dest="project_name", metavar="NAME", 
                               help=project_name_help)
        #self.parser.add_option("-g", "--gen-build",
        #              dest="gen_build", metavar="BUILD-TYPE", type=str,
        #              default='ant', help=gen_build_help)
                        
        (self.options, self.args) = self.parser.parse_args()
                    
        valid_levels = { 'debug' : logging.DEBUG, 'info' : logging.INFO,
                         'warn' : logging.WARN, 'error' : logging.ERROR,
                         'critical' : logging.CRITICAL}    
            
        if self.options.loglevel != None and self.options.loglevel in valid_levels:
            set_logger_level(valid_levels[self.options.loglevel])
        else:
            if self.options.loglevel:
                logger.error('Invalid log level: '+self.options.loglevel+ \
                             ' using default, which is WARN')
            set_logger_level(logging.WARN)
        
        if self.options.library_path != '':
            self.options.jar_path = self.options.library_path.split(':')
            print self.options.jar_path
        else:
            try:
                self.options.jar_path = conf.library_path
            except:
                logger.critical('Library path is not defined; exiting.')
                self.parser.print_help()
                raise Exception('Library path is not defined; exiting.')
        
        if not validate('library path', self.options.jar_path):
            logger.critical('All library path directories must be validate; exiting')
            raise Exception('All library path directories must be validate; exiting')
        
        if self.options.source_path != '':
            self.options.src_path = self.options.source_path.split(':')
            print self.options.src_path
        else:
            try:
                self.options.src_path = conf.source_path
            except:
                logger.critical('Source path is not defined; exiting.')
                self.parser.print_help()
                raise Exception('Source path is not defined; exiting.')

        
        if not validate('source path', self.options.src_path):
            logger.critical('All source path directories must be validate; exiting')
            raise Exception('All source path directories must be validate; exiting')
        
        if self.options.project_name == '':
            try:
                self.options.project_name = conf.project_name
            except:
                logger.info('Project name is not defined.')
    
def validate(name, path):
    print path
    for dir in path:
        if not os.path.isdir(dir):
            logger.error('Invalid directory on the '+name+': '+dir)
            return False
    return True

def load_jars(jar_path):
    jfinder = BinaryBundleFinder()
    jfinder.find(jar_path)
    jfinder.load()
    return jfinder
    
def load_src(src_path):
    sfinder = SourceBundleFinder()
    sfinder.find(src_path)
    sfinder.load()
    return sfinder

def convert_paths(jar_path, src_path):
    index = 0
    for path in jar_path:
        jar_path[index] = abspath(path)
        index += 1
    index = 0
    for path in src_path:
        src_path[index] = abspath(path)
        index += 1
        

def run():
    
    jars = None
    src = None
    deps = None
    cmd_set = False        
    params = Parameters()
    
    if params.options.display_jars:
        print '-'*80
        jars = load_jars(params.options.jar_path)
        jars.display()
        cmd_set = True
 
    if params.options.display_src:
        if not cmd_set:
            print '-'*80
        src = load_src(params.options.src_path)
        src.display()
        cmd_set = True
        
    if params.options.check_dep:
        if not jars:
            jars = load_jars(params.options.jar_path)
               
        if not src:
            src = load_src(params.options.src_path)
                
        #jars.display()
        #src.display()
            
        deps = Dep(jars, src, jars.target_platform)
        assert deps.resolve()
        assert deps.sort()
        cmd_set = True
        
    if params.options.build_gen or not cmd_set:
        if jars == None:
            jars = load_jars(params.options.jar_path)
               
        if src == None:
            src = load_src(params.options.src_path)
                
        if deps == None:
            deps = Dep(jars, src, jars.target_platform)
            assert deps.resolve()
            assert deps.sort()
            
        writer = FileWriter()
        gen = AntGenerator(params.options.project_name, deps.jars, deps.src.bundles,
                           deps.target_platform, '.', writer)
        gen.generate_build_files()

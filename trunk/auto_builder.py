#!/usr/bin/env python

import logging
import logging.config
logging.config.fileConfig('logger.config')

import os
import manifest
import subprocess
import dependencies
import generator

from conf import project_name, jar_path, src_path, bundle_dirs, do_not_package_libs
from optparse import OptionParser
from os.path import join, abspath
from generator import AntGenerator, FileWriter
from dependencies import BinaryBundleFinder
from dependencies import SourceBundleFinder

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

#import dependencies

class Dep:
    def __init__(self, jars, src, target):
        self.jars = jars
        self.src = src
        self.exports = {}
        self.bundles = {}
        self.required_jars = {}
        self.target_platform = target
        
    def __add_package__(self, packages, package, bundle):
        #package.name -> [(package, bundle), (package, bundle)]
        if package.name in packages:
                
            inserted = False
            for pentry, bentry in packages[package.name]:
                index = packages[package.name].index((pentry, bentry))
                assert index >= 0 and index <= len(packages[package.name])
                    
                if package.b_version.is_equal(pentry.b_version):
                    if bundle.is_binary_bundle:
                        packages[package.name].insert(index, (package, bundle))
                    else:
                        packages[package.name].insert(index+1, (package, bundle))
                    inserted = True
                    break
                    
                elif package.b_version.is_less(pentry.b_version):
                    packages[package.name].insert(index, (package, bundle))
                    inserted = True
                    break
                    
            if inserted == False:
                packages[package.name].append((package, bundle))
                    
        else:
            packages[package.name] = [(package, bundle)]
            
    def __partially_order__(self, bundle):
        ret = False
        for dep_bundle in bundle.deps:
            for dep_dep_bundle in dep_bundle.deps:
                if dep_dep_bundle == bundle:
                    print 'ERROR: circular dependencies are not supported.'
                    assert False
                        
                #print 'bundle ', bundle, bundle.sym_name, '=', bundle.build_level                
                #print 'dep bundle ', dep_bundle, dep_bundle.sym_name,'=', dep_bundle.build_level
                
                
            if dep_bundle.build_level >= bundle.build_level and not dep_bundle.is_binary_bundle:
                #print 'matched: ', bundle.sym_name, ' deps on ', dep_bundle.sym_name
                bundle.build_level = dep_bundle.build_level + 1
                ret = True
        return ret      
        
    def sort(self):
        #for bundle in src.bundles:
        #    print bundle.sym_name, bundle.build_level
        h4x0r = True
        while h4x0r:
            h4x0r = False
            for bundle in src.bundles:
                if self.__partially_order__(bundle):
                    h4x0r = True
                   
        src.bundles = sorted(src.bundles, key=lambda bundle : bundle.build_level)
        
        for bundle in src.bundles:
            #print bundle.sym_name, bundle.build_level
            pass
        
        return True
        
    def resolve(self):
        exports = {}
        bundles = {}
        for bundle in src.bundles:
            print bundle.sym_name
            assert not bundle.sym_name in bundles 
            bundles[bundle.sym_name] = bundle
                
            for package in bundle.epackages:
                self.__add_package__(exports, package, bundle)
        #assert False
        
        #print bundles
            
        for bundle in jars.bundles:
            #print '--->'+str(bundle.sym_name)+'<---', bundle
            if not bundle.sym_name in bundles:
                bundles[bundle.sym_name] = bundle
            else:
                #print 'Bundle '+str(bundle.sym_name)+' found both binary and src; using the src version (this should be an option)'
                assert join(bundle.root, bundle.file) in self.target_platform
                del self.target_platform[join(bundle.root,bundle.file)]
                
            #print bundle.display()
            for package in bundle.epackages:
                self.__add_package__(exports, package, bundle)
        
        #assert False
        #print bundles
        required_jars = {}
        # package.name = [(pacakge, bundle), (package, bundle)]
        for bundle in src.bundles:
            
            if bundle.fragment:
                assert bundle.fragment_host.name in bundles
              
            for required_bundle_info in bundle.rbundles:
                found = False
                print 'required bundle', bundle.sym_name , required_bundle_info.name 
                if required_bundle_info.name in bundles and \
                    required_bundle_info.is_in_range(\
                        bundles[required_bundle_info.name].version):
                    found = True
                    if bundle.fragment and bundle.sym_name == 'com.ambient.labtrack.test':
                        print 'adding dep '+str(required_bundle_info.name)+\
                              '-'+str(bundles[required_bundle_info.name].version),' to ',\
                                      bundle.sym_name
                    print 'Adding the dep bundle = ', required_bundle_info.name, bundles[required_bundle_info.name]
                    
                    bundle.add_dep(bundles[required_bundle_info.name])
                    if bundles[required_bundle_info.name].is_binary_bundle:
                        required_jars[bundles[required_bundle_info.name].sym_name] =\
                        bundles[required_bundle_info.name]
                        
                if not found:
                    print 'ERROR could not find matching required bundle ',\
                        required_bundle_info.name, required_bundle_info
                        
            for package in bundle.ipackages:
                found = False
                version_found = []
                if package.name in exports:
                    for ex_package, ex_bundle in exports[package.name]:
                        #if package.name == 'javax.jms':
                            #import pdb
                            #pdb.set_trace()
                        if package.is_in_range(ex_package.b_version):
                            found = True
                            #print 'adding dep '+ex_bundle.sym_name+' to '+bundle.sym_name, 'because of package ', package.name
                            bundle.add_dep(ex_bundle)
                            if ex_bundle.is_binary_bundle:
                                required_jars[ex_bundle.sym_name] = ex_bundle
                        else:
                            version_found.append(ex_package)
                            #print ' pde build doesnt do the right thing either'
                            
                        #else:
                            #import pdb
                            #pdb.set_trace()
                        #    if package.is_in_range(ex_package.b_version):
                        #        pass
                    if not found:
                        found_str = ''
                        for i in version_found:
                            found_str += i.__str__() + ', '
                            
                        print 'ERROR: cannot find the correct version of '+package.name+\
                        ' for '+bundle.sym_name+'; requires '+package.__str__()+\
                        ' found = '+found_str
                        return False
                        
                else:
                    import re
                    print re.match(r'javax.xml.namespace', str(exports))
                    print 'ERROR: cannot resolve package: ', package.name\
                    +' for bundle '+bundle.sym_name+'; skipping it'
                    #return False
                    
        #print required_jars
        #self.required_jars = required_jars
        #assert False
        return True
        
        
class Jars:
    def __init__(self):
        self.jar_files = []
        self.bundles = []
        self.unique_bundles = {}
        self.target_platform = {}
        
    def load(self):
        for root, file in self.jar_files:
            ret = subprocess.call(['cp', join(root, file), '/tmp'])
        cdir = os.getcwd()
        os.chdir('/tmp')
        for root, file in self.jar_files:
            ret = subprocess.call(['jar', 'xf', file, 'META-INF/MANIFEST.MF'])
            assert ret == 0
            manifest_des = open('META-INF/MANIFEST.MF', 'r')
            manifest_file = manifest_des.read()
            #print manifest_file
            parser = manifest.ManifestParser()
            bundle = parser.parse(manifest_file)
            bundle.root = root
            bundle.file = file
            bundle.is_binary_bundle = True
            if bundle.sym_name == '':
                #print 'Bundle '+join(root, file)+' has no symbolic name; skipping it'
                if not (bundle.file == 'aspectjrt.jar' or \
                        bundle.file == 'aspectjweaver.jar' or\
                        bundle.file == 'cglib-nodep_2.2.jar' or \
                        bundle.file == 'RXTXcomm.jar'):
                        
                    print '------------------------------------------------------------------------------------>'+str(bundle.file)+'<---'
                    assert False
                    
                continue
                

                
            assert bundle.sym_name != ''
            assert not bundle.sym_name in self.unique_bundles
            self.unique_bundles[bundle.sym_name] = bundle
            self.bundles.append(bundle)
            if not(bundle.file in do_not_package_libs):
                self.target_platform[join(bundle.root,bundle.file)] =\
                    (bundle.root, bundle.file, False)
                
        os.chdir(cdir)
            
    def display(self):
        for i in self.bundles:
            i.display()
            print '-'*80
        
    def find(self, jar_path):
        for i in jar_path:
            #print 'jar_path: ', i
            for root, dirs, files in os.walk(i):
                for dir in dirs:
                    if dir in bundle_dirs:
                        self.target_platform[join(root,dir)] = (root, dir, True)
                for file in files:
                    if file.endswith(r'.jar'):
                        self.jar_files.append((root, file))
                        
                        
       
class Src:
    def __init__(self):
        self.src_manifests = []
        self.src_files = []
        self.bundles = []
        
    def find_libs(self, path):
        libs = {}
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(r'.jar'):
                    libs[join(root, file)] = join(root, file)
        return libs
        
    def load(self):
        for root, dir, libs in self.src_manifests:
            #print join(root, dir, 'MANIFEST.MF')
            manifest_des = open(join(root, dir, 'MANIFEST.MF'), 'r')
            manifest_file = manifest_des.read()
            #print manifest_file
            parser = manifest.ManifestParser()
            bundle = parser.parse(manifest_file)
            bundle.root = root
            #print bundle, bundle.sym_name
            if libs.keys().__len__() > 0:
                #print libs
                bundle.extra_libs = libs
                #assert False
            self.bundles.append(bundle)
            
    def display(self):
        for i in self.bundles:
            i.display()
            print '-'*80
        
    def find(self, src_path):
        for i in src_path:
            for root, dirs, files in os.walk(i):
                libs = {}
                manifest = ()
                manifest_found = False
                
                if 'META-INF' in dirs:
                    manifest_found = True
                else:
                    continue
                    
                for dir in dirs:
                    if dir == 'META-INF':
                        manifest = (root, dir)
                    if dir == 'lib':
                        libs = self.find_libs(join(root, dir))
                        #print libs
                        #assert False
                        
                manifest += (libs,)
                self.src_manifests.append(manifest)
                    
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
        display_jars_help = 'Display Java archives'
        display_src_help = 'Display sources'
        check_dep_help = 'Check dependencies'
        build_gen_help = 'Generate build artifacts'
        loglevel_help = 'set the logging level; valid values are debug, info, '\
                        'warn, error and critical'

        #; if no options are given, '\
        #                 'then this command is executed; supported values'\
        #                 ' are: ant, make, maven; default value is: ant.'
        self.parser.add_option("-j", "--display-jars", action="store_true",
                                default=False, dest="display_jars",
                                help=display_jars_help)
        self.parser.add_option("-s", "--display-src", action="store_true",
                                default=False, dest="display_src",
                                help=display_src_help)
        self.parser.add_option("-c", "--check-dep", action="store_true",
                               default=False, dest="check_dep",
                               help=check_dep_help)
        self.parser.add_option('-l', '--logging-level', dest='loglevel',
                               metavar='LEVEL', help=loglevel_help)
        self.parser.add_option("-b", "--build-gen", action="store_true",
                               default=False, dest="build_gen",
                               help=build_gen_help)
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
            
def load_jars():
    jfinder = BinaryBundleFinder()
    jfinder.find(jar_path, bundle_dirs)
    jfinder.load(do_not_package_libs)
    return jfinder
    
def load_src():
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
        
if __name__ == '__main__':
    jars = None
    src = None
    deps = None
    cmd_set = False        
    params = Parameters()
    
    if params.options.display_jars:
        print '-'*80
        jars = load_jars()
        jars.display()
        cmd_set = True
 
    if params.options.display_src:
        if not cmd_set:
            print '-'*80
        src = load_src()
        src.display()
        cmd_set = True
        
    if params.options.check_dep:
        if not jars:
            jars = load_jars()
               
        if not src:
            src = load_src()
                
        #jars.display()
        #src.display()
            
        deps = Dep(jars, src, jars.target_platform)
        assert deps.resolve()
        assert deps.sort()
        cmd_set = True
        
    if params.options.build_gen or not cmd_set:
        if jars == None:
            jars = load_jars()
               
        if src == None:
            src = load_src()
                
        if deps == None:
            deps = Dep(jars, src, jars.target_platform)
            assert deps.resolve()
            assert deps.sort()
            
        writer = FileWriter()
        gen = AntGenerator(project_name, deps.jars, deps.src.bundles,
                           deps.target_platform, '.', writer)
        gen.generate_build_files()
        
    #else:
    #    params.parser.print_version()
    #    params.parser.print_help()

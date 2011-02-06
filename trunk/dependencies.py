#!/usr/bin/env python
#
#    
#    James Percent (james@empty-set.net)
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

import os
import manifest
import subprocess
import logging
import tempfile
import shutil
from os.path import join, abspath

logger = logging.getLogger(__name__)
def set_logger_level(logLevel):
    logger.setLevel(logLevel)

class BinaryBundleFinder:
    def __init__(self):
        self.jar_files = []
        self.bundles = []
        self.unique_bundles = {}
        self.target_platform = {}
        
    def load(self, do_not_package_libs):
        tmp = tempfile.mkdtemp()
        #print tmp
        for root, file in self.jar_files:
            shutil.copy(join(root, file), tmp)
        cdir = os.getcwd()

        for root, file in self.jar_files:
            os.chdir(tmp)
            ret = subprocess.call(['jar', 'xf', join(tmp,file),
                                   join('META-INF','MANIFEST.MF')])
            assert ret == 0
            os.chdir(cdir)
            manifest_des = open(join(tmp, 'META-INF','MANIFEST.MF'), 'r')
            manifest_file = manifest_des.read()
            shutil.rmtree(join(tmp, 'META-INF'))
            logger.debug(manifest_file)
            parser = manifest.ManifestParser()
            bundle = parser.parse(manifest_file)
            if bundle == None:
                continue    
            bundle.root = root
            bundle.file = file
            bundle.is_binary_bundle = True
            if bundle.sym_name == '':
                logger.info('Bundle '+join(root, file)+' has no symbolic name;'\
                            ' skipping it')
                continue
            
            assert bundle.sym_name != ''
            assert not bundle.sym_name in self.unique_bundles
            self.unique_bundles[bundle.sym_name] = bundle
            self.bundles.append(bundle)
            if not(bundle.file in do_not_package_libs):
                self.target_platform[join(bundle.root,bundle.file)] =\
                    (bundle.root, bundle.file, False)
        shutil.rmtree(tmp)
            
    def display(self):
        for i in self.bundles:
            i.display()
            print '-'*80
        
    def find(self, jar_path, bundle_dirs):
        for i in jar_path:
            logger.debug('jar_path: '+str(i))
            for root, dirs, files in os.walk(i):
                for dir in dirs:
                    if dir in bundle_dirs:
                        self.target_platform[join(root,dir)] = (root, dir, True)
                for file in files:
                    if file.endswith(r'.jar'):
                        self.jar_files.append((root, file))
                        
                        
       
class SourceBundleFinder:
    def __init__(self):
        self.src_manifests = []
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
            logger.debug(join(root, dir, 'MANIFEST.MF'))
            manifest_des = open(join(root, dir, 'MANIFEST.MF'), 'r')
            manifest_file = manifest_des.read()
            logger.debug(manifest_file)
            parser = manifest.ManifestParser()
            bundle = parser.parse(manifest_file)
            bundle.root = root
            logger.debug(bundle, bundle.sym_name)
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
                        
                manifest += (libs,)
                self.src_manifests.append(manifest)


class Dependencies:
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
                    logger.error('circular dependencies are not supported.')
                    assert False
                        
                #print 'bundle ', bundle, bundle.sym_name, '=', bundle.build_level                
                #print 'dep bundle ', dep_bundle, dep_bundle.sym_name,'=',\
                # dep_bundle.build_level
                
            if dep_bundle.build_level >= bundle.build_level and\
                                         not dep_bundle.is_binary_bundle:
                #print 'matched: ', bundle.sym_name, ' deps on ',\
                # dep_bundle.sym_name
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
                #print 'Bundle '+str(bundle.sym_name)+\
                #' found both binary and src;'+\
                #' using the src version (this should be an option)'
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
                print 'required bundle', bundle.sym_name, \
                    required_bundle_info.name
                
                if required_bundle_info.name in bundles and \
                    required_bundle_info.is_in_range(\
                        bundles[required_bundle_info.name].version):
                    found = True
                    
                    if bundle.fragment and\
                        bundle.sym_name == 'com.ambient.labtrack.test':
                        
                        print 'adding dep '+str(required_bundle_info.name)+\
                           '-'+str(bundles[required_bundle_info.name].version),\
                           ' to ', bundle.sym_name
                        
                    print 'Adding the dep bundle = ', required_bundle_info.name,\
                           bundles[required_bundle_info.name]
                    
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
                            #print 'adding dep '+ex_bundle.sym_name+' to '+\
                            #bundle.sym_name, 'because of package ', package.name
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
                            
                        print 'ERROR: cannot find the correct version of '+\
                              package.name+' for '+bundle.sym_name+\
                              '; requires '+package.__str__()+' found = '+found_str
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
    

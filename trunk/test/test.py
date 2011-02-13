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

import unittest
import pdb
import sys
from os.path import join

sys.path.append('../.')

import auto_builder
import dependencies
import generator
import manifest
from auto_builder import *
from dependencies import *
from manifest import *
from generator import *

auto_builder.set_logger_level(logging.WARN)

###############################################################################
#
# manifest.py tests
#
class manifest_test(unittest.TestCase):
    def set_version(self, v, m, mi, mic, qual):
        v.set_major(m)        
        v.set_minor(mi)
        v.set_micro(mic)
        v.set_qual(qual)
        return v
    
    def test_bundle_dir_manifest(self):
        test_manifest_file = open(\
            './gnu_io.manifest.mf', 'r')
        test = test_manifest_file.read()
        parser = ManifestParser()
        bundle = parser.parse(test)
        #print bundle.epackages[0].name, bundle.classpath_jars
        self.assertEquals(1, bundle.epackages.__len__())
        self.assertEquals('gnu.io', bundle.epackages[0].name)
        classpath_jars = set(bundle.classpath_jars)
        self.assertTrue('RXTXcomm.jar' in classpath_jars)
        self.assertTrue('../RXTXcomm-1.1.jar' in classpath_jars)
        
    def test_manifest_parser(self):
        test_manifest_file = open(\
            './com.springsource.org.apache.log4j-1.2.15.manifest.mf', 'r')
        test = test_manifest_file.read()
    
        parser = ManifestParser()
        bundle = parser.parse(test)
       
        for i in bundle.epackages: 
            if i.name =='org.apache.log4j':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())

            elif i.name == 'org.apache.log4j.chainsaw':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
                
            elif i.name == 'org.apache.log4j.config':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.helpers':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())    
            elif i.name == 'org.apache.log4j.jdbc':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.jmx':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.lf5':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.lf5.config':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.lf5.util':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.lf5.viewer':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.lf5.viewer.categoryexplorer':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.lf5.viewer.configure':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())        
            elif i.name == 'org.apache.log4j.lf5.viewer.images':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.net':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.nt':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.or':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.or.jms':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.or.sax':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.spi':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.varia':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__())
            elif i.name == 'org.apache.log4j.xml':
                self.assertEquals(True, i.b_inclusive)
                self.assertEquals('1.2.15', i.b_version.__str__())
                self.assertEquals(False, i.e_inclusive)
                self.assertEquals(str(sys.maxint),i.e_version.__str__()) 
            else:
                print i.name
                self.assertTrue(False)
                
            for i in bundle.ipackages: 
                if i.name =='com.sun.jdmk.comm':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('5.1.0', i.b_version.__str__())
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals('5.1.0',i.e_version.__str__())
                    
                elif i.name == 'javax.jms':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('1.1.0', i.b_version.__str__())
                    self.assertEquals(False,i.e_inclusive)
                    self.assertEquals('2.0.0',i.e_version.__str__())
                    
                elif i.name =='javax.mail':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('1.4.0', i.b_version.__str__())
                    self.assertEquals(False, i.e_inclusive)
                    self.assertEquals('2.0.0',i.e_version.__str__())
                    
                elif i.name == 'javax.mail.internet':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('1.4.0', i.b_version.__str__())
                    self.assertEquals(False, i.e_inclusive)
                    self.assertEquals('2.0.0',i.e_version.__str__())
                    
                elif i.name == 'javax.management':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)
                    
                elif i.name == 'javax.naming':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)
                    
                elif i.name == 'javax.swing':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)                    
                    
                elif i.name == 'javax.swing.border':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)                    
                    
                elif i.name == 'javax.swing.event':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)                    
                    
                elif i.name == 'javax.swing.table':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)
                    
                elif i.name == 'javax.swing.text':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)
                    
                elif i.name == 'javax.swing.tree':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)

                elif i.name == 'javax.xml.parsers':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)
                    
                elif i.name == 'org.w3c.dom':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)
                    
                elif i.name == 'org.xml.sax':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)
                    
                elif i.name == 'org.xml.sax.helpers':
                    self.assertEquals(True, i.b_inclusive)
                    self.assertEquals('0', i.b_version.major)
                    self.assertEquals(True, i.e_inclusive)
                    self.assertEquals(str(sys.maxint),i.e_version.major)
                    
                else:
                    print i.name
                    self.assertTrue(False)  
    
    def test_bundle_version(self):
        test = 'Bundle-Version: 3.5.2.R35x_v20100126\n'
        p = ManifestParser()
        bundle = p.parse(test)
        self.assertEquals(bundle.version.__str__(), '3.5.2.R35x_v20100126')
        
    def test_export_package(self):
        test = 'Export-Package: org.apache.commons.pool;version=1.4, org.apache.common\r\n s.pool.impl;version=1.4'
        p = ManifestParser()
        bundle = p.parse(test)
        self.assertEquals(2, bundle.epackages.__len__())
        self.assertEquals(bundle.epackages[0].name, 'org.apache.commons.pool')
        self.assertEquals(bundle.epackages[0].b_version.__str__(), '1.4')
        self.assertEquals(bundle.epackages[0].e_version.__str__(), str(sys.maxint))
        self.assertEquals(bundle.epackages[1].name, 'org.apache.commons.pool.impl')
        self.assertEquals(bundle.epackages[1].b_version.__str__(), '1.4')
        self.assertEquals(bundle.epackages[1].e_version.__str__(), str(sys.maxint))
        
    def test_version(self):
        v = Version()
        v1 = Version()
        v = self.set_version(v, 1 , 3, 3, '7')
        v1 = self.set_version(v1, 1, 3, 3, '7')
        self.assertEquals(True, v.is_equal(v1))
        self.assertEquals(False, v.is_less(v1))
        
        self.set_version(v, 1, 2, 3, '7')
        
        self.assertEquals(False, v.is_equal(v1))
        self.assertEquals(False, v.is_less(v1))
        self.assertEquals(True, v1.is_less(v))
        
        self.set_version(v, 1, 3, 2, '7')
        self.assertEquals(False, v.is_equal(v1))
        self.assertEquals(False, v.is_less(v1))
        self.assertEquals(True, v1.is_less(v))
        
        self.set_version(v, 1, 3, 3, '6')
        self.assertEquals(False, v.is_equal(v1))
        self.assertEquals(False, v.is_less(v1))
        self.assertEquals(True, v1.is_less(v))
        
        self.set_version(v, 3, 1, 3, '3')
        self.assertEquals(False, v.is_equal(v1))
        self.assertEquals(True, v.is_less(v1))
        self.assertEquals(False, v1.is_less(v))
        
        v2 = Version()
        v3 = Version()
        
        v2.set_major(3)
        v2.set_minor(3)
        v2.set_micro(0)
        
        v3.set_major(3)
        v3.set_minor(3)
        
        self.assertEquals(False, v3.is_less(v2))
        self.assertEquals(False, v2.is_less(v3))
        self.assertEquals(True, v2.is_equal(v3))
        self.assertEquals(True, v3.is_equal(v2))
        
    def test_package(self):
        i = Package('java.lang.whatever')
        v = Version()
        i.set_version_range(v, True, v, True)
        self.assertEquals(True, i.is_in_range(v))
        v1 = Version()
        self.set_version(v, 1, 3, 3, '7')
        self.set_version(v1, 3, 1, 4, '1')
        i.set_version_range(v, True, v1, False)
        
        self.assertEquals(True, i.is_in_range(v))
        self.assertEquals(False, i.is_in_range(v1))
        
        i.set_version_range(v, True, v1, True)
        self.assertEquals(True, i.is_in_range(v))
        self.assertEquals(True, i.is_in_range(v1))
        
        i.set_version_range(v, False, v1, True)
        self.assertEquals(False, i.is_in_range(v))
        self.assertEquals(True, i.is_in_range(v1))
        
        v2 = Version()
        self.set_version(v2, 1, 6, 1, '8')
        self.assertEquals(True, i.is_in_range(v2))
        i.set_version_range(v, False, v1, False)
        self.assertEquals(True, i.is_in_range(v2))
        i.set_version_range(v, True, v1, False)
        self.assertEquals(True, i.is_in_range(v2))
        i.set_version_range(v, True, v1, True)
        self.assertEquals(True, i.is_in_range(v2))
        i1 = Package('org.eclipse.sucks.my.b41135')
        
        self.assertEquals(True, i.is_in_range(v))
        self.assertEquals(True, i.is_in_range(v1))
        self.assertEquals(True, i.is_in_range(v2))
        
        v2 = Version()
        v3 = Version()

        v2.set_major(3)
        v2.set_minor(3)
        v2.set_micro(0)

        v3.set_major(3)
        v3.set_minor(3)
        
        m = Package('java.is.teh.s0x0r')
        m1 = Package('java.is.teh.s0x0r')
        
        m.set_version_range(v2, True, v2, True)
        m1.set_version_range(v3, True, v3, True)
        
        self.assertEquals(True, m.is_in_range(m1.b_version))
        self.assertEquals(True, m1.is_in_range(m.b_version))
        

###############################################################################
#
# auto_builder.py Tests
#
class ParametersTest(unittest.TestCase):
    def testLogLevels(self):
        conf.library_path = [os.getcwd()]
        conf.source_path = [os.getcwd()]        
        params = auto_builder.Parameters()
        self.assertEquals(logging.WARN, auto_builder.logger.getEffectiveLevel())
        
        sys.argv = [sys.argv[0], '-l', 'debug']
        params = auto_builder.Parameters()
        self.assertEquals(logging.DEBUG, auto_builder.logger.getEffectiveLevel())
        
        sys.argv = [sys.argv[0], '-l', 'info']
        params = auto_builder.Parameters()
        self.assertEquals(logging.INFO, auto_builder.logger.getEffectiveLevel())
        
        sys.argv = [sys.argv[0], '-l', 'warn']
        params = auto_builder.Parameters()
        self.assertEquals(logging.WARN, auto_builder.logger.getEffectiveLevel())
        
        sys.argv = [sys.argv[0], '-l', 'error']
        params = auto_builder.Parameters()
        self.assertEquals(logging.ERROR, auto_builder.logger.getEffectiveLevel())
        
        sys.argv = [sys.argv[0], '-l', 'critical']
        params = auto_builder.Parameters()
        self.assertEquals(logging.CRITICAL, auto_builder.logger.getEffectiveLevel())
    
        sys.argv = [sys.argv[0], '-l', 'notaloglevel']
        params = auto_builder.Parameters()
        self.assertEquals(logging.WARN, auto_builder.logger.getEffectiveLevel())
        
        sys.argv = [sys.argv[0], '-l', 'stillnotaloglevel']
        params = auto_builder.Parameters()
        self.assertEquals(logging.WARN, auto_builder.logger.getEffectiveLevel())
    
    
    def testOptions(self):
        conf.library_path = [os.getcwd()]
        conf.source_path = [os.getcwd()]
        conf.project_name = ''
        sys.argv = [sys.argv[0], '-j']
        params = auto_builder.Parameters()
        self.assertEquals(True, params.options.display_jars)
        self.assertEquals(False, params.options.display_src)
        self.assertEquals(False, params.options.check_dep)
        self.assertEquals(False, params.options.build_gen)
        self.assertEquals('', params.options.library_path)
        self.assertEquals('', params.options.source_path)
        self.assertEquals('', params.options.project_name)
        
        sys.argv = [sys.argv[0], '-j', '-d']
        params = auto_builder.Parameters()
        self.assertEquals(True, params.options.display_jars)
        self.assertEquals(True, params.options.display_src)
        self.assertEquals(False, params.options.check_dep)
        self.assertEquals(False, params.options.build_gen)
        self.assertEquals('', params.options.library_path)
        self.assertEquals('', params.options.source_path)
        self.assertEquals('', params.options.project_name)
        
        sys.argv = [sys.argv[0], '-c']
        params = auto_builder.Parameters()
        self.assertEquals(False, params.options.display_jars)
        self.assertEquals(False, params.options.display_src)
        self.assertEquals(True, params.options.check_dep)
        self.assertEquals(False, params.options.build_gen)
        self.assertEquals('', params.options.library_path)
        self.assertEquals('', params.options.source_path)
        self.assertEquals('', params.options.project_name)
        
        sys.argv = [sys.argv[0], '-b']
        params = auto_builder.Parameters()
        self.assertEquals(False, params.options.display_jars)
        self.assertEquals(False, params.options.display_src)
        self.assertEquals(False, params.options.check_dep)
        self.assertEquals(True, params.options.build_gen)
        self.assertEquals('', params.options.library_path)
        self.assertEquals('', params.options.source_path)
        self.assertEquals('', params.options.project_name)
        
        sys.argv = [sys.argv[0], '-b', '-p', '.']
        params = auto_builder.Parameters()
        self.assertEquals(False, params.options.display_jars)
        self.assertEquals(False, params.options.display_src)
        self.assertEquals(False, params.options.check_dep)
        self.assertEquals(True, params.options.build_gen)
        self.assertEquals('.', params.options.library_path)
        self.assertEquals('', params.options.source_path)
        self.assertEquals('', params.options.project_name)
        
        sys.argv = [sys.argv[0], '-j', '-s', '.']
        params = auto_builder.Parameters()
        self.assertEquals(True, params.options.display_jars)
        self.assertEquals(False, params.options.display_src)
        self.assertEquals(False, params.options.check_dep)
        self.assertEquals(False, params.options.build_gen)
        self.assertEquals('', params.options.library_path)
        self.assertEquals('.', params.options.source_path)
        self.assertEquals('', params.options.project_name)
        
        sys.argv = [sys.argv[0], '-j', '-s', '.', '-p', '.']
        params = auto_builder.Parameters()
        self.assertEquals(True, params.options.display_jars)
        self.assertEquals(False, params.options.display_src)
        self.assertEquals(False, params.options.check_dep)
        self.assertEquals(False, params.options.build_gen)
        self.assertEquals('.', params.options.library_path)
        self.assertEquals('.', params.options.source_path)
        self.assertEquals('', params.options.project_name)
        
        sys.argv = [sys.argv[0], '-b', '-n', 'james-r0x0rz']
        params = auto_builder.Parameters()
        self.assertEquals(False, params.options.display_jars)
        self.assertEquals(False, params.options.display_src)
        self.assertEquals(False, params.options.check_dep)
        self.assertEquals(True, params.options.build_gen)
        self.assertEquals('', params.options.library_path)
        self.assertEquals('', params.options.source_path)
        self.assertEquals('james-r0x0rz', params.options.project_name)
        
        sys.argv = [sys.argv[0], '-j']
        
        conf.library_path = 'lkjadslfjks#1@@!@!!%%(@*!*!()(0adflajjaldf'
        caught = False
        try:
            params = auto_builder.Parameters()
        except:
            caught = True
        self.assertTrue(caught)
        
        conf.library_path = '.'
        caught = False
        try:
            params = auto_builder.Parameters()
        except:
            caught = True
        self.assertFalse(caught)
        
        conf.source_path = 'lkjadslfjks#1@@!@!!%%(@*!*!()(0adflajjaldf'
        caught = False
        try:
            params = auto_builder.Parameters()
        except:
            caught = True
        self.assertTrue(caught)
        
        conf.source_path = '.'
        caught = False
        try:
            params = auto_builder.Parameters()
        except:
            caught = True
        self.assertFalse(caught)
        
        bad_name = 'alkdfjoi?##@!#*!?91039102*Ulkajdlfaj8ie'
        sys.argv = [sys.argv[0], '-j', '-s',
                    bad_name, '-p', '.']
        caught = False
        try:
            params = auto_builder.Parameters()
        except:
            caught = True
        self.assertTrue(caught)

        sys.argv = [sys.argv[0], '-j', '-s',
                    bad_name, '-p', bad_name]
        caught = False
        try:
            params = auto_builder.Parameters()
        except:
            caught = True
        self.assertTrue(caught)


        sys.argv = [sys.argv[0], '-j', '-s', '.', '-p', bad_name]
        caught = False
        try:
            params = auto_builder.Parameters()
        except:
            caught = True
        self.assertTrue(caught)


        sys.argv = [sys.argv[0], '-j', '-s', '.', '-p', '.']
        caught = False
        try:
            params = auto_builder.Parameters()
        except:
            caught = True
        self.assertFalse(caught)


###############################################################################
#
# dependencies.py tests
#

class TestDependencies(unittest.TestCase):
    def testAddPackage(self):
        #, exports, package, bundle):
        
        bfinder = BinaryBundleFinder()
        jar_path = ['testlib']
        bfinder.find(jar_path)
        bfinder.load()
        
        sfinder = SourceBundleFinder()
        src_path = ['org.syndeticlogic.minerva',
                    'org.syndeticlogic.minerva.tools']
        sfinder.find(src_path)
        sfinder.load()
        
        deps = Dependencies(bfinder, sfinder, bfinder.target_platform)
        
        deps.resolve()

        bundles_epackages = { 
        'org.rifidi.org.apache.mina-core' : (
        'org.apache.mina.common' , 
        'org.apache.mina.common.support' , 
        'org.apache.mina.filter' , 
        'org.apache.mina.filter.codec' , 
        'org.apache.mina.filter.codec.demux' , 
        'org.apache.mina.filter.codec.serialization' , 
        'org.apache.mina.filter.codec.support' , 
        'org.apache.mina.filter.codec.textline' , 
        'org.apache.mina.filter.executor' , 
        'org.apache.mina.handler' , 
        'org.apache.mina.handler.chain' , 
        'org.apache.mina.handler.demux' , 
        'org.apache.mina.handler.multiton' , 
        'org.apache.mina.handler.support' , 
        'org.apache.mina.management' , 
        'org.apache.mina.transport.socket.nio' , 
        'org.apache.mina.transport.socket.nio.support' , 
        'org.apache.mina.transport.vmpipe' , 
        'org.apache.mina.transport.vmpipe.support' , 
        'org.apache.mina.util' , 
        ), 
        'org.apache.geronimo.specs.geronimo-j2ee-management_1.1_spec' : (
        'javax.management.j2ee.statistics' , 
        'javax.management.j2ee' , 
        ), 
        'org.springframework.orm' : (
        'org.springframework.orm' , 
        'org.springframework.orm.hibernate3' , 
        'org.springframework.orm.hibernate3.annotation' , 
        'org.springframework.orm.hibernate3.support' , 
        'org.springframework.orm.ibatis' , 
        'org.springframework.orm.ibatis.support' , 
        'org.springframework.orm.jdo' , 
        'org.springframework.orm.jdo.support' , 
        'org.springframework.orm.jpa' , 
        'org.springframework.orm.jpa.persistenceunit' , 
        'org.springframework.orm.jpa.support' , 
        'org.springframework.orm.jpa.vendor' , 
        'org.springframework.orm.toplink' , 
        'org.springframework.orm.toplink.support' , 
        ), 
        'org.rifidi.org.springframework.aop' : (
        'org.springframework.aop' , 
        'org.springframework.aop.aspectj' , 
        'org.springframework.aop.aspectj.annotation' , 
        'org.springframework.aop.aspectj.autoproxy' , 
        'org.springframework.aop.config' , 
        'org.springframework.aop.framework' , 
        'org.springframework.aop.framework.adapter' , 
        'org.springframework.aop.framework.autoproxy' , 
        'org.springframework.aop.framework.autoproxy.target' , 
        'org.springframework.aop.interceptor' , 
        'org.springframework.aop.scope' , 
        'org.springframework.aop.support' , 
        'org.springframework.aop.support.annotation' , 
        'org.springframework.aop.target' , 
        'org.springframework.aop.target.dynamic' , 
        ), 
        'org.springframework.web' : (
        'org.springframework.remoting.caucho' , 
        'org.springframework.remoting.httpinvoker' , 
        'org.springframework.remoting.jaxrpc' , 
        'org.springframework.remoting.jaxrpc.support' , 
        'org.springframework.remoting.jaxws' , 
        'org.springframework.web' , 
        'org.springframework.web.context' , 
        'org.springframework.web.context.request' , 
        'org.springframework.web.context.support' , 
        'org.springframework.web.filter' , 
        'org.springframework.web.jsf' , 
        'org.springframework.web.jsf.el' , 
        'org.springframework.web.util' , 
        ), 
        'org.springframework.web.servlet' : (
        'org.springframework.web.bind' , 
        'org.springframework.web.bind.annotation' , 
        'org.springframework.web.bind.annotation.support' , 
        'org.springframework.web.bind.support' , 
        'org.springframework.web.multipart' , 
        'org.springframework.web.multipart.commons' , 
        'org.springframework.web.multipart.support' , 
        'org.springframework.web.servlet' , 
        'org.springframework.web.servlet.handler' , 
        'org.springframework.web.servlet.handler.metadata' , 
        'org.springframework.web.servlet.i18n' , 
        'org.springframework.web.servlet.mvc' , 
        'org.springframework.web.servlet.mvc.annotation' , 
        'org.springframework.web.servlet.mvc.multiaction' , 
        'org.springframework.web.servlet.mvc.support' , 
        'org.springframework.web.servlet.mvc.throwaway' , 
        'org.springframework.web.servlet.support' , 
        'org.springframework.web.servlet.tags' , 
        'org.springframework.web.servlet.tags.form' , 
        'org.springframework.web.servlet.theme' , 
        'org.springframework.web.servlet.view' , 
        'org.springframework.web.servlet.view.document' , 
        'org.springframework.web.servlet.view.freemarker' , 
        'org.springframework.web.servlet.view.jasperreports' , 
        'org.springframework.web.servlet.view.tiles2' , 
        'org.springframework.web.servlet.view.velocity' , 
        'org.springframework.web.servlet.view.xslt' , 
        ), 
        'com.springsource.javax.persistence' : (
        'javax.persistence' , 
        'javax.persistence.spi' , 
        ), 
        'org.apache.felix.bundlerepository' : (
        'org.osgi.service.obr' , 
        ), 
        'com.springsource.javax.xml.bind' : (
        'javax.xml.bind' , 
        'javax.xml.bind.annotation' , 
        'javax.xml.bind.annotation.adapters' , 
        'javax.xml.bind.attachment' , 
        'javax.xml.bind.helpers' , 
        'javax.xml.bind.util' , 
        ), 
        'com.springsource.javax.servlet.jsp' : (
        'javax.servlet.jsp' , 
        'javax.servlet.jsp.el' , 
        'javax.servlet.jsp.resources' , 
        'javax.servlet.jsp.tagext' , 
        ), 
        'javax.servlet' : (
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.servlet.resources' , 
        ), 
        'com.mysql.jdbc' : (
        'com.mysql.jdbc' , 
        'com.mysql.jdbc.jdbc2.optional' , 
        'com.mysql.jdbc.log' , 
        'com.mysql.jdbc.profiler' , 
        'com.mysql.jdbc.util' , 
        'com.mysql.jdbc.exceptions' , 
        'com.mysql.jdbc.exceptions.jdbc4' , 
        'com.mysql.jdbc.interceptors' , 
        'com.mysql.jdbc.integration.c3p0' , 
        'com.mysql.jdbc.integration.jboss' , 
        'com.mysql.jdbc.configs' , 
        'org.gjt.mm.mysql' , 
        ), 
        'org.rifidi.org.llrp.ltk' : (
        'org.llrp.ltk.exceptions' , 
        'org.llrp.ltk.generated' , 
        'org.llrp.ltk.generated.enumerations' , 
        'org.llrp.ltk.generated.interfaces' , 
        'org.llrp.ltk.generated.messages' , 
        'org.llrp.ltk.generated.parameters' , 
        'org.llrp.ltk.net' , 
        'org.llrp.ltk.types' , 
        'org.llrp.ltk.util' , 
        ), 
        'org.apache.geronimo.specs.geronimo-jms_1.1_spec' : (
        'javax.jms' , 
        ), 
        'org.springframework.transaction' : (
        'org.springframework.dao' , 
        'org.springframework.dao.annotation' , 
        'org.springframework.dao.support' , 
        'org.springframework.jca.cci' , 
        'org.springframework.jca.cci.connection' , 
        'org.springframework.jca.cci.core' , 
        'org.springframework.jca.cci.core.support' , 
        'org.springframework.jca.cci.object' , 
        'org.springframework.jca.context' , 
        'org.springframework.jca.endpoint' , 
        'org.springframework.jca.support' , 
        'org.springframework.jca.work' , 
        'org.springframework.jca.work.glassfish' , 
        'org.springframework.jca.work.jboss' , 
        'org.springframework.transaction' , 
        'org.springframework.transaction.annotation' , 
        'org.springframework.transaction.config' , 
        'org.springframework.transaction.interceptor' , 
        'org.springframework.transaction.jta' , 
        'org.springframework.transaction.support' , 
        ), 
        'org.apache.derby' : (
        'org.apache.derby.authentication' , 
        'org.apache.derby.catalog' , 
        'org.apache.derby.catalog.types' , 
        'org.apache.derby.client' , 
        'org.apache.derby.client.am' , 
        'org.apache.derby.client.am.stmtcache' , 
        'org.apache.derby.client.net' , 
        'org.apache.derby.database' , 
        'org.apache.derby.diag' , 
        'org.apache.derby.drda' , 
        'org.apache.derby.iapi.db' , 
        'org.apache.derby.iapi.error' , 
        'org.apache.derby.iapi.jdbc' , 
        'org.apache.derby.iapi.reference' , 
        'org.apache.derby.iapi.security' , 
        'org.apache.derby.iapi.services.cache' , 
        'org.apache.derby.iapi.services.classfile' , 
        'org.apache.derby.iapi.services.compiler' , 
        'org.apache.derby.iapi.services.context' , 
        'org.apache.derby.iapi.services.crypto' , 
        'org.apache.derby.iapi.services.daemon' , 
        'org.apache.derby.iapi.services.diag' , 
        'org.apache.derby.iapi.services.i18n' , 
        'org.apache.derby.iapi.services.info' , 
        'org.apache.derby.iapi.services.io' , 
        'org.apache.derby.iapi.services.jmx' , 
        'org.apache.derby.iapi.services.loader' , 
        'org.apache.derby.iapi.services.locks' , 
        'org.apache.derby.iapi.services.memory' , 
        'org.apache.derby.iapi.services.monitor' , 
        'org.apache.derby.iapi.services.property' , 
        'org.apache.derby.iapi.services.sanity' , 
        'org.apache.derby.iapi.services.stream' , 
        'org.apache.derby.iapi.services.timer' , 
        'org.apache.derby.iapi.services.uuid' , 
        'org.apache.derby.iapi.sql' , 
        'org.apache.derby.iapi.sql.compile' , 
        'org.apache.derby.iapi.sql.conn' , 
        'org.apache.derby.iapi.sql.depend' , 
        'org.apache.derby.iapi.sql.dictionary' , 
        'org.apache.derby.iapi.sql.execute' , 
        'org.apache.derby.iapi.store.access' , 
        'org.apache.derby.iapi.store.access.conglomerate' , 
        'org.apache.derby.iapi.store.access.xa' , 
        'org.apache.derby.iapi.store.raw' , 
        'org.apache.derby.iapi.store.raw.data' , 
        'org.apache.derby.iapi.store.raw.log' , 
        'org.apache.derby.iapi.store.raw.xact' , 
        'org.apache.derby.iapi.store.replication.master' , 
        'org.apache.derby.iapi.store.replication.slave' , 
        'org.apache.derby.iapi.tools.i18n' , 
        'org.apache.derby.iapi.types' , 
        'org.apache.derby.iapi.util' , 
        'org.apache.derby.impl.db' , 
        'org.apache.derby.impl.drda' , 
        'org.apache.derby.impl.io' , 
        'org.apache.derby.impl.io.vfmem' , 
        'org.apache.derby.impl.jdbc' , 
        'org.apache.derby.impl.jdbc.authentication' , 
        'org.apache.derby.impl.load' , 
        'org.apache.derby.impl.services.bytecode' , 
        'org.apache.derby.impl.services.cache' , 
        'org.apache.derby.impl.services.daemon' , 
        'org.apache.derby.impl.services.jce' , 
        'org.apache.derby.impl.services.jmx' , 
        'org.apache.derby.impl.services.jmxnone' , 
        'org.apache.derby.impl.services.locks' , 
        'org.apache.derby.impl.services.monitor' , 
        'org.apache.derby.impl.services.reflect' , 
        'org.apache.derby.impl.services.stream' , 
        'org.apache.derby.impl.services.timer' , 
        'org.apache.derby.impl.services.uuid' , 
        'org.apache.derby.impl.sql' , 
        'org.apache.derby.impl.sql.catalog' , 
        'org.apache.derby.impl.sql.compile' , 
        'org.apache.derby.impl.sql.conn' , 
        'org.apache.derby.impl.sql.depend' , 
        'org.apache.derby.impl.sql.execute' , 
        'org.apache.derby.impl.sql.execute.rts' , 
        'org.apache.derby.impl.store.access' , 
        'org.apache.derby.impl.store.access.btree' , 
        'org.apache.derby.impl.store.access.btree.index' , 
        'org.apache.derby.impl.store.access.conglomerate' , 
        'org.apache.derby.impl.store.access.heap' , 
        'org.apache.derby.impl.store.access.sort' , 
        'org.apache.derby.impl.store.raw' , 
        'org.apache.derby.impl.store.raw.data' , 
        'org.apache.derby.impl.store.raw.log' , 
        'org.apache.derby.impl.store.raw.xact' , 
        'org.apache.derby.impl.store.replication' , 
        'org.apache.derby.impl.store.replication.buffer' , 
        'org.apache.derby.impl.store.replication.master' , 
        'org.apache.derby.impl.store.replication.net' , 
        'org.apache.derby.impl.store.replication.slave' , 
        'org.apache.derby.impl.tools.dblook' , 
        'org.apache.derby.impl.tools.ij' , 
        'org.apache.derby.impl.tools.sysinfo' , 
        'org.apache.derby.io' , 
        'org.apache.derby.jdbc' , 
        'org.apache.derby.mbeans' , 
        'org.apache.derby.mbeans.drda' , 
        'org.apache.derby.osgi' , 
        'org.apache.derby.security' , 
        'org.apache.derby.shared.common.error' , 
        'org.apache.derby.shared.common.i18n' , 
        'org.apache.derby.shared.common.sanity' , 
        'org.apache.derby.tools' , 
        'org.apache.derby.vti' , 
        ), 
        'org.eclipse.equinox.launcher' : (
        'org.eclipse.core.launcher' , 
        'org.eclipse.equinox.internal.launcher' , 
        'org.eclipse.equinox.launcher' , 
        ), 
        'com.springsource.javax.xml.rpc' : (
        'javax.xml.messaging' , 
        'javax.xml.rpc' , 
        'javax.xml.rpc.encoding' , 
        'javax.xml.rpc.handler' , 
        'javax.xml.rpc.handler.soap' , 
        'javax.xml.rpc.holders' , 
        'javax.xml.rpc.server' , 
        'javax.xml.rpc.soap' , 
        ), 
        'com.springsource.javax.el' : (
        'javax.el' , 
        ), 
        'com.springsource.slf4j.jcl' : (
        'org.slf4j.impl' , 
        ), 
        'org.jdom' : (
        'org.jdom' , 
        'org.jdom.adapters' , 
        'org.jdom.filter' , 
        'org.jdom.input' , 
        'org.jdom.output' , 
        'org.jdom.transform' , 
        'org.jdom.xpath' , 
        ), 
        'org.apache.activemq.activemq-core' : (
        'org.apache.activemq.protobuf.compiler.parser' , 
        'org.apache.activemq.openwire.v3' , 
        'org.apache.activemq.filter' , 
        'org.apache.activemq.transaction' , 
        'org.apache.activemq.network.jms' , 
        'org.apache.activemq.selector' , 
        'org.apache.activemq.openwire.tool' , 
        'org.apache.activemq.thread' , 
        'org.apache.activemq.usage' , 
        'org.apache.activemq.jndi' , 
        'org.apache.activemq.broker.view' , 
        'org.apache.activemq.kaha.impl' , 
        'org.apache.activemq.store.kahadb' , 
        'org.apache.activemq.transport.reliable' , 
        'org.apache.activemq.store.amq' , 
        'org.apache.activemq.broker.region' , 
        'org.apache.activemq.transport' , 
        'org.apache.activemq.openwire.v4' , 
        'org.apache.activemq.transport.peer' , 
        'org.apache.activemq.transport.fanout' , 
        'org.apache.activemq.protobuf.compiler' , 
        'org.apache.activemq.broker' , 
        'org.apache.activemq.broker.region.virtual' , 
        'org.apache.activemq.transport.discovery' , 
        'org.apache.activemq.transport.failover' , 
        'org.apache.activemq.jaas' , 
        'org.apache.activemq.transport.stomp' , 
        'org.apache.activemq.openwire.v2' , 
        'org.apache.activemq.broker.cluster' , 
        'org.apache.activemq.transport.logwriters' , 
        'org.apache.activemq.management' , 
        'org.apache.activemq.kaha.impl.index' , 
        'org.apache.activemq.transport.nio' , 
        'org.apache.activemq.broker.ft' , 
        'org.apache.activemq.blob' , 
        'org.apache.activemq.xbean' , 
        'org.apache.activemq.transport.mock' , 
        'org.apache.activemq.store.jdbc' , 
        'org.apache.activemq.store.memory' , 
        'org.apache.activemq.openwire.v1' , 
        'org.apache.activemq.advisory' , 
        'org.apache.activemq.broker.util' , 
        'org.apache.activemq.jmdns' , 
        'org.apache.activemq.store' , 
        'org.apache.activemq.kaha.impl.index.hash' , 
        'org.apache.activemq.state' , 
        'org.apache.activemq.store.kahadb.data' , 
        'org.apache.activemq.transport.tcp' , 
        'org.apache.activemq.security' , 
        'org.apache.activemq.network' , 
        'org.apache.activemq.openwire' , 
        'org.apache.activemq.broker.region.policy' , 
        'org.apache.activemq.proxy' , 
        'org.apache.activemq.memory.buffer' , 
        'org.apache.activemq.wireformat' , 
        'org.apache.activemq.spring' , 
        'org.apache.activemq.transport.vm' , 
        'org.apache.activemq' , 
        'org.apache.activemq.protobuf' , 
        'org.apache.activemq.util' , 
        'org.apache.activemq.openwire.v5' , 
        'org.apache.activemq.kaha.impl.data' , 
        'org.apache.activemq.store.journal' , 
        'org.apache.activemq.broker.jmx' , 
        'org.apache.activemq.kaha.impl.index.tree' , 
        'org.apache.activemq.transport.multicast' , 
        'org.apache.activemq.plugin' , 
        'org.apache.activemq.kaha.impl.container' , 
        'org.apache.activemq.kaha.impl.async' , 
        'org.apache.activemq.memory.list' , 
        'org.apache.activemq.broker.region.group' , 
        'org.apache.activemq.transport.udp' , 
        'org.apache.activemq.store.kahadaptor' , 
        'org.apache.activemq.transport.discovery.simple' , 
        'org.apache.activemq.kaha' , 
        'org.apache.activemq.command' , 
        'org.apache.activemq.broker.region.cursors' , 
        'org.apache.activemq.transport.discovery.multicast' , 
        'org.apache.activemq.transport.discovery.rendezvous' , 
        'org.apache.activemq.memory' , 
        'org.apache.activemq.store.jdbc.adapter' , 
        'META-INF.services.org.apache.xbean.spring.http.activemq.apache.org.schema' , 
        ), 
        'com.springsource.slf4j.log4j' : (
        'org.slf4j.impl' , 
        ), 
        'com.springsource.javax.xml.stream' : (
        'javax.xml' , 
        'javax.xml.stream' , 
        'javax.xml.stream.events' , 
        'javax.xml.stream.util' , 
        ), 
        'org.springframework.core' : (
        'org.springframework.asm' , 
        'org.springframework.asm.commons' , 
        'org.springframework.asm.signature' , 
        'org.springframework.core' , 
        'org.springframework.core.annotation' , 
        'org.springframework.core.enums' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.core.style' , 
        'org.springframework.core.task' , 
        'org.springframework.core.task.support' , 
        'org.springframework.core.type' , 
        'org.springframework.core.type.classreading' , 
        'org.springframework.core.type.filter' , 
        'org.springframework.metadata' , 
        'org.springframework.metadata.commons' , 
        'org.springframework.util' , 
        'org.springframework.util.comparator' , 
        'org.springframework.util.xml' , 
        ), 
        'org.aspectj.weaver' : (
        'org.aspectj.apache.bcel' , 
        'org.aspectj.apache.bcel.classfile' , 
        'org.aspectj.apache.bcel.classfile.annotation' , 
        'org.aspectj.apache.bcel.generic' , 
        'org.aspectj.apache.bcel.util' , 
        'org.aspectj.asm' , 
        'org.aspectj.asm.internal' , 
        'org.aspectj.bridge' , 
        'org.aspectj.bridge.context' , 
        'org.aspectj.util' , 
        'org.aspectj.weaver' , 
        'org.aspectj.weaver.ast' , 
        'org.aspectj.weaver.bcel' , 
        'org.aspectj.weaver.internal.tools' , 
        'org.aspectj.weaver.loadtime' , 
        'org.aspectj.weaver.loadtime.definition' , 
        'org.aspectj.weaver.model' , 
        'org.aspectj.weaver.patterns' , 
        'org.aspectj.weaver.reflect' , 
        'org.aspectj.weaver.tools' , 
        ), 
        'org.aspectj.runtime' : (
        'org.aspectj.internal.lang.annotation' , 
        'org.aspectj.internal.lang.reflect' , 
        'org.aspectj.lang' , 
        'org.aspectj.lang.annotation' , 
        'org.aspectj.lang.internal.lang' , 
        'org.aspectj.lang.reflect' , 
        'org.aspectj.runtime' , 
        'org.aspectj.runtime.internal' , 
        'org.aspectj.runtime.internal.cflowstack' , 
        'org.aspectj.runtime.reflect' , 
        ), 
        'org.eclipse.osgi.services' : (
        'org.osgi.service.cm' , 
        'org.osgi.service.component' , 
        'org.osgi.service.device' , 
        'org.osgi.service.event' , 
        'org.osgi.service.http' , 
        'org.osgi.service.io' , 
        'org.osgi.service.log' , 
        'org.osgi.service.metatype' , 
        'org.osgi.service.provisioning' , 
        'org.osgi.service.upnp' , 
        'org.osgi.service.useradmin' , 
        'org.osgi.service.wireadmin' , 
        ), 
        'org.springframework.security.core' : (
        'org.springframework.security.event.authentication' , 
        'org.springframework.security.providers.dao.salt' , 
        'org.springframework.security.ui.basicauth' , 
        'org.springframework.security.acl.basic.jdbc' , 
        'org.springframework.security.providers.jaas.event' , 
        'org.springframework.security.providers.jaas' , 
        'org.springframework.security.acl.basic.cache' , 
        'org.springframework.security.acl' , 
        'org.springframework.security' , 
        'org.springframework.security.providers.rememberme' , 
        'org.springframework.security.vote' , 
        'org.springframework.security.authoritymapping' , 
        'org.springframework.security.ui.preauth.websphere' , 
        'org.springframework.security.providers.ldap.authenticator' , 
        'org.springframework.security.securechannel' , 
        'org.springframework.security.ui' , 
        'org.springframework.security.ui.preauth.x509' , 
        'org.springframework.security.intercept.method.aspectj' , 
        'org.springframework.security.ui.rememberme' , 
        'org.springframework.security.ui.session' , 
        'org.springframework.security.context' , 
        'org.springframework.security.context.rmi' , 
        'org.springframework.security.intercept.method' , 
        'org.springframework.security.ldap' , 
        'org.springframework.security.runas' , 
        'org.springframework.security.config' , 
        'org.springframework.security.providers.rcp' , 
        'org.springframework.security.providers.x509.cache' , 
        'org.springframework.security.providers.dao.cache' , 
        'org.springframework.security.context.httpinvoker' , 
        'org.springframework.security.providers.preauth' , 
        'org.springframework.security.userdetails.jdbc' , 
        'org.springframework.security.userdetails.ldap' , 
        'org.springframework.security.providers.dao' , 
        'org.springframework.security.acl.basic' , 
        'org.springframework.security.wrapper' , 
        'org.springframework.security.providers.x509' , 
        'org.springframework.security.intercept.web' , 
        'org.springframework.security.token' , 
        'org.springframework.security.intercept' , 
        'org.springframework.security.providers.anonymous' , 
        'org.springframework.security.ui.savedrequest' , 
        'org.springframework.security.ui.switchuser' , 
        'org.springframework.security.util' , 
        'org.springframework.security.ui.digestauth' , 
        'org.springframework.security.userdetails.hierarchicalroles' , 
        'org.springframework.security.ui.webapp' , 
        'org.springframework.security.providers' , 
        'org.springframework.security.userdetails.checker' , 
        'org.springframework.security.providers.encoding' , 
        'org.springframework.security.ldap.search' , 
        'org.springframework.security.event.authorization' , 
        'org.springframework.security.adapters' , 
        'org.springframework.security.providers.x509.populator' , 
        'org.springframework.security.userdetails.memory' , 
        'org.springframework.security.concurrent' , 
        'org.springframework.security.ui.preauth.j2ee' , 
        'org.springframework.security.providers.ldap' , 
        'org.springframework.security.ui.logout' , 
        'org.springframework.security.userdetails' , 
        'org.springframework.security.afterinvocation' , 
        'org.springframework.security.ldap.populator' , 
        'org.springframework.security.ui.preauth' , 
        'org.springframework.security.ui.x509' , 
        'org.springframework.security.ui.preauth.header' , 
        'org.springframework.security.intercept.method.aopalliance' , 
        ), 
        'com.springsource.org.apache.commons.logging' : (
        'org.apache.commons.logging' , 
        'org.apache.commons.logging.impl' , 
        ), 
        'org.springframework.context.support' : (
        'org.springframework.cache.ehcache' , 
        'org.springframework.mail' , 
        'org.springframework.mail.javamail' , 
        'org.springframework.scheduling.commonj' , 
        'org.springframework.scheduling.quartz' , 
        'org.springframework.ui.freemarker' , 
        'org.springframework.ui.jasperreports' , 
        'org.springframework.ui.velocity' , 
        ), 
        'com.springsource.slf4j.api' : (
        'org.slf4j' , 
        'org.slf4j.helpers' , 
        'org.slf4j.spi' , 
        ), 
        'org.springframework.osgi.extender' : (
        'org.springframework.osgi.extender' , 
        'org.springframework.osgi.extender.event' , 
        'org.springframework.osgi.extender.internal.activator' , 
        'org.springframework.osgi.extender.internal.dependencies.shutdown' , 
        'org.springframework.osgi.extender.internal.dependencies.startup' , 
        'org.springframework.osgi.extender.internal.support' , 
        'org.springframework.osgi.extender.internal.util.concurrent' , 
        'org.springframework.osgi.extender.support' , 
        'org.springframework.osgi.extender.support.internal' , 
        'org.springframework.osgi.extender.support.scanning' , 
        ), 
        'org.springframework.jms' : (
        'org.springframework.jms' , 
        'org.springframework.jms.config' , 
        'org.springframework.jms.connection' , 
        'org.springframework.jms.core' , 
        'org.springframework.jms.core.support' , 
        'org.springframework.jms.listener' , 
        'org.springframework.jms.listener.adapter' , 
        'org.springframework.jms.listener.endpoint' , 
        'org.springframework.jms.listener.serversession' , 
        'org.springframework.jms.remoting' , 
        'org.springframework.jms.support' , 
        'org.springframework.jms.support.converter' , 
        'org.springframework.jms.support.destination' , 
        ), 
        'com.springsource.javax.annotation' : (
        'javax.annotation' , 
        'javax.annotation.security' , 
        ), 
        'org.springframework.bundle.osgi.web.extender' : (
        ), 
        'org.springframework.osgi.core' : (
        'org.springframework.osgi' , 
        'org.springframework.osgi.bundle' , 
        'org.springframework.osgi.compendium.config' , 
        'org.springframework.osgi.compendium.internal' , 
        'org.springframework.osgi.config' , 
        'org.springframework.osgi.context' , 
        'org.springframework.osgi.context.event' , 
        'org.springframework.osgi.context.internal.classloader' , 
        'org.springframework.osgi.context.support' , 
        'org.springframework.osgi.context.support.internal' , 
        'org.springframework.osgi.service' , 
        'org.springframework.osgi.service.dependency.internal' , 
        'org.springframework.osgi.service.exporter' , 
        'org.springframework.osgi.service.exporter.support' , 
        'org.springframework.osgi.service.exporter.support.internal.controller' , 
        'org.springframework.osgi.service.importer' , 
        'org.springframework.osgi.service.importer.event' , 
        'org.springframework.osgi.service.importer.support' , 
        'org.springframework.osgi.service.importer.support.internal.aop' , 
        'org.springframework.osgi.service.importer.support.internal.collection' , 
        'org.springframework.osgi.service.importer.support.internal.collection.comparator' , 
        'org.springframework.osgi.service.importer.support.internal.controller' , 
        'org.springframework.osgi.service.importer.support.internal.dependency' , 
        'org.springframework.osgi.service.importer.support.internal.support' , 
        'org.springframework.osgi.service.importer.support.internal.util' , 
        'org.springframework.osgi.service.util.internal.aop' , 
        'org.springframework.osgi.util' , 
        'org.springframework.osgi.util.internal' , 
        ), 
        'org.apache.geronimo.specs.geronimo-javamail_1.4_spec' : (
        'javax.mail.search' , 
        'javax.mail.util' , 
        'javax.mail.event' , 
        'javax.mail.internet' , 
        'javax.mail' , 
        ), 
        'com.springsource.org.apache.jasper' : (
        'org.apache' , 
        'org.apache.jasper' , 
        'org.apache.jasper.compiler' , 
        'org.apache.jasper.compiler.tagplugin' , 
        'org.apache.jasper.el' , 
        'org.apache.jasper.resources' , 
        'org.apache.jasper.runtime' , 
        'org.apache.jasper.security' , 
        'org.apache.jasper.servlet' , 
        'org.apache.jasper.tagplugins.jstl' , 
        'org.apache.jasper.tagplugins.jstl.core' , 
        'org.apache.jasper.util' , 
        'org.apache.jasper.xmlparser' , 
        ), 
        'org.apache.activemq.activemq-pool' : (
        'org.apache.activemq.pool' , 
        ), 
        'org.springframework.bundle.spring.aspects' : (
        'org.springframework.transaction.aspectj' , 
        'org.springframework.beans.factory.aspectj' , 
        ), 
        'com.springsource.org.aopalliance' : (
        'org.aopalliance.aop' , 
        'org.aopalliance.intercept' , 
        ), 
        'org.syndeticlogic.gnu.io' : (
        'gnu.io' , 
        ), 
        'org.springframework.osgi.io' : (
        'org.springframework.osgi.io' , 
        'org.springframework.osgi.io.internal' , 
        'org.springframework.osgi.io.internal.resolver' , 
        ), 
        'com.springsource.org.apache.taglibs.standard' : (
        'org.apache.taglibs.standard' , 
        'org.apache.taglibs.standard.extra.spath' , 
        'org.apache.taglibs.standard.functions' , 
        'org.apache.taglibs.standard.lang.jstl' , 
        'org.apache.taglibs.standard.lang.jstl.parser' , 
        'org.apache.taglibs.standard.lang.jstl.test' , 
        'org.apache.taglibs.standard.lang.jstl.test.beans' , 
        'org.apache.taglibs.standard.lang.support' , 
        'org.apache.taglibs.standard.resources' , 
        'org.apache.taglibs.standard.tag.common.core' , 
        'org.apache.taglibs.standard.tag.common.fmt' , 
        'org.apache.taglibs.standard.tag.common.sql' , 
        'org.apache.taglibs.standard.tag.common.xml' , 
        'org.apache.taglibs.standard.tag.el.core' , 
        'org.apache.taglibs.standard.tag.el.fmt' , 
        'org.apache.taglibs.standard.tag.el.sql' , 
        'org.apache.taglibs.standard.tag.el.xml' , 
        'org.apache.taglibs.standard.tag.rt.core' , 
        'org.apache.taglibs.standard.tag.rt.fmt' , 
        'org.apache.taglibs.standard.tag.rt.sql' , 
        'org.apache.taglibs.standard.tag.rt.xml' , 
        'org.apache.taglibs.standard.tei' , 
        'org.apache.taglibs.standard.tlv' , 
        ), 
        'org.eclipse.equinox.weaving.hook' : (
        'org.eclipse.equinox.service.weaving' , 
        'org.eclipse.equinox.weaving.hooks' , 
        ), 
        'com.springsource.javax.ejb' : (
        'javax.ejb' , 
        'javax.ejb.spi' , 
        'javax.interceptor' , 
        ), 
        'org.apache.activemq.kahadb' : (
        'org.apache.kahadb.index' , 
        'org.apache.kahadb.util' , 
        'org.apache.kahadb.page' , 
        'org.apache.kahadb.journal' , 
        ), 
        'com.springsource.org.apache.coyote' : (
        'org.apache.coyote' , 
        'org.apache.coyote.ajp' , 
        'org.apache.coyote.http11' , 
        'org.apache.coyote.http11.filters' , 
        'org.apache.coyote.memory' , 
        'org.apache.jk' , 
        'org.apache.jk.apr' , 
        'org.apache.jk.common' , 
        'org.apache.jk.config' , 
        'org.apache.jk.core' , 
        'org.apache.jk.server' , 
        'org.apache.tomcat.jni' , 
        'org.apache.tomcat.util' , 
        'org.apache.tomcat.util.buf' , 
        'org.apache.tomcat.util.buf.res' , 
        'org.apache.tomcat.util.collections' , 
        'org.apache.tomcat.util.digester' , 
        'org.apache.tomcat.util.http' , 
        'org.apache.tomcat.util.http.fileupload' , 
        'org.apache.tomcat.util.http.mapper' , 
        'org.apache.tomcat.util.http.res' , 
        'org.apache.tomcat.util.log' , 
        'org.apache.tomcat.util.modeler' , 
        'org.apache.tomcat.util.modeler.modules' , 
        'org.apache.tomcat.util.net' , 
        'org.apache.tomcat.util.net.jsse' , 
        'org.apache.tomcat.util.net.jsse.res' , 
        'org.apache.tomcat.util.net.res' , 
        'org.apache.tomcat.util.res' , 
        'org.apache.tomcat.util.threads' , 
        'org.apache.tomcat.util.threads.res' , 
        ), 
        'org.eclipse.osgi' : (
        'org.eclipse.osgi.event' , 
        'org.eclipse.osgi.framework.console' , 
        'org.eclipse.osgi.framework.eventmgr' , 
        'org.eclipse.osgi.framework.log' , 
        'org.eclipse.osgi.launch' , 
        'org.eclipse.osgi.service.datalocation' , 
        'org.eclipse.osgi.service.debug' , 
        'org.eclipse.osgi.service.environment' , 
        'org.eclipse.osgi.service.localization' , 
        'org.eclipse.osgi.service.pluginconversion' , 
        'org.eclipse.osgi.service.resolver' , 
        'org.eclipse.osgi.service.runnable' , 
        'org.eclipse.osgi.service.security' , 
        'org.eclipse.osgi.service.urlconversion' , 
        'org.eclipse.osgi.signedcontent' , 
        'org.eclipse.osgi.storagemanager' , 
        'org.eclipse.osgi.util' , 
        'org.osgi.framework' , 
        'org.osgi.framework.launch' , 
        'org.osgi.framework.hooks.service' , 
        'org.osgi.service.condpermadmin' , 
        'org.osgi.service.framework' , 
        'org.osgi.service.packageadmin' , 
        'org.osgi.service.permissionadmin' , 
        'org.osgi.service.startlevel' , 
        'org.osgi.service.url' , 
        'org.osgi.util.tracker' , 
        'org.eclipse.core.runtime.adaptor' , 
        'org.eclipse.core.runtime.internal.adaptor' , 
        'org.eclipse.core.runtime.internal.stats' , 
        'org.eclipse.osgi.baseadaptor' , 
        'org.eclipse.osgi.baseadaptor.bundlefile' , 
        'org.eclipse.osgi.baseadaptor.hooks' , 
        'org.eclipse.osgi.baseadaptor.loader' , 
        'org.eclipse.osgi.framework.adaptor' , 
        'org.eclipse.osgi.framework.debug' , 
        'org.eclipse.osgi.framework.internal.core' , 
        'org.eclipse.osgi.framework.internal.protocol' , 
        'org.eclipse.osgi.framework.internal.protocol.bundleentry' , 
        'org.eclipse.osgi.framework.internal.protocol.bundleresource' , 
        'org.eclipse.osgi.framework.internal.protocol.reference' , 
        'org.eclipse.osgi.framework.internal.reliablefile' , 
        'org.eclipse.osgi.framework.util' , 
        'org.eclipse.osgi.internal.baseadaptor' , 
        'org.eclipse.osgi.internal.composite' , 
        'org.eclipse.osgi.internal.loader' , 
        'org.eclipse.osgi.internal.loader.buddy' , 
        'org.eclipse.osgi.internal.module' , 
        'org.eclipse.osgi.internal.profile' , 
        'org.eclipse.osgi.internal.resolver' , 
        'org.eclipse.osgi.internal.serviceregistry' , 
        'org.eclipse.osgi.internal.permadmin' , 
        'org.eclipse.osgi.internal.provisional.service.security' , 
        'org.eclipse.osgi.internal.provisional.verifier' , 
        'org.eclipse.osgi.internal.service.security' , 
        'org.eclipse.osgi.internal.signedcontent' , 
        'org.eclipse.osgi.service.internal.composite' , 
        ), 
        'com.springsource.javax.xml.ws' : (
        'javax.xml.ws' , 
        'javax.xml.ws.handler' , 
        'javax.xml.ws.handler.soap' , 
        'javax.xml.ws.http' , 
        'javax.xml.ws.soap' , 
        'javax.xml.ws.spi' , 
        'javax.xml.ws.wsaddressing' , 
        ), 
        'org.springframework.osgi.web' : (
        'org.springframework.osgi.io.internal' , 
        'org.springframework.osgi.io.internal.resolver' , 
        'org.springframework.osgi.test.internal.util.jar' , 
        'org.springframework.osgi.test.internal.util.jar.storage' , 
        'org.springframework.osgi.web.context.support' , 
        'org.springframework.osgi.web.deployer' , 
        'org.springframework.osgi.web.deployer.internal.support' , 
        'org.springframework.osgi.web.deployer.internal.util' , 
        'org.springframework.osgi.web.deployer.jetty' , 
        'org.springframework.osgi.web.deployer.support' , 
        'org.springframework.osgi.web.deployer.tomcat' , 
        ), 
        'org.syndeticlogic.minerva' : (
        'org.syndeticlogic.minerva.api' , 
        'org.syndeticlogic.minerva.configuration' , 
        'org.syndeticlogic.minerva.console' , 
        'org.syndeticlogic.minerva.daos' , 
        'org.syndeticlogic.minerva.exceptions' , 
        'org.syndeticlogic.minerva.notification' , 
        'org.syndeticlogic.minerva.rmi' , 
        'org.syndeticlogic.minerva.sensors' , 
        'org.syndeticlogic.minerva.sensors.sessions' , 
        'org.syndeticlogic.minerva.services' , 
        'org.syndeticlogic.minerva.util' , 
        ), 
        'com.springsource.org.apache.log4j' : (
        'org.apache.log4j' , 
        'org.apache.log4j.chainsaw' , 
        'org.apache.log4j.config' , 
        'org.apache.log4j.helpers' , 
        'org.apache.log4j.jdbc' , 
        'org.apache.log4j.jmx' , 
        'org.apache.log4j.lf5' , 
        'org.apache.log4j.lf5.config' , 
        'org.apache.log4j.lf5.util' , 
        'org.apache.log4j.lf5.viewer' , 
        'org.apache.log4j.lf5.viewer.categoryexplorer' , 
        'org.apache.log4j.lf5.viewer.configure' , 
        'org.apache.log4j.lf5.viewer.images' , 
        'org.apache.log4j.net' , 
        'org.apache.log4j.nt' , 
        'org.apache.log4j.or' , 
        'org.apache.log4j.or.jms' , 
        'org.apache.log4j.or.sax' , 
        'org.apache.log4j.spi' , 
        'org.apache.log4j.varia' , 
        'org.apache.log4j.xml' , 
        ), 
        'org.fosstrak.tdt.tdt' : (
        'org.fosstrak.tdt' , 
        'schemes' , 
        'auxiliary' , 
        'org.epcglobalinc.tdt' , 
        ), 
        'com.springsource.org.apache.el' : (
        'org.apache.el' , 
        'org.apache.el.lang' , 
        'org.apache.el.parser' , 
        'org.apache.el.util' , 
        ), 
        'org.springframework.osgi.catalina.start.osgi' : (
        ), 
        'com.springsource.javax.xml.soap' : (
        'javax.xml.soap' , 
        ), 
        'com.springsource.javax.servlet' : (
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.servlet.resources' , 
        ), 
        'org.rifidi.org.springframework.context' : (
        'org.springframework.context' , 
        'org.springframework.context.access' , 
        'org.springframework.context.annotation' , 
        'org.springframework.context.config' , 
        'org.springframework.context.event' , 
        'org.springframework.context.i18n' , 
        'org.springframework.context.support' , 
        'org.springframework.context.weaving' , 
        'org.springframework.ejb.access' , 
        'org.springframework.ejb.config' , 
        'org.springframework.ejb.interceptor' , 
        'org.springframework.ejb.support' , 
        'org.springframework.instrument.classloading' , 
        'org.springframework.instrument.classloading.glassfish' , 
        'org.springframework.instrument.classloading.oc4j' , 
        'org.springframework.instrument.classloading.weblogic' , 
        'org.springframework.jmx' , 
        'org.springframework.jmx.access' , 
        'org.springframework.jmx.export' , 
        'org.springframework.jmx.export.annotation' , 
        'org.springframework.jmx.export.assembler' , 
        'org.springframework.jmx.export.metadata' , 
        'org.springframework.jmx.export.naming' , 
        'org.springframework.jmx.export.notification' , 
        'org.springframework.jmx.support' , 
        'org.springframework.jndi' , 
        'org.springframework.jndi.support' , 
        'org.springframework.remoting' , 
        'org.springframework.remoting.rmi' , 
        'org.springframework.remoting.soap' , 
        'org.springframework.remoting.support' , 
        'org.springframework.scheduling' , 
        'org.springframework.scheduling.backportconcurrent' , 
        'org.springframework.scheduling.concurrent' , 
        'org.springframework.scheduling.support' , 
        'org.springframework.scheduling.timer' , 
        'org.springframework.scripting' , 
        'org.springframework.scripting.bsh' , 
        'org.springframework.scripting.config' , 
        'org.springframework.scripting.groovy' , 
        'org.springframework.scripting.jruby' , 
        'org.springframework.scripting.support' , 
        'org.springframework.stereotype' , 
        'org.springframework.ui' , 
        'org.springframework.ui.context' , 
        'org.springframework.ui.context.support' , 
        'org.springframework.validation' , 
        'org.springframework.validation.support' , 
        ), 
        'org.apache.xbean.spring' : (
        'org.apache.xbean.spring.jndi' , 
        'org.apache.xbean.spring' , 
        'org.apache.xbean.spring.context.impl' , 
        'org.apache.xbean.spring.util' , 
        'org.apache.xbean.spring.context' , 
        'org.apache.xbean.spring.context.v2c' , 
        'org.apache.xbean.spring.context.v2' , 
        'org.apache.xbean.spring.generator' , 
        ), 
        'com.springsource.org.apache.catalina' : (
        'org.apache' , 
        'org.apache.catalina' , 
        'org.apache.catalina.authenticator' , 
        'org.apache.catalina.connector' , 
        'org.apache.catalina.core' , 
        'org.apache.catalina.deploy' , 
        'org.apache.catalina.loader' , 
        'org.apache.catalina.manager' , 
        'org.apache.catalina.manager.host' , 
        'org.apache.catalina.manager.util' , 
        'org.apache.catalina.mbeans' , 
        'org.apache.catalina.realm' , 
        'org.apache.catalina.security' , 
        'org.apache.catalina.servlets' , 
        'org.apache.catalina.session' , 
        'org.apache.catalina.ssi' , 
        'org.apache.catalina.startup' , 
        'org.apache.catalina.users' , 
        'org.apache.catalina.util' , 
        'org.apache.catalina.valves' , 
        'org.apache.naming' , 
        'org.apache.naming.factory' , 
        'org.apache.naming.java' , 
        'org.apache.naming.resources' , 
        'org.apache.naming.resources.jndi' , 
        ), 
        'org.rifidi.org.relique.jdbc' : (
        'org.relique.jdbc.csv' , 
        ), 
        'org.syndeticlogic.minerva.tools' : (
        'org.syndeticlogic.minerva.diagnostics' , 
        'org.syndeticlogic.minerva.tools.tracking' , 
        ), 
        'com.springsource.javax.servlet.jsp.jstl' : (
        'javax.servlet.jsp.jstl.core' , 
        'javax.servlet.jsp.jstl.fmt' , 
        'javax.servlet.jsp.jstl.sql' , 
        'javax.servlet.jsp.jstl.tlv' , 
        ), 
        'com.springsource.net.sf.cglib' : (
        'net.sf.cglib.asm' , 
        'net.sf.cglib.asm.attrs' , 
        'net.sf.cglib.beans' , 
        'net.sf.cglib.core' , 
        'net.sf.cglib.proxy' , 
        'net.sf.cglib.reflect' , 
        'net.sf.cglib.transform' , 
        'net.sf.cglib.transform.hook' , 
        'net.sf.cglib.transform.impl' , 
        'net.sf.cglib.util' , 
        ), 
        'org.apache.geronimo.specs.geronimo-activation_1.1_spec' : (
        'javax.activation' , 
        ), 
        'org.eclipse.equinox.simpleconfigurator' : (
        'org.eclipse.equinox.internal.provisional.configurator' , 
        'org.eclipse.equinox.internal.simpleconfigurator' , 
        'org.eclipse.equinox.internal.simpleconfigurator.console' , 
        'org.eclipse.equinox.internal.simpleconfigurator.utils' , 
        ), 
        'org.springframework.beans' : (
        'org.springframework.beans' , 
        'org.springframework.beans.annotation' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.access' , 
        'org.springframework.beans.factory.access.el' , 
        'org.springframework.beans.factory.annotation' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.generic' , 
        'org.springframework.beans.factory.parsing' , 
        'org.springframework.beans.factory.serviceloader' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.wiring' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.beans.propertyeditors' , 
        'org.springframework.beans.support' , 
        ), 
        'org.springframework.jdbc' : (
        'org.springframework.jdbc' , 
        'org.springframework.jdbc.core' , 
        'org.springframework.jdbc.core.metadata' , 
        'org.springframework.jdbc.core.namedparam' , 
        'org.springframework.jdbc.core.simple' , 
        'org.springframework.jdbc.core.support' , 
        'org.springframework.jdbc.datasource' , 
        'org.springframework.jdbc.datasource.lookup' , 
        'org.springframework.jdbc.object' , 
        'org.springframework.jdbc.support' , 
        'org.springframework.jdbc.support.incrementer' , 
        'org.springframework.jdbc.support.lob' , 
        'org.springframework.jdbc.support.nativejdbc' , 
        'org.springframework.jdbc.support.rowset' , 
        'org.springframework.jdbc.support.xml' , 
        ), 
        'com.springsource.org.junit' : (
        'junit.extensions' , 
        'junit.framework' , 
        'junit.runner' , 
        'junit.textui' , 
        'org.hamcrest' , 
        'org.hamcrest.core' , 
        'org.hamcrest.internal' , 
        'org.junit' , 
        'org.junit.experimental' , 
        'org.junit.experimental.categories' , 
        'org.junit.experimental.max' , 
        'org.junit.experimental.results' , 
        'org.junit.experimental.runners' , 
        'org.junit.experimental.theories' , 
        'org.junit.experimental.theories.internal' , 
        'org.junit.experimental.theories.suppliers' , 
        'org.junit.internal' , 
        'org.junit.internal.builders' , 
        'org.junit.internal.matchers' , 
        'org.junit.internal.requests' , 
        'org.junit.internal.runners' , 
        'org.junit.internal.runners.model' , 
        'org.junit.internal.runners.statements' , 
        'org.junit.matchers' , 
        'org.junit.rules' , 
        'org.junit.runner' , 
        'org.junit.runner.manipulation' , 
        'org.junit.runner.notification' , 
        'org.junit.runners' , 
        'org.junit.runners.model' , 
        ), 
        'com.springsource.org.apache.jasper.org.eclipse.jdt' : (
        'org.eclipse.jdt.core.compiler' , 
        'org.eclipse.jdt.internal.compiler' , 
        'org.eclipse.jdt.internal.compiler.ast' , 
        'org.eclipse.jdt.internal.compiler.batch' , 
        'org.eclipse.jdt.internal.compiler.classfmt' , 
        'org.eclipse.jdt.internal.compiler.codegen' , 
        'org.eclipse.jdt.internal.compiler.env' , 
        'org.eclipse.jdt.internal.compiler.flow' , 
        'org.eclipse.jdt.internal.compiler.impl' , 
        'org.eclipse.jdt.internal.compiler.lookup' , 
        'org.eclipse.jdt.internal.compiler.parser' , 
        'org.eclipse.jdt.internal.compiler.parser.diagnose' , 
        'org.eclipse.jdt.internal.compiler.problem' , 
        'org.eclipse.jdt.internal.compiler.util' , 
        'org.eclipse.jdt.internal.core.util' , 
        ), 
        'com.springsource.org.apache.juli.extras' : (
        'org.apache.juli' , 
        'org.apache.juli.logging' , 
        'org.apache.juli.logging.impl' , 
        )}
        
        bundles_ipackages = { 
        'org.rifidi.org.apache.mina-core' : (
        'org.slf4j' , 
        ), 
        'org.apache.geronimo.specs.geronimo-j2ee-management_1.1_spec' : (
        'javax.ejb' , 
        'javax.management' , 
        'javax.management.j2ee' , 
        'javax.management.j2ee.statistics' , 
        ), 
        'org.springframework.orm' : (
        'com.ibatis.common.util' , 
        'com.ibatis.common.xml' , 
        'com.ibatis.sqlmap.client' , 
        'com.ibatis.sqlmap.client.event' , 
        'com.ibatis.sqlmap.engine.builder.xml' , 
        'com.ibatis.sqlmap.engine.impl' , 
        'com.ibatis.sqlmap.engine.transaction' , 
        'com.ibatis.sqlmap.engine.transaction.external' , 
        'com.ibatis.sqlmap.engine.type' , 
        'javax.jdo' , 
        'javax.jdo.datastore' , 
        'javax.naming' , 
        'javax.persistence' , 
        'javax.persistence.spi' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.sql' , 
        'javax.transaction' , 
        'javax.xml.parsers' , 
        'oracle.toplink.essentials.ejb.cmp3' , 
        'oracle.toplink.essentials.expressions' , 
        'oracle.toplink.essentials.internal.databaseaccess' , 
        'oracle.toplink.essentials.internal.sessions' , 
        'oracle.toplink.essentials.sessions' , 
        'oracle.toplink.exceptions' , 
        'oracle.toplink.expressions' , 
        'oracle.toplink.internal.databaseaccess' , 
        'oracle.toplink.jndi' , 
        'oracle.toplink.logging' , 
        'oracle.toplink.publicinterface' , 
        'oracle.toplink.queryframework' , 
        'oracle.toplink.sessionbroker' , 
        'oracle.toplink.sessions' , 
        'oracle.toplink.threetier' , 
        'oracle.toplink.tools.sessionconfiguration' , 
        'oracle.toplink.tools.sessionmanagement' , 
        'org.aopalliance.intercept' , 
        'org.apache.commons.logging' , 
        'org.apache.openjpa.persistence' , 
        'org.eclipse.persistence.expressions' , 
        'org.eclipse.persistence.internal.databaseaccess' , 
        'org.eclipse.persistence.internal.sessions' , 
        'org.eclipse.persistence.jpa' , 
        'org.eclipse.persistence.sessions' , 
        'org.hibernate' , 
        'org.hibernate.cache' , 
        'org.hibernate.cfg' , 
        'org.hibernate.classic' , 
        'org.hibernate.connection' , 
        'org.hibernate.context' , 
        'org.hibernate.criterion' , 
        'org.hibernate.dialect' , 
        'org.hibernate.ejb' , 
        'org.hibernate.engine' , 
        'org.hibernate.event' , 
        'org.hibernate.event.def' , 
        'org.hibernate.exception' , 
        'org.hibernate.impl' , 
        'org.hibernate.jdbc' , 
        'org.hibernate.persister.entity' , 
        'org.hibernate.tool.hbm2ddl' , 
        'org.hibernate.transaction' , 
        'org.hibernate.transform' , 
        'org.hibernate.type' , 
        'org.hibernate.usertype' , 
        'org.hibernate.util' , 
        'org.springframework.aop.scope' , 
        'org.springframework.aop.support' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.annotation' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.context' , 
        'org.springframework.context.weaving' , 
        'org.springframework.core' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.core.type' , 
        'org.springframework.core.type.classreading' , 
        'org.springframework.core.type.filter' , 
        'org.springframework.dao' , 
        'org.springframework.dao.support' , 
        'org.springframework.instrument.classloading' , 
        'org.springframework.jdbc' , 
        'org.springframework.jdbc.datasource' , 
        'org.springframework.jdbc.datasource.lookup' , 
        'org.springframework.jdbc.support' , 
        'org.springframework.jdbc.support.lob' , 
        'org.springframework.jndi' , 
        'org.springframework.transaction' , 
        'org.springframework.transaction.jta' , 
        'org.springframework.transaction.support' , 
        'org.springframework.ui' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.springframework.web.context' , 
        'org.springframework.web.context.request' , 
        'org.springframework.web.context.support' , 
        'org.springframework.web.filter' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'org.rifidi.org.springframework.aop' : (
        'com.jamonapi' , 
        'net.sf.cglib.core' , 
        'net.sf.cglib.proxy' , 
        'net.sf.cglib.transform.impl' , 
        'org.aopalliance.aop' , 
        'org.aopalliance.intercept' , 
        'org.apache.commons.logging' , 
        'org.apache.commons.pool' , 
        'org.apache.commons.pool.impl' , 
        'org.aspectj.bridge' , 
        'org.aspectj.lang' , 
        'org.aspectj.lang.annotation' , 
        'org.aspectj.lang.reflect' , 
        'org.aspectj.runtime.internal' , 
        'org.aspectj.util' , 
        'org.aspectj.weaver' , 
        'org.aspectj.weaver.ast' , 
        'org.aspectj.weaver.internal.tools' , 
        'org.aspectj.weaver.patterns' , 
        'org.aspectj.weaver.reflect' , 
        'org.aspectj.weaver.tools' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.parsing' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.core' , 
        'org.springframework.core.annotation' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.w3c.dom' , 
        ), 
        'org.springframework.web' : (
        'com.caucho.burlap.client' , 
        'com.caucho.burlap.io' , 
        'com.caucho.burlap.server' , 
        'com.caucho.hessian.client' , 
        'com.caucho.hessian.io' , 
        'com.caucho.hessian.server' , 
        'com.sun.net.httpserver' , 
        'javax.el' , 
        'javax.faces.application' , 
        'javax.faces.context' , 
        'javax.faces.el' , 
        'javax.faces.event' , 
        'javax.jws' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.servlet.jsp' , 
        'javax.servlet.jsp.el' , 
        'javax.servlet.jsp.tagext' , 
        'javax.xml.namespace' , 
        'javax.xml.rpc' , 
        'javax.xml.rpc.encoding' , 
        'javax.xml.rpc.server' , 
        'javax.xml.rpc.soap' , 
        'javax.xml.soap' , 
        'javax.xml.ws' , 
        'javax.xml.ws.handler' , 
        'javax.xml.ws.soap' , 
        'org.aopalliance.aop' , 
        'org.aopalliance.intercept' , 
        'org.apache.axis.encoding.ser' , 
        'org.apache.commons.httpclient' , 
        'org.apache.commons.httpclient.methods' , 
        'org.apache.commons.httpclient.params' , 
        'org.apache.commons.logging' , 
        'org.apache.log4j' , 
        'org.apache.taglibs.standard.lang.support' , 
        'org.springframework.aop.framework' , 
        'org.springframework.aop.support' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.access' , 
        'org.springframework.beans.factory.access.el' , 
        'org.springframework.beans.factory.annotation' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.context' , 
        'org.springframework.context.access' , 
        'org.springframework.context.i18n' , 
        'org.springframework.context.support' , 
        'org.springframework.core' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.core.task' , 
        'org.springframework.core.task.support' , 
        'org.springframework.remoting' , 
        'org.springframework.remoting.rmi' , 
        'org.springframework.remoting.soap' , 
        'org.springframework.remoting.support' , 
        'org.springframework.ui' , 
        'org.springframework.ui.context' , 
        'org.springframework.ui.context.support' , 
        'org.springframework.util' , 
        'org.xml.sax' , 
        ), 
        'org.springframework.web.servlet' : (
        'com.lowagie.text' , 
        'com.lowagie.text.pdf' , 
        'freemarker.cache' , 
        'freemarker.core' , 
        'freemarker.ext.jsp' , 
        'freemarker.ext.servlet' , 
        'freemarker.template' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.servlet.jsp' , 
        'javax.servlet.jsp.jstl.core' , 
        'javax.servlet.jsp.jstl.fmt' , 
        'javax.servlet.jsp.tagext' , 
        'javax.sql' , 
        'javax.xml.transform' , 
        'javax.xml.transform.dom' , 
        'javax.xml.transform.stream' , 
        'jxl' , 
        'jxl.write' , 
        'net.sf.jasperreports.engine' , 
        'net.sf.jasperreports.engine.design' , 
        'net.sf.jasperreports.engine.export' , 
        'net.sf.jasperreports.engine.util' , 
        'net.sf.jasperreports.engine.xml' , 
        'org.apache.commons.attributes' , 
        'org.apache.commons.fileupload' , 
        'org.apache.commons.fileupload.disk' , 
        'org.apache.commons.fileupload.servlet' , 
        'org.apache.commons.logging' , 
        'org.apache.poi.hssf.usermodel' , 
        'org.apache.poi.poifs.filesystem' , 
        'org.apache.tiles' , 
        'org.apache.tiles.access' , 
        'org.apache.tiles.context' , 
        'org.apache.tiles.definition' , 
        'org.apache.tiles.factory' , 
        'org.apache.tiles.jsp.context' , 
        'org.apache.tiles.locale.impl' , 
        'org.apache.tiles.preparer' , 
        'org.apache.tiles.servlet.context' , 
        'org.apache.tiles.web.util' , 
        'org.apache.velocity' , 
        'org.apache.velocity.app' , 
        'org.apache.velocity.app.tools' , 
        'org.apache.velocity.context' , 
        'org.apache.velocity.exception' , 
        'org.apache.velocity.runtime.resource.loader' , 
        'org.apache.velocity.tools.generic' , 
        'org.apache.velocity.tools.view' , 
        'org.apache.velocity.tools.view.context' , 
        'org.apache.velocity.tools.view.servlet' , 
        'org.apache.velocity.tools.view.tools' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.generic' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.beans.propertyeditors' , 
        'org.springframework.context' , 
        'org.springframework.context.event' , 
        'org.springframework.context.i18n' , 
        'org.springframework.context.support' , 
        'org.springframework.core' , 
        'org.springframework.core.annotation' , 
        'org.springframework.core.enums' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.core.style' , 
        'org.springframework.stereotype' , 
        'org.springframework.ui' , 
        'org.springframework.ui.context' , 
        'org.springframework.ui.context.support' , 
        'org.springframework.ui.freemarker' , 
        'org.springframework.ui.jasperreports' , 
        'org.springframework.ui.velocity' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.springframework.validation' , 
        'org.springframework.validation.support' , 
        'org.springframework.web' , 
        'org.springframework.web.context' , 
        'org.springframework.web.context.request' , 
        'org.springframework.web.context.support' , 
        'org.springframework.web.filter' , 
        'org.springframework.web.util' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'com.springsource.javax.persistence' : (
        'javax.sql' , 
        ), 
        'org.apache.felix.bundlerepository' : (
        'org.osgi.framework' , 
        'org.osgi.service.log' , 
        'org.osgi.service.obr' , 
        'org.osgi.service.url' , 
        ), 
        'com.springsource.javax.xml.bind' : (
        'javax.activation' , 
        'javax.xml.namespace' , 
        'javax.xml.parsers' , 
        'javax.xml.stream' , 
        'javax.xml.transform' , 
        'javax.xml.transform.dom' , 
        'javax.xml.transform.sax' , 
        'javax.xml.transform.stream' , 
        'javax.xml.validation' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        'org.xml.sax.ext' , 
        'org.xml.sax.helpers' , 
        ), 
        'com.springsource.javax.servlet.jsp' : (
        'javax.el' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        ), 
        'javax.servlet' : (
        ), 
        'com.mysql.jdbc' : (
        'javax.net' , 
        'javax.net.ssl' , 
        'javax.xml.parsers' , 
        'javax.xml.stream' , 
        'javax.xml.transform' , 
        'javax.xml.transform.dom' , 
        'javax.xml.transform.sax' , 
        'javax.xml.transform.stax' , 
        'javax.xml.transform.stream' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        'org.xml.sax.helpers' , 
        'javax.naming' , 
        'javax.naming.spi' , 
        'javax.sql' , 
        'javax.transaction.xa' , 
        'org.apache.commons.logging' , 
        'org.apache.log4j' , 
        'com.mchange.v2.c3p0' , 
        'org.jboss.resource.adapter.jdbc' , 
        'org.jboss.resource.adapter.jdbc.vendor' , 
        ), 
        'org.rifidi.org.llrp.ltk' : (
        'jargs.gnu' , 
        'org.apache.log4j' , 
        'org.apache.mina.common' , 
        'org.apache.mina.common.support' , 
        'org.apache.mina.filter' , 
        'org.apache.mina.filter.codec' , 
        'org.apache.mina.filter.codec.demux' , 
        'org.apache.mina.filter.codec.serialization' , 
        'org.apache.mina.filter.codec.support' , 
        'org.apache.mina.filter.codec.textline' , 
        'org.apache.mina.filter.executor' , 
        'org.apache.mina.handler' , 
        'org.apache.mina.handler.chain' , 
        'org.apache.mina.handler.demux' , 
        'org.apache.mina.handler.multiton' , 
        'org.apache.mina.handler.support' , 
        'org.apache.mina.management' , 
        'org.apache.mina.transport.socket.nio' , 
        'org.apache.mina.transport.socket.nio.support' , 
        'org.apache.mina.transport.vmpipe' , 
        'org.apache.mina.transport.vmpipe.support' , 
        'org.apache.mina.util' , 
        'org.jdom' , 
        'org.jdom.adapters' , 
        'org.jdom.filter' , 
        'org.jdom.input' , 
        'org.jdom.output' , 
        'org.jdom.transform' , 
        'org.jdom.xpath' , 
        ), 
        'org.apache.geronimo.specs.geronimo-jms_1.1_spec' : (
        'javax.jms' , 
        'javax.transaction.xa' , 
        ), 
        'org.springframework.transaction' : (
        'com.evermind.server' , 
        'com.ibm.ws.Transaction' , 
        'com.ibm.wsspi.uow' , 
        'javax.ejb' , 
        'javax.management' , 
        'javax.naming' , 
        'javax.resource' , 
        'javax.resource.cci' , 
        'javax.resource.spi' , 
        'javax.resource.spi.endpoint' , 
        'javax.resource.spi.work' , 
        'javax.transaction' , 
        'javax.transaction.xa' , 
        'oracle.j2ee.transaction' , 
        'org.aopalliance.aop' , 
        'org.aopalliance.intercept' , 
        'org.apache.commons.logging' , 
        'org.objectweb.jotm' , 
        'org.springframework.aop' , 
        'org.springframework.aop.config' , 
        'org.springframework.aop.framework' , 
        'org.springframework.aop.support' , 
        'org.springframework.aop.support.annotation' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.parsing' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.beans.propertyeditors' , 
        'org.springframework.context' , 
        'org.springframework.context.support' , 
        'org.springframework.core' , 
        'org.springframework.core.task' , 
        'org.springframework.jndi' , 
        'org.springframework.metadata' , 
        'org.springframework.scheduling' , 
        'org.springframework.stereotype' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.w3c.dom' , 
        'weblogic.transaction' , 
        ), 
        'org.apache.derby' : (
        ), 
        'org.eclipse.equinox.launcher' : (
        ), 
        'com.springsource.javax.xml.rpc' : (
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.xml.soap' , 
        ), 
        'com.springsource.javax.el' : (
        ), 
        'com.springsource.slf4j.jcl' : (
        'org.apache.commons.logging' , 
        'org.slf4j' , 
        'org.slf4j.helpers' , 
        'org.slf4j.spi' , 
        ), 
        'org.jdom' : (
        ), 
        'org.apache.activemq.activemq-core' : (
        'META-INF.services.org.apache.xbean.spring.http.activemq.apache.org.schema' , 
        'com.thoughtworks.xstream' , 
        'com.thoughtworks.xstream.converters' , 
        'com.thoughtworks.xstream.io' , 
        'com.thoughtworks.xstream.io.json' , 
        'com.thoughtworks.xstream.io.xml' , 
        'javax.jms' , 
        'javax.management' , 
        'javax.management.j2ee.statistics' , 
        'javax.management.openmbean' , 
        'javax.management.remote' , 
        'javax.naming' , 
        'javax.naming.directory' , 
        'javax.naming.event' , 
        'javax.naming.spi' , 
        'javax.net' , 
        'javax.net.ssl' , 
        'javax.security.auth' , 
        'javax.security.auth.callback' , 
        'javax.security.auth.login' , 
        'javax.security.auth.spi' , 
        'javax.sql' , 
        'javax.transaction.xa' , 
        'javax.xml.parsers' , 
        'org.apache.activeio.journal' , 
        'org.apache.activeio.journal.active' , 
        'org.apache.activeio.packet' , 
        'org.apache.activemq' , 
        'org.apache.activemq.advisory' , 
        'org.apache.activemq.blob' , 
        'org.apache.activemq.broker' , 
        'org.apache.activemq.broker.cluster' , 
        'org.apache.activemq.broker.ft' , 
        'org.apache.activemq.broker.jmx' , 
        'org.apache.activemq.broker.region' , 
        'org.apache.activemq.broker.region.cursors' , 
        'org.apache.activemq.broker.region.group' , 
        'org.apache.activemq.broker.region.policy' , 
        'org.apache.activemq.broker.region.virtual' , 
        'org.apache.activemq.broker.util' , 
        'org.apache.activemq.broker.view' , 
        'org.apache.activemq.command' , 
        'org.apache.activemq.filter' , 
        'org.apache.activemq.jaas' , 
        'org.apache.activemq.jmdns' , 
        'org.apache.activemq.jndi' , 
        'org.apache.activemq.kaha' , 
        'org.apache.activemq.kaha.impl' , 
        'org.apache.activemq.kaha.impl.async' , 
        'org.apache.activemq.kaha.impl.container' , 
        'org.apache.activemq.kaha.impl.data' , 
        'org.apache.activemq.kaha.impl.index' , 
        'org.apache.activemq.kaha.impl.index.hash' , 
        'org.apache.activemq.kaha.impl.index.tree' , 
        'org.apache.activemq.management' , 
        'org.apache.activemq.memory' , 
        'org.apache.activemq.memory.buffer' , 
        'org.apache.activemq.memory.list' , 
        'org.apache.activemq.network' , 
        'org.apache.activemq.network.jms' , 
        'org.apache.activemq.openwire' , 
        'org.apache.activemq.openwire.tool' , 
        'org.apache.activemq.openwire.v1' , 
        'org.apache.activemq.openwire.v2' , 
        'org.apache.activemq.openwire.v3' , 
        'org.apache.activemq.openwire.v4' , 
        'org.apache.activemq.openwire.v5' , 
        'org.apache.activemq.plugin' , 
        'org.apache.activemq.protobuf' , 
        'org.apache.activemq.protobuf.compiler' , 
        'org.apache.activemq.protobuf.compiler.parser' , 
        'org.apache.activemq.proxy' , 
        'org.apache.activemq.security' , 
        'org.apache.activemq.selector' , 
        'org.apache.activemq.spring' , 
        'org.apache.activemq.state' , 
        'org.apache.activemq.store' , 
        'org.apache.activemq.store.amq' , 
        'org.apache.activemq.store.jdbc' , 
        'org.apache.activemq.store.jdbc.adapter' , 
        'org.apache.activemq.store.journal' , 
        'org.apache.activemq.store.kahadaptor' , 
        'org.apache.activemq.store.kahadb' , 
        'org.apache.activemq.store.kahadb.data' , 
        'org.apache.activemq.store.memory' , 
        'org.apache.activemq.thread' , 
        'org.apache.activemq.transaction' , 
        'org.apache.activemq.transport' , 
        'org.apache.activemq.transport.discovery' , 
        'org.apache.activemq.transport.discovery.multicast' , 
        'org.apache.activemq.transport.discovery.rendezvous' , 
        'org.apache.activemq.transport.discovery.simple' , 
        'org.apache.activemq.transport.failover' , 
        'org.apache.activemq.transport.fanout' , 
        'org.apache.activemq.transport.logwriters' , 
        'org.apache.activemq.transport.mock' , 
        'org.apache.activemq.transport.multicast' , 
        'org.apache.activemq.transport.nio' , 
        'org.apache.activemq.transport.peer' , 
        'org.apache.activemq.transport.reliable' , 
        'org.apache.activemq.transport.stomp' , 
        'org.apache.activemq.transport.tcp' , 
        'org.apache.activemq.transport.udp' , 
        'org.apache.activemq.transport.vm' , 
        'org.apache.activemq.usage' , 
        'org.apache.activemq.util' , 
        'org.apache.activemq.wireformat' , 
        'org.apache.activemq.xbean' , 
        'org.apache.commons.logging' , 
        'org.apache.commons.net.ftp' , 
        'org.apache.derby.jdbc' , 
        'org.apache.kahadb.index' , 
        'org.apache.kahadb.journal' , 
        'org.apache.kahadb.page' , 
        'org.apache.kahadb.util' , 
        'org.apache.maven.plugin' , 
        'org.apache.maven.plugin.logging' , 
        'org.apache.maven.project' , 
        'org.apache.tools.ant' , 
        'org.apache.tools.ant.taskdefs' , 
        'org.apache.xbean.spring.context' , 
        'org.apache.xbean.spring.context.impl' , 
        'org.apache.xbean.spring.context.v2' , 
        'org.apache.xpath' , 
        'org.apache.xpath.objects' , 
        'org.codehaus.jam' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.beans.propertyeditors' , 
        'org.springframework.context' , 
        'org.springframework.core.io' , 
        'org.springframework.jndi' , 
        'org.springframework.util' , 
        'org.w3c.dom' , 
        'org.w3c.dom.traversal' , 
        'org.xml.sax' , 
        ), 
        'com.springsource.slf4j.log4j' : (
        'org.apache.log4j' , 
        'org.slf4j' , 
        'org.slf4j.helpers' , 
        'org.slf4j.spi' , 
        ), 
        'com.springsource.javax.xml.stream' : (
        'javax.xml.transform' , 
        ), 
        'org.springframework.core' : (
        'edu.emory.mathcs.backport.java.util.concurrent' , 
        'javax.xml.transform' , 
        'org.apache.commons.attributes' , 
        'org.apache.commons.collections' , 
        'org.apache.commons.collections.map' , 
        'org.apache.commons.logging' , 
        'org.apache.log4j' , 
        'org.apache.log4j.xml' , 
        'org.aspectj.bridge' , 
        'org.aspectj.weaver' , 
        'org.aspectj.weaver.bcel' , 
        'org.aspectj.weaver.patterns' , 
        'org.eclipse.core.runtime' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'org.aspectj.weaver' : (
        ), 
        'org.aspectj.runtime' : (
        ), 
        'org.eclipse.osgi.services' : (
        'org.osgi.framework' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        ), 
        'org.springframework.security.core' : (
        'javax.crypto' , 
        'javax.crypto.spec' , 
        'javax.naming' , 
        'javax.naming.directory' , 
        'javax.naming.ldap' , 
        'javax.rmi' , 
        'javax.security.auth' , 
        'javax.security.auth.callback' , 
        'javax.security.auth.login' , 
        'javax.security.auth.spi' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.sql' , 
        'javax.xml.parsers' , 
        'net.sf.ehcache' , 
        'org.aopalliance.aop' , 
        'org.aopalliance.intercept' , 
        'org.apache.commons.codec.binary' , 
        'org.apache.commons.codec.digest' , 
        'org.apache.commons.collections.iterators' , 
        'org.apache.commons.logging' , 
        'org.apache.directory.server.configuration' , 
        'org.apache.directory.server.core' , 
        'org.apache.directory.server.core.configuration' , 
        'org.apache.directory.server.jndi' , 
        'org.apache.directory.server.protocol.shared.store' , 
        'org.aspectj.lang' , 
        'org.aspectj.lang.reflect' , 
        'org.aspectj.weaver.tools' , 
        'org.jaxen' , 
        'org.jaxen.dom' , 
        'org.springframework.aop' , 
        'org.springframework.aop.config' , 
        'org.springframework.aop.framework' , 
        'org.springframework.aop.support' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.parsing' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.beans.propertyeditors' , 
        'org.springframework.context' , 
        'org.springframework.context.i18n' , 
        'org.springframework.context.support' , 
        'org.springframework.core' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.dao' , 
        'org.springframework.dao.support' , 
        'org.springframework.jdbc.core' , 
        'org.springframework.jdbc.core.support' , 
        'org.springframework.jdbc.object' , 
        'org.springframework.ldap' , 
        'org.springframework.ldap.core' , 
        'org.springframework.ldap.core.support' , 
        'org.springframework.metadata' , 
        'org.springframework.mock.web' , 
        'org.springframework.remoting.httpinvoker' , 
        'org.springframework.remoting.support' , 
        'org.springframework.security' , 
        'org.springframework.security.acl' , 
        'org.springframework.security.acl.basic' , 
        'org.springframework.security.acl.basic.cache' , 
        'org.springframework.security.acl.basic.jdbc' , 
        'org.springframework.security.adapters' , 
        'org.springframework.security.afterinvocation' , 
        'org.springframework.security.authoritymapping' , 
        'org.springframework.security.concurrent' , 
        'org.springframework.security.config' , 
        'org.springframework.security.context' , 
        'org.springframework.security.context.httpinvoker' , 
        'org.springframework.security.context.rmi' , 
        'org.springframework.security.event.authentication' , 
        'org.springframework.security.event.authorization' , 
        'org.springframework.security.intercept' , 
        'org.springframework.security.intercept.method' , 
        'org.springframework.security.intercept.method.aopalliance' , 
        'org.springframework.security.intercept.method.aspectj' , 
        'org.springframework.security.intercept.web' , 
        'org.springframework.security.ldap' , 
        'org.springframework.security.ldap.populator' , 
        'org.springframework.security.ldap.search' , 
        'org.springframework.security.providers' , 
        'org.springframework.security.providers.anonymous' , 
        'org.springframework.security.providers.dao' , 
        'org.springframework.security.providers.dao.cache' , 
        'org.springframework.security.providers.dao.salt' , 
        'org.springframework.security.providers.encoding' , 
        'org.springframework.security.providers.jaas' , 
        'org.springframework.security.providers.jaas.event' , 
        'org.springframework.security.providers.ldap' , 
        'org.springframework.security.providers.ldap.authenticator' , 
        'org.springframework.security.providers.preauth' , 
        'org.springframework.security.providers.rcp' , 
        'org.springframework.security.providers.rememberme' , 
        'org.springframework.security.providers.x509' , 
        'org.springframework.security.providers.x509.cache' , 
        'org.springframework.security.providers.x509.populator' , 
        'org.springframework.security.runas' , 
        'org.springframework.security.securechannel' , 
        'org.springframework.security.token' , 
        'org.springframework.security.ui' , 
        'org.springframework.security.ui.basicauth' , 
        'org.springframework.security.ui.digestauth' , 
        'org.springframework.security.ui.logout' , 
        'org.springframework.security.ui.preauth' , 
        'org.springframework.security.ui.preauth.header' , 
        'org.springframework.security.ui.preauth.j2ee' , 
        'org.springframework.security.ui.preauth.websphere' , 
        'org.springframework.security.ui.preauth.x509' , 
        'org.springframework.security.ui.rememberme' , 
        'org.springframework.security.ui.savedrequest' , 
        'org.springframework.security.ui.session' , 
        'org.springframework.security.ui.switchuser' , 
        'org.springframework.security.ui.webapp' , 
        'org.springframework.security.ui.x509' , 
        'org.springframework.security.userdetails' , 
        'org.springframework.security.userdetails.checker' , 
        'org.springframework.security.userdetails.hierarchicalroles' , 
        'org.springframework.security.userdetails.jdbc' , 
        'org.springframework.security.userdetails.ldap' , 
        'org.springframework.security.userdetails.memory' , 
        'org.springframework.security.util' , 
        'org.springframework.security.vote' , 
        'org.springframework.security.wrapper' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.springframework.web.context' , 
        'org.springframework.web.context.support' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'com.springsource.org.apache.commons.logging' : (
        'javax.servlet' , 
        'org.apache.avalon.framework.logger' , 
        'org.apache.log' , 
        'org.apache.log4j' , 
        ), 
        'org.springframework.context.support' : (
        'commonj.timers' , 
        'commonj.work' , 
        'freemarker.cache' , 
        'freemarker.template' , 
        'javax.activation' , 
        'javax.mail' , 
        'javax.mail.internet' , 
        'javax.naming' , 
        'javax.sql' , 
        'net.sf.ehcache' , 
        'net.sf.ehcache.bootstrap' , 
        'net.sf.ehcache.constructs.blocking' , 
        'net.sf.ehcache.event' , 
        'net.sf.ehcache.store' , 
        'net.sf.jasperreports.engine' , 
        'net.sf.jasperreports.engine.data' , 
        'net.sf.jasperreports.engine.export' , 
        'org.apache.commons.collections' , 
        'org.apache.commons.logging' , 
        'org.apache.velocity' , 
        'org.apache.velocity.app' , 
        'org.apache.velocity.context' , 
        'org.apache.velocity.exception' , 
        'org.apache.velocity.runtime' , 
        'org.apache.velocity.runtime.log' , 
        'org.apache.velocity.runtime.resource' , 
        'org.apache.velocity.runtime.resource.loader' , 
        'org.quartz' , 
        'org.quartz.impl' , 
        'org.quartz.impl.jdbcjobstore' , 
        'org.quartz.simpl' , 
        'org.quartz.spi' , 
        'org.quartz.utils' , 
        'org.quartz.xml' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.support' , 
        'org.springframework.context' , 
        'org.springframework.core' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.core.task' , 
        'org.springframework.jdbc.datasource' , 
        'org.springframework.jndi' , 
        'org.springframework.scheduling' , 
        'org.springframework.transaction' , 
        'org.springframework.transaction.support' , 
        'org.springframework.util' , 
        ), 
        'com.springsource.slf4j.api' : (
        'org.slf4j.impl' , 
        ), 
        'org.springframework.osgi.extender' : (
        'org.apache.commons.logging' , 
        'org.osgi.framework' , 
        'org.osgi.service.packageadmin' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.context' , 
        'org.springframework.context.event' , 
        'org.springframework.core' , 
        'org.springframework.core.enums' , 
        'org.springframework.core.task' , 
        'org.springframework.osgi' , 
        'org.springframework.osgi.context' , 
        'org.springframework.osgi.context.event' , 
        'org.springframework.osgi.context.support' , 
        'org.springframework.osgi.io.internal.resolver' , 
        'org.springframework.osgi.service.importer' , 
        'org.springframework.osgi.service.importer.event' , 
        'org.springframework.osgi.service.importer.support' , 
        'org.springframework.osgi.util' , 
        'org.springframework.scheduling.timer' , 
        'org.springframework.util' , 
        'org.xml.sax' , 
        ), 
        'org.springframework.jms' : (
        'javax.jms' , 
        'javax.naming' , 
        'javax.resource' , 
        'javax.resource.spi' , 
        'javax.resource.spi.endpoint' , 
        'org.aopalliance.intercept' , 
        'org.apache.commons.logging' , 
        'org.apache.commons.pool' , 
        'org.apache.commons.pool.impl' , 
        'org.springframework.aop.framework' , 
        'org.springframework.aop.support' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.parsing' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.context' , 
        'org.springframework.core' , 
        'org.springframework.core.task' , 
        'org.springframework.jca.endpoint' , 
        'org.springframework.jndi' , 
        'org.springframework.remoting' , 
        'org.springframework.remoting.support' , 
        'org.springframework.scheduling' , 
        'org.springframework.scheduling.timer' , 
        'org.springframework.transaction' , 
        'org.springframework.transaction.support' , 
        'org.springframework.util' , 
        'org.w3c.dom' , 
        ), 
        'com.springsource.javax.annotation' : (
        ), 
        'org.springframework.bundle.osgi.web.extender' : (
        'org.apache.commons.logging' , 
        'org.osgi.framework' , 
        'org.springframework.beans.factory' , 
        'org.springframework.core' , 
        'org.springframework.core.task' , 
        'org.springframework.osgi' , 
        'org.springframework.osgi.context' , 
        'org.springframework.osgi.context.support' , 
        'org.springframework.osgi.util' , 
        'org.springframework.osgi.web.deployer' , 
        'org.springframework.osgi.web.deployer.jetty' , 
        'org.springframework.osgi.web.deployer.support' , 
        'org.springframework.osgi.web.deployer.tomcat' , 
        'org.springframework.scheduling.timer' , 
        'org.springframework.util' , 
        ), 
        'org.springframework.osgi.core' : (
        'org.aopalliance.aop' , 
        'org.aopalliance.intercept' , 
        'org.apache.commons.logging' , 
        'org.osgi.framework' , 
        'org.osgi.service.cm' , 
        'org.osgi.service.startlevel' , 
        'org.springframework.aop.framework' , 
        'org.springframework.aop.support' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.beans.propertyeditors' , 
        'org.springframework.context' , 
        'org.springframework.context.event' , 
        'org.springframework.context.support' , 
        'org.springframework.core' , 
        'org.springframework.core.enums' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.osgi.io' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'org.apache.geronimo.specs.geronimo-javamail_1.4_spec' : (
        'javax.activation' , 
        'javax.mail' , 
        'javax.mail.event' , 
        'javax.mail.internet' , 
        'javax.mail.search' , 
        'javax.mail.util' , 
        ), 
        'com.springsource.org.apache.jasper' : (
        'javax.el' , 
        'javax.naming' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.servlet.jsp' , 
        'javax.servlet.jsp.el' , 
        'javax.servlet.jsp.resources' , 
        'javax.servlet.jsp.tagext' , 
        'javax.servlet.resources' , 
        'javax.xml.parsers' , 
        'org.apache.el' , 
        'org.apache.el.lang' , 
        'org.apache.juli.logging' , 
        'org.apache.tools.ant' , 
        'org.apache.tools.ant.taskdefs' , 
        'org.apache.tools.ant.types' , 
        'org.apache.tools.ant.util' , 
        'org.eclipse.jdt.core.compiler' , 
        'org.eclipse.jdt.internal.compiler' , 
        'org.eclipse.jdt.internal.compiler.classfmt' , 
        'org.eclipse.jdt.internal.compiler.env' , 
        'org.eclipse.jdt.internal.compiler.problem' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        'org.xml.sax.ext' , 
        'org.xml.sax.helpers' , 
        ), 
        'org.apache.activemq.activemq-pool' : (
        'javax.jms' , 
        'javax.naming' , 
        'javax.transaction' , 
        'javax.transaction.xa' , 
        'org.apache.activemq' , 
        'org.apache.activemq.advisory' , 
        'org.apache.activemq.jndi' , 
        'org.apache.activemq.pool' , 
        'org.apache.activemq.ra' , 
        'org.apache.activemq.transport' , 
        'org.apache.activemq.util' , 
        'org.apache.commons.logging' , 
        'org.apache.commons.pool' , 
        'org.apache.commons.pool.impl' , 
        'org.apache.geronimo.transaction.manager' , 
        'org.springframework.beans.factory' , 
        ), 
        'org.springframework.bundle.spring.aspects' : (
        'org.apache.commons.logging' , 
        'org.aspectj.internal.lang.annotation' , 
        'org.aspectj.lang' , 
        'org.aspectj.lang.annotation' , 
        'org.aspectj.lang.reflect' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.annotation' , 
        'org.springframework.beans.factory.aspectj' , 
        'org.springframework.beans.factory.wiring' , 
        'org.springframework.transaction.annotation' , 
        'org.springframework.transaction.aspectj' , 
        'org.springframework.transaction.interceptor' , 
        ), 
        'com.springsource.org.aopalliance' : (
        ), 
        'org.syndeticlogic.gnu.io' : (
        ), 
        'org.springframework.osgi.io' : (
        'org.apache.commons.logging' , 
        'org.osgi.framework' , 
        'org.osgi.service.packageadmin' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.util' , 
        ), 
        'com.springsource.org.apache.taglibs.standard' : (
        'javax.naming' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.servlet.jsp' , 
        'javax.servlet.jsp.el' , 
        'javax.servlet.jsp.jstl.core' , 
        'javax.servlet.jsp.jstl.fmt' , 
        'javax.servlet.jsp.jstl.sql' , 
        'javax.servlet.jsp.tagext' , 
        'javax.sql' , 
        'javax.xml.parsers' , 
        'javax.xml.transform' , 
        'javax.xml.transform.dom' , 
        'javax.xml.transform.sax' , 
        'javax.xml.transform.stream' , 
        'org.apache.xalan.serialize' , 
        'org.apache.xalan.templates' , 
        'org.apache.xml.utils' , 
        'org.apache.xpath' , 
        'org.apache.xpath.objects' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        'org.xml.sax.helpers' , 
        ), 
        'org.eclipse.equinox.weaving.hook' : (
        ), 
        'com.springsource.javax.ejb' : (
        'javax.transaction' , 
        'javax.xml.rpc.handler' , 
        ), 
        'org.apache.activemq.kahadb' : (
        'org.apache.commons.logging' , 
        'org.apache.kahadb.index' , 
        'org.apache.kahadb.journal' , 
        'org.apache.kahadb.page' , 
        'org.apache.kahadb.util' , 
        ), 
        'com.springsource.org.apache.coyote' : (
        'javax.management' , 
        'javax.management.loading' , 
        'javax.management.modelmbean' , 
        'javax.naming' , 
        'javax.naming.directory' , 
        'javax.net.ssl' , 
        'javax.security.cert' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.xml.parsers' , 
        'javax.xml.transform' , 
        'javax.xml.transform.dom' , 
        'javax.xml.transform.stream' , 
        'org.apache.catalina' , 
        'org.apache.catalina.deploy' , 
        'org.apache.juli.logging' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        'org.xml.sax.helpers' , 
        ), 
        'org.eclipse.osgi' : (
        ), 
        'com.springsource.javax.xml.ws' : (
        'javax.xml.bind' , 
        'javax.xml.bind.annotation' , 
        'javax.xml.namespace' , 
        'javax.xml.soap' , 
        'javax.xml.transform' , 
        'javax.xml.transform.stream' , 
        'org.w3c.dom' , 
        ), 
        'org.springframework.osgi.web' : (
        'javax.servlet' , 
        'org.apache.catalina' , 
        'org.apache.catalina.core' , 
        'org.apache.catalina.startup' , 
        'org.apache.commons.logging' , 
        'org.mortbay.jetty' , 
        'org.mortbay.jetty.handler' , 
        'org.mortbay.jetty.webapp' , 
        'org.mortbay.resource' , 
        'org.mortbay.util' , 
        'org.osgi.framework' , 
        'org.osgi.service.packageadmin' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.context' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.osgi' , 
        'org.springframework.osgi.context' , 
        'org.springframework.osgi.context.support' , 
        'org.springframework.osgi.io' , 
        'org.springframework.osgi.service.importer.support' , 
        'org.springframework.osgi.util' , 
        'org.springframework.ui.context' , 
        'org.springframework.ui.context.support' , 
        'org.springframework.util' , 
        'org.springframework.web.context' , 
        'org.springframework.web.context.support' , 
        ), 
        'org.syndeticlogic.minerva' : (
        'com.espertech.esper.client' , 
        'com.espertech.esper.client.metric' , 
        'com.espertech.esper.client.soda' , 
        'com.espertech.esper.client.time' , 
        'com.espertech.esper.event' , 
        'javax.jms' , 
        'javax.xml.namespace' , 
        'javax.xml.parsers' , 
        'javax.xml.xpath' , 
        'net.sf.cglib.asm' , 
        'net.sf.cglib.asm.attrs' , 
        'net.sf.cglib.beans' , 
        'net.sf.cglib.core' , 
        'net.sf.cglib.proxy' , 
        'net.sf.cglib.reflect' , 
        'net.sf.cglib.transform' , 
        'net.sf.cglib.transform.hook' , 
        'net.sf.cglib.transform.impl' , 
        'net.sf.cglib.util' , 
        'org.aopalliance.aop' , 
        'org.aopalliance.intercept' , 
        'org.apache.activemq' , 
        'org.apache.activemq.broker' , 
        'org.apache.activemq.command' , 
        'org.apache.activemq.jndi' , 
        'org.apache.activemq.management' , 
        'org.apache.activemq.pool' , 
        'org.apache.activemq.spring' , 
        'org.apache.activemq.xbean' , 
        'org.apache.commons.codec.binary' , 
        'org.apache.commons.dbcp' , 
        'org.apache.commons.logging' , 
        'org.apache.log4j' , 
        'org.eclipse.osgi.framework.console' , 
        'org.epcglobalinc.tdt' , 
        'org.fosstrak.tdt' , 
        'org.osgi.framework' , 
        'org.osgi.service.cm' , 
        'org.osgi.service.obr' , 
        'org.springframework.aop' , 
        'org.springframework.aop.framework' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.context' , 
        'org.springframework.core' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.dao' , 
        'org.springframework.jdbc.core' , 
        'org.springframework.jdbc.core.simple' , 
        'org.springframework.jdbc.support' , 
        'org.springframework.jms' , 
        'org.springframework.jms.core' , 
        'org.springframework.jms.support' , 
        'org.springframework.jms.support.destination' , 
        'org.springframework.osgi.extender.internal.dependencies.startup' , 
        'org.springframework.remoting.rmi' , 
        'org.springframework.remoting.support' , 
        'org.springframework.security' , 
        'org.springframework.security.config' , 
        'org.springframework.security.intercept' , 
        'org.springframework.security.intercept.method' , 
        'org.springframework.security.intercept.method.aopalliance' , 
        'org.springframework.security.providers' , 
        'org.springframework.security.providers.dao' , 
        'org.springframework.security.userdetails' , 
        'org.springframework.security.userdetails.checker' , 
        'org.springframework.security.userdetails.jdbc' , 
        'org.springframework.security.userdetails.memory' , 
        'org.springframework.security.vote' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'com.springsource.org.apache.log4j' : (
        'com.sun.jdmk.comm' , 
        'javax.jms' , 
        'javax.mail' , 
        'javax.mail.internet' , 
        'javax.management' , 
        'javax.naming' , 
        'javax.swing' , 
        'javax.swing.border' , 
        'javax.swing.event' , 
        'javax.swing.table' , 
        'javax.swing.text' , 
        'javax.swing.tree' , 
        'javax.xml.parsers' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        'org.xml.sax.helpers' , 
        ), 
        'org.fosstrak.tdt.tdt' : (
        'javax.xml.bind' , 
        'javax.xml.bind.annotation' , 
        'javax.xml.datatype' , 
        'javax.xml.namespace' , 
        'javax.xml.parsers' , 
        'javax.xml.transform' , 
        'javax.xml.transform.stream' , 
        'javax.xml.xpath' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'com.springsource.org.apache.el' : (
        'javax.el' , 
        ), 
        'org.springframework.osgi.catalina.start.osgi' : (
        'javax.management' , 
        'org.apache.catalina' , 
        'org.apache.catalina.connector' , 
        'org.apache.catalina.core' , 
        'org.apache.catalina.startup' , 
        'org.apache.catalina.util' , 
        'org.apache.commons.logging' , 
        'org.apache.naming.resources' , 
        'org.osgi.framework' , 
        'org.osgi.service.url' , 
        ), 
        'com.springsource.javax.xml.soap' : (
        'javax.activation' , 
        'javax.xml.namespace' , 
        'javax.xml.transform' , 
        'javax.xml.transform.dom' , 
        'org.w3c.dom' , 
        ), 
        'com.springsource.javax.servlet' : (
        ), 
        'org.rifidi.org.springframework.context' : (
        'bsh' , 
        'com.ibm.websphere.management' , 
        'com.sun.enterprise.loader' , 
        'com.sun.net.httpserver' , 
        'edu.emory.mathcs.backport.java.util.concurrent' , 
        'groovy.lang' , 
        'javax.annotation' , 
        'javax.ejb' , 
        'javax.interceptor' , 
        'javax.jms' , 
        'javax.management' , 
        'javax.management.modelmbean' , 
        'javax.management.openmbean' , 
        'javax.management.remote' , 
        'javax.naming' , 
        'javax.persistence' , 
        'javax.persistence.spi' , 
        'javax.rmi' , 
        'javax.rmi.CORBA' , 
        'javax.xml.namespace' , 
        'javax.xml.ws' , 
        'net.sf.cglib.asm' , 
        'net.sf.cglib.core' , 
        'net.sf.cglib.proxy' , 
        'oracle.classloader.util' , 
        'org.aopalliance.aop' , 
        'org.aopalliance.intercept' , 
        'org.apache.commons.logging' , 
        'org.aspectj.weaver.loadtime' , 
        'org.codehaus.groovy.control' , 
        'org.jruby' , 
        'org.jruby.ast' , 
        'org.jruby.exceptions' , 
        'org.jruby.javasupport' , 
        'org.jruby.runtime' , 
        'org.jruby.runtime.builtin' , 
        'org.omg.CORBA' , 
        'org.omg.CORBA.portable' , 
        'org.omg.CORBA_2_3.portable' , 
        'org.springframework.aop' , 
        'org.springframework.aop.framework' , 
        'org.springframework.aop.framework.adapter' , 
        'org.springframework.aop.scope' , 
        'org.springframework.aop.support' , 
        'org.springframework.aop.target' , 
        'org.springframework.aop.target.dynamic' , 
        'org.springframework.beans' , 
        'org.springframework.beans.annotation' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.access' , 
        'org.springframework.beans.factory.annotation' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.parsing' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.beans.propertyeditors' , 
        'org.springframework.beans.support' , 
        'org.springframework.core' , 
        'org.springframework.core.annotation' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.core.task' , 
        'org.springframework.core.task.support' , 
        'org.springframework.core.type' , 
        'org.springframework.core.type.classreading' , 
        'org.springframework.core.type.filter' , 
        'org.springframework.instrument' , 
        'org.springframework.metadata' , 
        'org.springframework.orm.jpa.support' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'org.apache.xbean.spring' : (
        'com.thoughtworks.qdox' , 
        'com.thoughtworks.qdox.model' , 
        'javax.management' , 
        'javax.naming' , 
        'javax.naming.spi' , 
        'javax.xml.namespace' , 
        'org.apache.commons.logging' , 
        'org.apache.tools.ant' , 
        'org.apache.tools.ant.taskdefs' , 
        'org.apache.tools.ant.types' , 
        'org.apache.xbean.spring' , 
        'org.apache.xbean.spring.context' , 
        'org.apache.xbean.spring.context.impl' , 
        'org.apache.xbean.spring.context.v2' , 
        'org.apache.xbean.spring.context.v2c' , 
        'org.apache.xbean.spring.generator' , 
        'org.apache.xbean.spring.jndi' , 
        'org.apache.xbean.spring.util' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.config' , 
        'org.springframework.beans.factory.parsing' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.context' , 
        'org.springframework.context.support' , 
        'org.springframework.core' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.springframework.web.context.support' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'com.springsource.org.apache.catalina' : (
        'javax.annotation' , 
        'javax.annotation.security' , 
        'javax.ejb' , 
        'javax.mail' , 
        'javax.mail.internet' , 
        'javax.management' , 
        'javax.management.modelmbean' , 
        'javax.naming' , 
        'javax.naming.directory' , 
        'javax.naming.spi' , 
        'javax.persistence' , 
        'javax.security.auth' , 
        'javax.security.auth.callback' , 
        'javax.security.auth.login' , 
        'javax.security.auth.spi' , 
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.sql' , 
        'javax.xml.parsers' , 
        'javax.xml.transform' , 
        'javax.xml.transform.stream' , 
        'javax.xml.ws' , 
        'org.apache.coyote' , 
        'org.apache.juli.logging' , 
        'org.apache.tomcat.jni' , 
        'org.apache.tomcat.util' , 
        'org.apache.tomcat.util.buf' , 
        'org.apache.tomcat.util.digester' , 
        'org.apache.tomcat.util.http' , 
        'org.apache.tomcat.util.http.fileupload' , 
        'org.apache.tomcat.util.http.mapper' , 
        'org.apache.tomcat.util.log' , 
        'org.apache.tomcat.util.modeler' , 
        'org.apache.tomcat.util.modeler.modules' , 
        'org.apache.tomcat.util.net' , 
        'org.apache.tomcat.util.res' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'org.rifidi.org.relique.jdbc' : (
        ), 
        'org.syndeticlogic.minerva.tools' : (
        'gnu.io' , 
        'javax.jms' , 
        'org.apache.commons.codec' , 
        'org.apache.commons.codec.binary' , 
        'org.apache.commons.logging' , 
        'org.osgi.framework' , 
        'org.springframework.beans.factory' , 
        'org.springframework.core' , 
        'org.springframework.jdbc.datasource' , 
        'org.springframework.jms.core' , 
        ), 
        'com.springsource.javax.servlet.jsp.jstl' : (
        'javax.servlet' , 
        'javax.servlet.http' , 
        'javax.servlet.jsp' , 
        'javax.servlet.jsp.tagext' , 
        'javax.xml.parsers' , 
        'org.apache.taglibs.standard.tag.common.fmt' , 
        'org.xml.sax' , 
        'org.xml.sax.helpers' , 
        ), 
        'com.springsource.net.sf.cglib' : (
        'org.apache.tools.ant' , 
        'org.apache.tools.ant.types' , 
        'org.codehaus.aspectwerkz.hook' , 
        ), 
        'org.apache.geronimo.specs.geronimo-activation_1.1_spec' : (
        'javax.activation' , 
        ), 
        'org.eclipse.equinox.simpleconfigurator' : (
        'org.eclipse.osgi.framework.console' , 
        'org.eclipse.osgi.service.datalocation' , 
        'org.eclipse.osgi.service.resolver' , 
        'org.osgi.framework' , 
        'org.osgi.service.packageadmin' , 
        'org.osgi.service.startlevel' , 
        'org.osgi.util.tracker' , 
        ), 
        'org.springframework.beans' : (
        'javax.el' , 
        'javax.xml.parsers' , 
        'net.sf.cglib.proxy' , 
        'org.apache.commons.logging' , 
        'org.springframework.core' , 
        'org.springframework.core.annotation' , 
        'org.springframework.core.io' , 
        'org.springframework.core.io.support' , 
        'org.springframework.core.type' , 
        'org.springframework.util' , 
        'org.springframework.util.xml' , 
        'org.w3c.dom' , 
        'org.xml.sax' , 
        ), 
        'org.springframework.jdbc' : (
        'com.ibm.websphere.rsadapter' , 
        'com.ibm.ws.rsadapter.jdbc' , 
        'com.mchange.v2.c3p0' , 
        'com.sun.rowset' , 
        'javax.naming' , 
        'javax.sql' , 
        'javax.sql.rowset' , 
        'javax.transaction' , 
        'javax.xml.transform' , 
        'javax.xml.transform.dom' , 
        'oracle.sql' , 
        'org.apache.commons.logging' , 
        'org.enhydra.jdbc.core' , 
        'org.jboss.resource.adapter.jdbc' , 
        'org.springframework.beans' , 
        'org.springframework.beans.factory' , 
        'org.springframework.beans.factory.support' , 
        'org.springframework.beans.factory.xml' , 
        'org.springframework.core' , 
        'org.springframework.core.io' , 
        'org.springframework.dao' , 
        'org.springframework.dao.support' , 
        'org.springframework.jndi' , 
        'org.springframework.transaction' , 
        'org.springframework.transaction.support' , 
        'org.springframework.util' , 
        'org.w3c.dom' , 
        'weblogic.jdbc.extensions' , 
        ), 
        'com.springsource.org.junit' : (
        ), 
        'com.springsource.org.apache.jasper.org.eclipse.jdt' : (
        ), 
        'com.springsource.org.apache.juli.extras' : (
        'javax.servlet' , 
        'org.apache.avalon.framework.logger' , 
        'org.apache.log' , 
        'org.apache.log4j' , 
        )}
        bundles_rbundles = { 
        'com.springsource.slf4j.jcl' : (
        'com.springsource.slf4j.api' , 
        ), 
        'org.jdom' : (
        'org.apache.xerces' , 
        ), 
        'com.springsource.slf4j.log4j' : (
        'com.springsource.slf4j.api' , 
        ), 
        'org.aspectj.weaver' : (
        'org.aspectj.runtime' , 
        ), 
        'com.springsource.org.apache.jasper' : (
        'com.springsource.org.apache.catalina' , 
        ), 
        'org.eclipse.equinox.weaving.hook' : (
        'org.eclipse.osgi' , 
        ), 
        'com.springsource.org.apache.coyote' : (
        'com.springsource.org.apache.catalina' , 
        ), 
        'org.syndeticlogic.minerva' : (
        'org.springframework.osgi.core' , 
        'org.syndeticlogic.minerva.init' , 
        'org.syndeticlogic.gnu.io' , 
        ), 
        'org.syndeticlogic.minerva.tools' : (
        'org.rifidi.org.relique.jdbc' , 
        'com.espertech.esper' , 
        'org.syndeticlogic.minerva' , 
        'org.eclipse.osgi' , 
        )}
        target_platform = { 
        'testlib/spring/org.springframework.web.servlet_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.web.servlet_2.5.6.SEC01.jar', False),
        'testlib/tomcat/com.springsource.org.apache.catalina_6.0.18.jar' :  ('testlib/tomcat', 'com.springsource.org.apache.catalina_6.0.18.jar', False),
        'testlib/javax/com.springsource.javax.xml.soap_1.3.0.jar' :  ('testlib/javax', 'com.springsource.javax.xml.soap_1.3.0.jar', False),
        'testlib/javax/com.springsource.javax.servlet.jsp.jstl_1.1.2.jar' :  ('testlib/javax', 'com.springsource.javax.servlet.jsp.jstl_1.1.2.jar', False),
        'testlib/plugins/org.eclipse.equinox.simpleconfigurator_1.0.100.v20090520-1905.jar' :  ('testlib/plugins', 'org.eclipse.equinox.simpleconfigurator_1.0.100.v20090520-1905.jar', False),
        'testlib/plugins/org.eclipse.equinox.weaving.hook_1.0.0.200905031323.jar' :  ('testlib/plugins', 'org.eclipse.equinox.weaving.hook_1.0.0.200905031323.jar', False),
        'testlib/libraries/org.jdom_1.0.0.v200806100616.jar' :  ('testlib/libraries', 'org.jdom_1.0.0.v200806100616.jar', False),
        'testlib/tomcat/com.springsource.org.apache.jasper.org.eclipse.jdt_6.0.18.jar' :  ('testlib/tomcat', 'com.springsource.org.apache.jasper.org.eclipse.jdt_6.0.18.jar', False),
        'testlib/logging/com.springsource.slf4j.api_1.5.6.jar' :  ('testlib/logging', 'com.springsource.slf4j.api_1.5.6.jar', False),
        'testlib/javax/com.springsource.javax.xml.stream_1.0.1.jar' :  ('testlib/javax', 'com.springsource.javax.xml.stream_1.0.1.jar', False),
        'testlib/plugins/org.eclipse.osgi_3.5.0.v20090520.jar' :  ('testlib/plugins', 'org.eclipse.osgi_3.5.0.v20090520.jar', False),
        'testlib/spring/org.rifidi.org.springframework.aop_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.rifidi.org.springframework.aop_2.5.6.SEC01.jar', False),
        'testlib/javax/com.springsource.javax.el_1.0.0.jar' :  ('testlib/javax', 'com.springsource.javax.el_1.0.0.jar', False),
        'testlib/spring/org.springframework.bundle.spring.aspects_2.5.5.jar' :  ('testlib/spring', 'org.springframework.bundle.spring.aspects_2.5.5.jar', False),
        'testlib/javax/com.springsource.javax.xml.rpc_1.1.0.jar' :  ('testlib/javax', 'com.springsource.javax.xml.rpc_1.1.0.jar', False),
        'testlib/libraries/org.apache.derby_10.5.1.1_201005192117.jar' :  ('testlib/libraries', 'org.apache.derby_10.5.1.1_201005192117.jar', False),
        'testlib/javax/org.apache.geronimo.specs.geronimo-javamail_1.4_spec_1.3.0.jar' :  ('testlib/javax', 'org.apache.geronimo.specs.geronimo-javamail_1.4_spec_1.3.0.jar', False),
        'testlib/aspectj/org.aspectj.weaver_1.6.4.20090304172355' :  ('testlib/aspectj', 'org.aspectj.weaver_1.6.4.20090304172355', True),
        'testlib/tomcat/com.springsource.org.apache.jasper_6.0.18.jar' :  ('testlib/tomcat', 'com.springsource.org.apache.jasper_6.0.18.jar', False),
        'testlib/spring/org.springframework.bundle.osgi.web.extender_1.1.3.jar' :  ('testlib/spring', 'org.springframework.bundle.osgi.web.extender_1.1.3.jar', False),
        'testlib/libraries/org.apache.activemq.kahadb_5.3.0.jar' :  ('testlib/libraries', 'org.apache.activemq.kahadb_5.3.0.jar', False),
        'testlib/spring/org.springframework.web_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.web_2.5.6.SEC01.jar', False),
        'testlib/javax/javax.servlet_2.5.0.v200806031605.jar' :  ('testlib/javax', 'javax.servlet_2.5.0.v200806031605.jar', False),
        'testlib/spring/com.springsource.org.junit_4.8.1.jar' :  ('testlib/spring', 'com.springsource.org.junit_4.8.1.jar', False),
        'testlib/spring/org.springframework.osgi.web_1.1.3.RELEASE.jar' :  ('testlib/spring', 'org.springframework.osgi.web_1.1.3.RELEASE.jar', False),
        'testlib/javax/com.springsource.javax.annotation_1.0.0.jar' :  ('testlib/javax', 'com.springsource.javax.annotation_1.0.0.jar', False),
        'testlib/tomcat/com.springsource.org.apache.coyote_6.0.18.jar' :  ('testlib/tomcat', 'com.springsource.org.apache.coyote_6.0.18.jar', False),
        'testlib/plugins/org.eclipse.osgi.services_3.2.0.v20090520-1800.jar' :  ('testlib/plugins', 'org.eclipse.osgi.services_3.2.0.v20090520-1800.jar', False),
        'testlib/spring/com.springsource.org.aopalliance_1.0.0.jar' :  ('testlib/spring', 'com.springsource.org.aopalliance_1.0.0.jar', False),
        'testlib/libraries/org.rifidi.org.relique.jdbc_1.0.0.jar' :  ('testlib/libraries', 'org.rifidi.org.relique.jdbc_1.0.0.jar', False),
        'testlib/plugins/com.mysql.jdbc_5.1.10.jar' :  ('testlib/plugins', 'com.mysql.jdbc_5.1.10.jar', False),
        'testlib/logging/com.springsource.slf4j.jcl_1.5.6.jar' :  ('testlib/logging', 'com.springsource.slf4j.jcl_1.5.6.jar', False),
        'testlib/spring/org.springframework.osgi.extender_1.1.3.RELEASE.jar' :  ('testlib/spring', 'org.springframework.osgi.extender_1.1.3.RELEASE.jar', False),
        'testlib/libraries/org.apache.felix.bundlerepository_1.5.0.SNAPSHOT.jar' :  ('testlib/libraries', 'org.apache.felix.bundlerepository_1.5.0.SNAPSHOT.jar', False),
        'testlib/spring/org.springframework.beans_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.beans_2.5.6.SEC01.jar', False),
        'testlib/spring/org.springframework.jms_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.jms_2.5.6.SEC01.jar', False),
        'testlib/spring/org.springframework.orm_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.orm_2.5.6.SEC01.jar', False),
        'testlib/logging/com.springsource.org.apache.log4j_1.2.15.jar' :  ('testlib/logging', 'com.springsource.org.apache.log4j_1.2.15.jar', False),
        'testlib/spring/org.springframework.osgi.io_1.1.3.RELEASE.jar' :  ('testlib/spring', 'org.springframework.osgi.io_1.1.3.RELEASE.jar', False),
        'testlib/spring/org.springframework.security.core_2.0.4.jar' :  ('testlib/spring', 'org.springframework.security.core_2.0.4.jar', False),
        'testlib/aspectj/org.aspectj.runtime_1.6.4.20090304172355' :  ('testlib/aspectj', 'org.aspectj.runtime_1.6.4.20090304172355', True),
        'testlib/tomcat/com.springsource.org.apache.el_6.0.18.jar' :  ('testlib/tomcat', 'com.springsource.org.apache.el_6.0.18.jar', False),
        'testlib/libraries/org.syndeticlogic.gnu.io_2.1.7' :  ('testlib/libraries', 'org.syndeticlogic.gnu.io_2.1.7', True),
        'testlib/javax/com.springsource.javax.ejb_3.0.0.jar' :  ('testlib/javax', 'com.springsource.javax.ejb_3.0.0.jar', False),
        'testlib/javax/com.springsource.javax.xml.ws_2.1.1.jar' :  ('testlib/javax', 'com.springsource.javax.xml.ws_2.1.1.jar', False),
        'testlib/spring/com.springsource.net.sf.cglib_2.1.3.jar' :  ('testlib/spring', 'com.springsource.net.sf.cglib_2.1.3.jar', False),
        'testlib/javax/com.springsource.javax.persistence_1.0.0.jar' :  ('testlib/javax', 'com.springsource.javax.persistence_1.0.0.jar', False),
        'testlib/spring/org.springframework.transaction_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.transaction_2.5.6.SEC01.jar', False),
        'testlib/javax/org.apache.geronimo.specs.geronimo-jms_1.1_spec_1.1.1.jar' :  ('testlib/javax', 'org.apache.geronimo.specs.geronimo-jms_1.1_spec_1.1.1.jar', False),
        'testlib/spring/org.springframework.context.support_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.context.support_2.5.6.SEC01.jar', False),
        'testlib/logging/com.springsource.org.apache.commons.logging_1.1.1.jar' :  ('testlib/logging', 'com.springsource.org.apache.commons.logging_1.1.1.jar', False),
        'testlib/javax/org.apache.geronimo.specs.geronimo-activation_1.1_spec_1.0.2.jar' :  ('testlib/javax', 'org.apache.geronimo.specs.geronimo-activation_1.1_spec_1.0.2.jar', False),
        'testlib/javax/com.springsource.javax.servlet.jsp_2.1.0.jar' :  ('testlib/javax', 'com.springsource.javax.servlet.jsp_2.1.0.jar', False),
        'testlib/javax/com.springsource.javax.servlet_2.5.0.jar' :  ('testlib/javax', 'com.springsource.javax.servlet_2.5.0.jar', False),
        'testlib/tomcat/com.springsource.org.apache.juli.extras_6.0.18.jar' :  ('testlib/tomcat', 'com.springsource.org.apache.juli.extras_6.0.18.jar', False),
        'testlib/logging/com.springsource.slf4j.log4j_1.5.6.jar' :  ('testlib/logging', 'com.springsource.slf4j.log4j_1.5.6.jar', False),
        'testlib/spring/org.springframework.core_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.core_2.5.6.SEC01.jar', False),
        'testlib/spring/org.springframework.osgi.core_1.1.3.RELEASE.jar' :  ('testlib/spring', 'org.springframework.osgi.core_1.1.3.RELEASE.jar', False),
        'testlib/libraries/org.rifidi.org.llrp.ltk_1.0.6.jar' :  ('testlib/libraries', 'org.rifidi.org.llrp.ltk_1.0.6.jar', False),
        'testlib/spring/org.rifidi.org.springframework.context_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.rifidi.org.springframework.context_2.5.6.SEC01.jar', False),
        'testlib/tomcat/com.springsource.org.apache.taglibs.standard_1.1.2.jar' :  ('testlib/tomcat', 'com.springsource.org.apache.taglibs.standard_1.1.2.jar', False),
        'testlib/spring/org.springframework.jdbc_2.5.6.SEC01.jar' :  ('testlib/spring', 'org.springframework.jdbc_2.5.6.SEC01.jar', False),
        'testlib/tomcat/org.springframework.osgi.catalina.start.osgi_1.0.0.SNAPSHOT.jar' :  ('testlib/tomcat', 'org.springframework.osgi.catalina.start.osgi_1.0.0.SNAPSHOT.jar', False),
        'testlib/libraries/org.apache.xbean.spring_3.6.0.jar' :  ('testlib/libraries', 'org.apache.xbean.spring_3.6.0.jar', False),
        'testlib/libraries/org.apache.activemq.activemq-core_5.3.0.jar' :  ('testlib/libraries', 'org.apache.activemq.activemq-core_5.3.0.jar', False),
        'testlib/libraries/org.fosstrak.tdt.tdt_0.9.0.jar' :  ('testlib/libraries', 'org.fosstrak.tdt.tdt_0.9.0.jar', False),
        'testlib/javax/org.apache.geronimo.specs.geronimo-j2ee-management_1.1_spec_1.0.1.jar' :  ('testlib/javax', 'org.apache.geronimo.specs.geronimo-j2ee-management_1.1_spec_1.0.1.jar', False),
        'testlib/plugins/org.eclipse.equinox.launcher_1.0.201.R35x_v20090715.jar' :  ('testlib/plugins', 'org.eclipse.equinox.launcher_1.0.201.R35x_v20090715.jar', False),
        'testlib/libraries/org.rifidi.org.apache.mina-core_1.0.0.jar' :  ('testlib/libraries', 'org.rifidi.org.apache.mina-core_1.0.0.jar', False),
        'testlib/libraries/org.apache.activemq.activemq-pool_5.3.0.jar' :  ('testlib/libraries', 'org.apache.activemq.activemq-pool_5.3.0.jar', False),
        'testlib/javax/com.springsource.javax.xml.bind_2.0.0.jar' :  ('testlib/javax', 'com.springsource.javax.xml.bind_2.0.0.jar', False)
        }

        for bundle in deps.bundles.values():
            self.assertTrue(bundle.sym_name in bundles_epackages)
            self.assertEquals(bundle.epackages.__len__(),
                            bundles_epackages[bundle.sym_name].__len__())
            for epackage in bundle.epackages:
                self.assertTrue(epackage.name in bundles_epackages[bundle.sym_name])    
            self.assertTrue(bundle.sym_name in bundles_ipackages)
            self.assertEquals(bundle.ipackages.__len__(),
                            bundles_ipackages[bundle.sym_name].__len__())
            for ipackage in bundle.ipackages:
                self.assertTrue(ipackage.name in bundles_ipackages[bundle.sym_name])            
            
            if bundle.rbundles.__len__() == 0:
                continue
            
            self.assertTrue(bundle.sym_name in bundles_rbundles)
            self.assertEquals(bundle.rbundles.__len__(),
                            bundles_rbundles[bundle.sym_name].__len__())
            for rbundle in bundle.rbundles:
                self.assertTrue(rbundle.name in bundles_rbundles[bundle.sym_name])            

        for i in deps.target_platform.keys():
            self.assertEquals(target_platform.__len__(), deps.target_platform.keys().__len__())
            self.assertTrue(i in target_platform)
            self.assertEquals(target_platform[i], deps.target_platform[i])

class TestBinaryBundleFinder(unittest.TestCase):
        
    def testFind(self):
        bfinder = BinaryBundleFinder()
        jar_path = ['testlib']
        bfinder.find(jar_path)

        files = ['aspectjrt.jar',\
        'aspectjweaver.jar',\
        'com.springsource.javax.annotation_1.0.0.jar',\
        'com.springsource.javax.ejb_3.0.0.jar',\
        'com.springsource.javax.el_1.0.0.jar',\
        'com.springsource.javax.persistence_1.0.0.jar',\
        'com.springsource.javax.servlet.jsp.jstl_1.1.2.jar',\
        'com.springsource.javax.servlet.jsp_2.1.0.jar',\
        'com.springsource.javax.servlet_2.5.0.jar',\
        'com.springsource.javax.xml.bind_2.0.0.jar',\
        'com.springsource.javax.xml.rpc_1.1.0.jar',\
        'com.springsource.javax.xml.soap_1.3.0.jar',\
        'com.springsource.javax.xml.stream_1.0.1.jar',\
        'com.springsource.javax.xml.ws_2.1.1.jar',\
        'javax.servlet_2.5.0.v200806031605.jar',\
        'org.apache.geronimo.specs.geronimo-activation_1.1_spec_1.0.2.jar',\
        'org.apache.geronimo.specs.geronimo-j2ee-management_1.1_spec_1.0.1.jar',\
        'org.apache.geronimo.specs.geronimo-javamail_1.4_spec_1.3.0.jar',\
        'org.apache.geronimo.specs.geronimo-jms_1.1_spec_1.1.1.jar',\
        'org.apache.activemq.activemq-core_5.3.0.jar',\
        'org.apache.activemq.activemq-pool_5.3.0.jar',\
        'org.apache.activemq.kahadb_5.3.0.jar',\
        'org.apache.derby_10.5.1.1_201005192117.jar',\
        'org.apache.felix.bundlerepository_1.5.0.SNAPSHOT.jar',\
        'org.apache.xbean.spring_3.6.0.jar',\
        'org.fosstrak.tdt.tdt_0.9.0.jar',\
        'org.jdom_1.0.0.v200806100616.jar',\
        'org.rifidi.org.apache.mina-core_1.0.0.jar',\
        'org.rifidi.org.llrp.ltk_1.0.6.jar',\
        'org.rifidi.org.relique.jdbc_1.0.0.jar',\
        'RXTXcomm.jar',\
        'com.springsource.org.apache.commons.logging_1.1.1.jar',\
        'com.springsource.org.apache.log4j_1.2.15.jar',\
        'com.springsource.slf4j.api_1.5.6.jar',\
        'com.springsource.slf4j.jcl_1.5.6.jar',\
        'com.springsource.slf4j.log4j_1.5.6.jar',\
        'com.mysql.jdbc_5.1.10.jar',\
        'org.eclipse.equinox.launcher_1.0.201.R35x_v20090715.jar',\
        'org.eclipse.equinox.simpleconfigurator_1.0.100.v20090520-1905.jar',\
        'org.eclipse.equinox.weaving.hook_1.0.0.200905031323.jar',\
        'org.eclipse.osgi.services_3.2.0.v20090520-1800.jar',\
        'org.eclipse.osgi_3.5.0.v20090520.jar',\
        'com.springsource.net.sf.cglib_2.1.3.jar',\
        'com.springsource.org.aopalliance_1.0.0.jar',\
        'com.springsource.org.junit_4.8.1.jar',\
        'org.rifidi.org.springframework.aop_2.5.6.SEC01.jar',\
        'org.rifidi.org.springframework.context_2.5.6.SEC01.jar',\
        'org.springframework.beans_2.5.6.SEC01.jar',\
        'org.springframework.bundle.osgi.web.extender_1.1.3.jar',\
        'org.springframework.bundle.spring.aspects_2.5.5.jar',\
        'org.springframework.context.support_2.5.6.SEC01.jar',\
        'org.springframework.core_2.5.6.SEC01.jar',\
        'org.springframework.jdbc_2.5.6.SEC01.jar',\
        'org.springframework.jms_2.5.6.SEC01.jar',\
        'org.springframework.orm_2.5.6.SEC01.jar',\
        'org.springframework.osgi.core_1.1.3.RELEASE.jar',\
        'org.springframework.osgi.extender_1.1.3.RELEASE.jar',\
        'org.springframework.osgi.io_1.1.3.RELEASE.jar',\
        'org.springframework.osgi.web_1.1.3.RELEASE.jar',\
        'org.springframework.security.core_2.0.4.jar',\
        'org.springframework.transaction_2.5.6.SEC01.jar',\
        'org.springframework.web.servlet_2.5.6.SEC01.jar',\
        'org.springframework.web_2.5.6.SEC01.jar',\
        'com.springsource.org.apache.catalina_6.0.18.jar',\
        'com.springsource.org.apache.coyote_6.0.18.jar',\
        'com.springsource.org.apache.el_6.0.18.jar',\
        'com.springsource.org.apache.jasper.org.eclipse.jdt_6.0.18.jar',\
        'com.springsource.org.apache.jasper_6.0.18.jar',\
        'com.springsource.org.apache.juli.extras_6.0.18.jar',\
        'com.springsource.org.apache.taglibs.standard_1.1.2.jar',\
        'org.springframework.osgi.catalina.start.osgi_1.0.0.SNAPSHOT.jar']

        self.assertEqual(files.__len__(), bfinder.jar_files.__len__())
        for i in files:
            found = False
            for j in bfinder.jar_files:
                if i == j[1]:
                    found = True
                    bfinder.jar_files.remove(j)
                    
            if not found:
                print 'did not find ' + i
                self.assertFalse(True)
        
#        print bfinder.target_platform
        tp_values = bfinder.target_platform.values()
        bundle_dirs = ['org.aspectj.runtime_1.6.4.20090304172355', 'org.aspectj.weaver_1.6.4.20090304172355', 'org.syndeticlogic.gnu.io_2.1.7']
        self.assertEqual(bundle_dirs.__len__(), tp_values.__len__())
        for i in bundle_dirs:
            found = False
            for j in tp_values:
                if i == j[1]:
                    found = True
                    self.assertTrue(True, j[2])
                    tp_values.remove(j)
            if not found:
                print 'did not find ', i
                self.assertFalse(True)
                
    def testLoad(self):
        bfinder = BinaryBundleFinder()
        jar_path = ['testlib']
        bfinder.find(jar_path)
        bfinder.load()

        bundles = ['org.aspectj.runtime',
        'org.aspectj.weaver',
        'org.syndeticlogic.gnu.io',
        'com.springsource.javax.annotation',
        'com.springsource.javax.ejb',
        'com.springsource.javax.el',
        'com.springsource.javax.persistence',
        'com.springsource.javax.servlet.jsp.jstl',
        'com.springsource.javax.servlet.jsp',
        'com.springsource.javax.servlet',
        'com.springsource.javax.xml.bind',
        'com.springsource.javax.xml.rpc',
        'com.springsource.javax.xml.soap',
        'com.springsource.javax.xml.stream',
        'com.springsource.javax.xml.ws',
        'javax.servlet',
        'org.apache.geronimo.specs.geronimo-activation_1.1_spec',
        'org.apache.geronimo.specs.geronimo-j2ee-management_1.1_spec',
        'org.apache.geronimo.specs.geronimo-javamail_1.4_spec',
        'org.apache.geronimo.specs.geronimo-jms_1.1_spec',
        'org.apache.activemq.activemq-core',
        'org.apache.activemq.activemq-pool',
        'org.apache.activemq.kahadb',
        'org.apache.derby',
        'org.apache.felix.bundlerepository',
        'org.apache.xbean.spring',
        'org.fosstrak.tdt.tdt',
        'org.jdom',
        'org.rifidi.org.apache.mina-core',
        'org.rifidi.org.llrp.ltk',
        'org.rifidi.org.relique.jdbc',
        'com.springsource.org.apache.commons.logging',
        'com.springsource.org.apache.log4j',
        'com.springsource.slf4j.api',
        'com.springsource.slf4j.jcl',
        'com.springsource.slf4j.log4j',
        'com.mysql.jdbc',
        'org.eclipse.equinox.launcher',
        'org.eclipse.equinox.simpleconfigurator',
        'org.eclipse.equinox.weaving.hook',
        'org.eclipse.osgi.services',
        'org.eclipse.osgi',
        'com.springsource.net.sf.cglib',
        'com.springsource.org.aopalliance',
        'com.springsource.org.junit',
        'org.rifidi.org.springframework.aop',
        'org.rifidi.org.springframework.context',
        'org.springframework.beans',
        'org.springframework.bundle.osgi.web.extender',
        'org.springframework.bundle.spring.aspects',
        'org.springframework.context.support',
        'org.springframework.core',
        'org.springframework.jdbc',
        'org.springframework.jms',
        'org.springframework.orm',
        'org.springframework.osgi.core',
        'org.springframework.osgi.extender',
        'org.springframework.osgi.io',
        'org.springframework.osgi.web',
        'org.springframework.security.core',
        'org.springframework.transaction',
        'org.springframework.web.servlet',
        'org.springframework.web',
        'com.springsource.org.apache.catalina',
        'com.springsource.org.apache.coyote',
        'com.springsource.org.apache.el',
        'com.springsource.org.apache.jasper.org.eclipse.jdt',
        'com.springsource.org.apache.jasper',
        'com.springsource.org.apache.juli.extras',
        'com.springsource.org.apache.taglibs.standard',
        'org.springframework.osgi.catalina.start.osgi']
        
        self.assertEqual(bundles.__len__(), bfinder.bundles.__len__())
        bf_bundles = bfinder.bundles
        for i in bundles:
            found = False
            for j in bf_bundles:
                if i == j.sym_name:
                    found = True
                    bf_bundles.remove(j)
                    if i == 'org.aspectj.runtime':
                        self.assertTrue(j.binary_bundle_dir)
                        self.assertEquals(1, j.classpath_jars.__len__())
                        self.assertEquals('aspectjrt.jar', j.classpath_jars[0])
                    elif i == 'org.aspectj.weaver':
                        self.assertTrue(j.binary_bundle_dir)
                        self.assertEquals(1, j.classpath_jars.__len__())
                        self.assertEquals('aspectjweaver.jar', j.classpath_jars[0])
                    elif i == 'org.syndeticlogic.gnu.io':
                        self.assertTrue(j.binary_bundle_dir)
                        self.assertEquals(1, j.classpath_jars.__len__())
                        self.assertEquals('RXTXcomm.jar', j.classpath_jars[0])

            if not found:
                print 'did not find ' + i
                self.assertFalse(True)
        targets =[ ('org.syndeticlogic.gnu.io_2.1.7', True),
        ('org.springframework.bundle.spring.aspects_2.5.5.jar', False),
        ('com.springsource.org.apache.catalina_6.0.18.jar', False),
        ('org.springframework.osgi.extender_1.1.3.RELEASE.jar', False),
        ('org.eclipse.equinox.launcher_1.0.201.R35x_v20090715.jar', False),
        ('com.springsource.javax.xml.rpc_1.1.0.jar', False),
        ('com.springsource.org.apache.taglibs.standard_1.1.2.jar', False),
        ('org.rifidi.org.relique.jdbc_1.0.0.jar', False),
        ('org.apache.geronimo.specs.geronimo-j2ee-management_1.1_spec_1.0.1.jar', False),
        ('org.springframework.osgi.core_1.1.3.RELEASE.jar', False),
        ('org.springframework.beans_2.5.6.SEC01.jar', False),
        ('com.springsource.slf4j.log4j_1.5.6.jar', False),
        ('org.aspectj.weaver_1.6.4.20090304172355', True),
        ('org.springframework.web.servlet_2.5.6.SEC01.jar', False),
        ('org.springframework.osgi.catalina.start.osgi_1.0.0.SNAPSHOT.jar', False),
        ('org.springframework.jdbc_2.5.6.SEC01.jar', False),
        ('com.springsource.org.apache.jasper.org.eclipse.jdt_6.0.18.jar', False),
        ('org.apache.activemq.kahadb_5.3.0.jar', False),
        ('org.springframework.transaction_2.5.6.SEC01.jar', False),
        ('org.springframework.context.support_2.5.6.SEC01.jar', False),
        ('org.jdom_1.0.0.v200806100616.jar', False),
        ('com.springsource.org.apache.coyote_6.0.18.jar', False),
        ('javax.servlet_2.5.0.v200806031605.jar', False),
        ('org.springframework.web_2.5.6.SEC01.jar', False),
        ('org.apache.geronimo.specs.geronimo-activation_1.1_spec_1.0.2.jar', False),
        ('org.apache.activemq.activemq-pool_5.3.0.jar', False),
        ('org.apache.geronimo.specs.geronimo-jms_1.1_spec_1.1.1.jar', False),
        ('com.springsource.org.apache.juli.extras_6.0.18.jar', False),
        ('com.springsource.javax.servlet_2.5.0.jar', False),
        ('com.springsource.org.aopalliance_1.0.0.jar', False),
        ('org.aspectj.runtime_1.6.4.20090304172355', True),
        ('com.springsource.org.apache.log4j_1.2.15.jar', False),
        ('org.springframework.core_2.5.6.SEC01.jar', False),
        ('com.springsource.slf4j.jcl_1.5.6.jar', False),
        ('com.springsource.net.sf.cglib_2.1.3.jar', False),
        ('org.apache.geronimo.specs.geronimo-javamail_1.4_spec_1.3.0.jar', False),
        ('com.springsource.javax.el_1.0.0.jar', False),
        ('org.rifidi.org.apache.mina-core_1.0.0.jar', False),
        ('com.springsource.javax.xml.ws_2.1.1.jar', False),
        ('com.springsource.javax.annotation_1.0.0.jar', False),
        ('com.springsource.javax.ejb_3.0.0.jar', False),
        ('org.rifidi.org.llrp.ltk_1.0.6.jar', False),
        ('com.springsource.javax.servlet.jsp.jstl_1.1.2.jar', False),
        ('com.mysql.jdbc_5.1.10.jar', False),
        ('com.springsource.javax.persistence_1.0.0.jar', False),
        ('org.eclipse.equinox.simpleconfigurator_1.0.100.v20090520-1905.jar', False),
        ('org.fosstrak.tdt.tdt_0.9.0.jar', False),
        ('com.springsource.javax.servlet.jsp_2.1.0.jar', False),
        ('org.springframework.osgi.web_1.1.3.RELEASE.jar', False),
        ('org.eclipse.osgi_3.5.0.v20090520.jar', False),
        ('org.rifidi.org.springframework.aop_2.5.6.SEC01.jar', False),
        ('org.apache.activemq.activemq-core_5.3.0.jar', False),
        ('org.springframework.osgi.io_1.1.3.RELEASE.jar', False),
        ('com.springsource.org.apache.commons.logging_1.1.1.jar', False),
        ('org.springframework.security.core_2.0.4.jar', False),
        ('com.springsource.org.apache.el_6.0.18.jar', False),
        ('com.springsource.javax.xml.bind_2.0.0.jar', False),
        ('org.eclipse.osgi.services_3.2.0.v20090520-1800.jar', False),
        ('com.springsource.javax.xml.stream_1.0.1.jar', False),
        ('org.springframework.jms_2.5.6.SEC01.jar', False),
        ('com.springsource.slf4j.api_1.5.6.jar', False),
        ('org.apache.xbean.spring_3.6.0.jar', False),
        ('com.springsource.javax.xml.soap_1.3.0.jar', False),
        ('org.apache.felix.bundlerepository_1.5.0.SNAPSHOT.jar', False),
        ('org.apache.derby_10.5.1.1_201005192117.jar', False),
        ('org.springframework.bundle.osgi.web.extender_1.1.3.jar', False),
        ('com.springsource.org.apache.jasper_6.0.18.jar', False),
        ('org.springframework.orm_2.5.6.SEC01.jar', False),
        ('org.rifidi.org.springframework.context_2.5.6.SEC01.jar', False),
        ('org.eclipse.equinox.weaving.hook_1.0.0.200905031323.jar', False),
        ('com.springsource.org.junit_4.8.1.jar', False)]
        
        bf_target_values = bfinder.target_platform.values()
        self.assertEquals(targets.__len__(), bf_target_values.__len__())
        for i in targets:
            found = False
            for j in bf_target_values:
                if i == j[1:]:
                    found = True
                    bf_target_values.remove(j)
            if not found:
                print 'did not find ' + i
                self.assertFalse(True)
                
class TestSourceBundleFinder(unittest.TestCase):
    def testFind(self):
        sfinder = SourceBundleFinder()
        src_path = ['org.syndeticlogic.minerva',
                    'org.syndeticlogic.minerva.tools']
        sfinder.find(src_path)
            
        srcs = [('org.syndeticlogic.minerva', 'META-INF', {}),
         ('org.syndeticlogic.minerva.tools', 'META-INF',
         {'org.syndeticlogic.minerva.tools/lib/spring-ws-1.5.9-all.jar': 'org.syndeticlogic.minerva.tools/lib/spring-ws-1.5.9-all.jar', 'org.syndeticlogic.minerva.tools/lib/jackson-mapper-asl-1.5.5.jar': 'org.syndeticlogic.minerva.tools/lib/jackson-mapper-asl-1.5.5.jar', 'org.syndeticlogic.minerva.tools/lib/jackson-core-asl-1.5.5.jar': 'org.syndeticlogic.minerva.tools/lib/jackson-core-asl-1.5.5.jar'})
         ]
        
        src_manifests = sfinder.src_manifests
        self.assertEquals(len(srcs), len(src_manifests))
        for i in srcs:
            found = False
            for j in src_manifests:
                if i == j:
                    found = True
                    src_manifests.remove(j)
            if not found:
                print 'did not find ' + i
                self.assertFalse(True)                    
            
    def testLoad(self):
        sfinder = SourceBundleFinder()
        src_path = ['org.syndeticlogic.minerva',
                    'org.syndeticlogic.minerva.tools']
        sfinder.find(src_path)
        sfinder.load()
        src_bundles = [('org.syndeticlogic.minerva', {} ),
                       ('org.syndeticlogic.minerva.tools', 
                        { 
        'org.syndeticlogic.minerva.tools/lib/spring-ws-1.5.9-all.jar': 
            'org.syndeticlogic.minerva.tools/lib/spring-ws-1.5.9-all.jar', 
        'org.syndeticlogic.minerva.tools/lib/jackson-mapper-asl-1.5.5.jar': 
            'org.syndeticlogic.minerva.tools/lib/jackson-mapper-asl-1.5.5.jar',
        'org.syndeticlogic.minerva.tools/lib/jackson-core-asl-1.5.5.jar':
            'org.syndeticlogic.minerva.tools/lib/jackson-core-asl-1.5.5.jar'} )]
        
        bundles = sfinder.bundles
        self.assertEquals(len(src_bundles), len(bundles))
        for i in src_bundles:
            found = False
            for j in bundles:
                if i[0] == j.sym_name and i[1] == j.extra_libs:
                    found = True
                    bundles.remove(j)
            if not found:
                print 'did not find ' + i
                self.assertFalse(True)                            

###############################################################################
#
# generator.py Tests
#
class TestFileWriter:
    def __init__(self):
        self.files = {}
        self.current = None
        self.closed = {}
        
    def get_cwd(self):
        assert self.current
        return 'test-home'
        
    def create_build_file(self, root_dir):
        self.current = root_dir
        self.files[self.current] = ''
        self.closed[self.current] = False
        
    def write(self, value):
        assert self.current
        self.files[self.current] += value
        
    def close_build_file(self):
        self.closed[self.current] = True
        self.current = None
        
class AntGeneratorTest(unittest.TestCase):
    
    minerva = '<?xml version="1.0"?>\n'+\
    '<project name="org.syndeticlogic.minerva" default="compile" basedir="test-home">\n'+\
        '\t<property name="lib" value="test-home/lib" />\n'+\
        '\t<property name="src" value="../minerva/src" />\n'+\
        '\t<property name="build" value="../minerva/bin" />\n'+\
        '\t<property name="manifest" value="../minerva/META-INF/MANIFEST.MF" />\n'+\
        '\t<property name="metainf" value="../minerva/META-INF" />\n'+\
        '\t<property name="bundle" value="test-home/lib/org.syndeticlogic.minerva_1.3.jar" />\n'+\
        '\t<path id="classpath">\n'+\
            '\t\t<pathelement location="../libs/org.eclipse.osgi.jar"/>\n'+\
        '\t</path>\n'+\
        '\t<target name="init" depends="clean">\n'+\
            '\t\t<tstamp />\n'+\
            '\t\t<mkdir dir="${build}" />\n'+\
        '\t</target>\n'+\
        '\t<target name="clean" description="clean up">\n'+\
            '\t\t<delete dir="${build}" />\n'+\
        '\t</target>\n'+\
        '\t<target name="compile" depends="init">\n'+\
            '\t\t<javac srcdir="${src}" destdir="${build}" classpathRef="classpath"/>\n'+\
        '\t</target>\n'+\
        '\t<target name="package" depends="compile">\n'+\
            '\t\t<jar destfile="${bundle}" basedir="${build}" manifest="${manifest}">\n'+\
                    '\t\t\t<metainf dir="${metainf}"/>\n'+\
            '\t\t</jar>\n'+\
        '\t</target>\n'+\
    '</project>\n'
    
    minerva_tools = '<?xml version="1.0"?>\n'+\
    '<project name="org.syndeticlogic.minerva.tools" default="compile" basedir="test-home">\n'+\
            '\t<property name="lib" value="test-home/lib" />\n'+\
            '\t<property name="src" value="../minerva.tools/src" />\n'+\
            '\t<property name="build" value="../minerva.tools/bin" />\n'+\
            '\t<property name="manifest" value="../minerva.tools/META-INF/MANIFEST.MF" />\n'+\
            '\t<property name="metainf" value="../minerva.tools/META-INF" />\n'+\
            '\t<property name="bundle" value="test-home/lib/org.syndeticlogic.minerva.tools_1.3.1.jar" />\n'+\
            '\t<path id="classpath">\n'+\
                '\t\t<pathelement location="../minerva/minerva.jar/bin"/>\n'+\
                '\t\t<pathelement location="../libs/org.eclipse.osgi.jar"/>\n'+\
            '\t</path>\n'+\
            '\t<target name="init" depends="clean">\n'+\
                    '\t\t<tstamp />\n'+\
                    '\t\t<mkdir dir="${build}" />\n'+\
            '\t</target>\n'+\
            '\t<target name="clean" description="clean up">\n'+\
                    '\t\t<delete dir="${build}" />\n'+\
            '\t</target>\n'+\
            '\t<target name="compile" depends="init">\n'+\
                    '\t\t<javac srcdir="${src}" destdir="${build}" classpathRef="classpath"/>\n'+\
            '\t</target>\n'+\
            '\t<target name="package" depends="compile">\n'+\
                    '\t\t<jar destfile="${bundle}" basedir="${build}" manifest="${manifest}">\n'+\
                            '\t\t\t<metainf dir="${metainf}"/>\n'+\
                    '\t\t</jar>\n'+\
            '\t</target>\n'+\
        '</project>\n'
    
    master = '<?xml version="1.0"?>\n'+\
    '<project name="test" default="compile" basedir=".">\n'+\
            '\t<property name="lib" value="./lib" />\n'+\
            '\t<target name="init">\n'+\
                    '\t\t<delete dir="${lib}" />\n'+\
                    '\t\t<mkdir dir="${lib}" />\n'+\
            '\t</target>\n'+\
            '\t<target name="clean" description="clean up">\n'+\
                    '\t\t<ant dir="../minerva" target="clean" />\n'+\
                    '\t\t<ant dir="../minerva.tools" target="clean" />\n'+\
            '\t</target>\n'+\
            '\t<target name="compile">\n'+\
                    '\t\t<ant dir="../minerva" target="compile" />\n'+\
                    '\t\t<ant dir="../minerva.tools" target="compile" />\n'+\
            '\t</target>\n'+\
            '\t<target name="lint" description="run lint" >\n'+\
                    '\t\t<ant dir="../minerva" target="lint" />\n'+\
                    '\t\t<ant dir="../minerva.tools" target="lint" />\n'+\
            '\t</target>\n'+\
            '\t<target name="package" description="packages bundles" depends="init">\n'+\
                    '\t\t<ant dir="../minerva" target="package" />\n'+\
                    '\t\t<ant dir="../minerva.tools" target="package" />\n'+\
                    '\t\t<copy file="../libs/org.eclipse.osgi.jar" todir="${lib}" overwrite="true" />\n'+\
            '\t</target>\n'+\
    '</project>\n'
    

    def generate_stubs(self):
        src = []
        jars = []
        target_platform = []
        v = Version()
        v.set_major(1)
        
        v1 = Version()
        v1.set_major(1)
        v1.set_minor(3)
        
        v2 = Version()
        v2.set_major(1)
        v2.set_minor(3)
        v2.set_micro(1)
        
        v3 = Version()
        v3.set_major(2)
        
        p = Package('org.eclipse.osgi')
        p.set_version_range(v, True, v1, False)
        
        p1 = Package('org.syndeticlogic.minerva')
        p1.set_version_range(v, True, v3, True)

        p2 = Package('org.syndeticlogic.minerva.tools')        
        p2.set_version_range(v, True, v1, True)
        
        p3 = Package('org.syndeticlogic.minerva.adapters')
        p3.set_version_range(v2, True, v3, False)
        
        p4 = Package('org.syndeticlogic.minerva.test')

        b = Bundle()
        b.sym_name = p.name
        b.root = '../libs'
        b.file = 'org.eclipse.osgi.jar'
        b.version = v1
        b.is_binary_bundle = True
        
        b1 = Bundle()
        b1.sym_name = p1.name
        b1.root = '../minerva'
        b1.file = 'minerva.jar'
        b1.version = v1
        b1.add_epackage(p1)
        b1.add_required_bundle_lookup_info(p1)
        b1.add_dep(b)
        
        b2 = Bundle()
        b2.sym_name = p2.name
        b2.root = '../minerva.tools'
        b2.file = 'minerva.tools.jar'
        b2.version = v2
        b2.add_epackage(p2)
        b2.add_ipackage(p1)
        b2.add_dep(b1)
        target_platform = {}
        target_platform[join(b.root, b.file)] = (b.root, b.file, False)
        writer = TestFileWriter()
        
        jars.append(b)
        src.append(b1)
        src.append(b2)
        
        return (jars, src, target_platform, writer)
        
    def test_generator(self):
        #print 'test generator'
        jars, src, target_platform, writer = self.generate_stubs()
        gen = AntGenerator("test", src, target_platform, './', writer)
        gen.generate_build_files()
        top = True
        self.assertTrue('../minerva' in writer.files)
        self.assertTrue('../minerva.tools' in writer.files)
        self.assertTrue('./' in writer.files)
        
        self.assertEquals(self.minerva, writer.files['../minerva'])
        self.assertEquals(self.minerva_tools, writer.files['../minerva.tools'])
        self.assertEquals(self.master, writer.files['./'])

if __name__ == '__main__':
    unittest.main()
    

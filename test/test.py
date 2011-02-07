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
        gen = AntGenerator("test", jars, src, target_platform, './', writer)
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
    

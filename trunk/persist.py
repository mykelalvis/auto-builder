#!/usr/bin/env python

import sqlite3
import logging
import os

logger = logging.getLogger(__name__)
def set_logger_level(logLevel):
    logger.setLevel(logLevel)
    
class RelationManager:   
    def __init__(self):
        self.bundle_rvar = []
        self.import_rvar = []
        self.export_rvar = []
        self.extra_libs_rvar = []
        self.junit_rvar = []
        self.classpath_jar_rvar = []
                                 
    def add_bundle(self, bundle):
        c = sqlite3.connect('auto-build.db')
        #
        #count = c.execute('select count(id) from bundles').next()[0]
        #print count
        #if count > 0:
        #    bundle_id = c.execute('select max(id) from bundles').next()
        #
        #    print type(bundle_id), bundle_id.__len__(), type(bundle_id[0]), bundle_id[0], bundle_id
        #
        #    assert type(bundle_id) == tuple
        #    assert bundle_id.__len__() == 1
        #    assert type(bundle_id[0]) == int
        #    self.bundle_id = bundle_id[0] + 1
        #
        bt = BundleTuple(bundle)
        self.bundle_rvar.append(bt)
        
        insert_bt = 'insert into bundles values('+bt.values()+')'
        print insert_bt
        try:
            c.execute(insert_bt)
        except sqlite3.IntegrityError, sqlerr:
            logger.error('sqlite3.IntegrityError = '+str(sqlerr))
        
        for rbundle in bundle.rbundles:
            rb = RequiredBundleTuple(bt.id, rbundle.name)
            insert_rb = 'insert into required_bundles values('+rb.values()+')'
            print insert_rb
            c.execute(insert_rb)
            self.export_rvar.append(rb)
        
        for epackage in bundle.epackages:
            ex = PackageExportTuple(bt.id, epackage)
            insert_ex = 'insert into exports values('+ex.values()+')'
            print insert_ex
            c.execute(insert_ex)
            self.export_rvar.append(ex)
            
        for ipackage in bundle.ipackages:
            im = PackageImportTuple(bt.id, ipackage)
            insert_im = 'insert into imports values('+im.values()+')'
            print insert_im            
            c.execute(insert_im)                                 
            self.import_rvar.append(im)
            
        for extra_lib in bundle.extra_libs:
            exlib = ExtraLibTuple(bt.id, extra_lib)
            insert_exlib = 'insert into extra_libs values('+exlib.values()+')'
            print insert_exlib
            c.execute(insert_exlib)                                 
            self.extra_libs_rvar.append(exlib)
            
        for junit_test in bundle.junit_tests:
            junit = JUnitTuple(bt.id, junit_test[0], junit_test[1], junit_test[3])
            insert_junit = 'insert into junit_tests values('+junit.values()+')'
            print insert_junit
            c.execute(insert_junit)                                 
            self.junit_rvar.append(junit)
            
        for classpath_jar in bundle.classpath_jars:
            classpathjar = ClasspathJarTuple(bt.id, classpath_jar)
            insert_classpathjar = 'insert into classpath_jars values('+classpathjar.values()+')'
            print insert_classpathjar            
            c.execute(insert_classpathjar)                                 
            self.classpath_jar_rvar.append(classpathjar)
        
        c.commit()
        c.close()    
            

    def create_relations(self):
        bundle_relation = 'create table if not exists bundles'\
                '(id  INT primary key on conflict fail,'\
                'name TEXT prm, version_major INT, version_minor INT,'\
                'version_micro INT, version_qual TEXT, root TEXT,'\
                'is_binary_bundle INT, file TEXT, fragment INT, '\
                'fragment_host TEXT, binary_bundle_dir TEXT)'
        
        required_bundle_relation = 'create table if not exists required_bundles'\
                '(bundle_id  INT, requried_bundle_name TEXT)'
                                    
        package_export_relation = 'create table if not exists exports '\
                '(bundle_id INT,package_name_name TEXT,'\
                'version_major INT, version_minor INT, version_micro INT,'\
                'version_qual TEXT)'
            
        package_import_relation = 'create table if not exists imports '\
                '(bundle_id INT, package_name_name TEXT,'\
                'begin_version_major INT, begin_version_minor INT,'\
                'begin_version_micro INT, begin_version_qual TEXT,'\
                'end_version_major INT, end_version_minor INT, end_version_micro INT,'\
                'end_version_qual TEXT)'
        
        extra_lib_relation = 'create table if not exists extra_libs' \
                '(bundle_id INT, root TEXT, file TEXT)'
        
        junit_relation = 'create table if not exists junit_tests'\
                '(bundle_id INT, root TEXT, junit_package_name TEXT, file_name TEXT)'
        
        classpath_jar_relation = 'create table if not exists classpath_jars '\
                '(bundle_id INT, classpath_jar_filename TEXT)'

        c = sqlite3.connect('auto-build.db')
        c.execute(bundle_relation)
        c.execute(required_bundle_relation)
        c.execute(package_export_relation)
        c.execute(package_import_relation)
        c.execute(extra_lib_relation)
        c.execute(junit_relation)
        c.execute(classpath_jar_relation)
        c.commit()
        c.close()
        
        
class BundleTuple:
    def __init__(self, bundle):

        self.sym_name = bundle.sym_name
        self.vmajor = bundle.version.major
        self.vminor = bundle.version.minor
        self.vmicro = bundle.version.micro
        self.vqual = bundle.version.qual
        self.root = os.path.abspath(bundle.root)

        self.id = self.root+'.'+self.sym_name+'-'+self.vmajor+'.'+self.vminor+\
                  '.'+self.vmicro+'.'+self.vqual
        
        self.is_binary_bundle = bundle.is_binary_bundle
        self.file = bundle.file        
        self.fragment = bundle.fragment
        self.fragment_host = bundle.fragment_host
        self.binary_bundle_dir = bundle.binary_bundle_dir
        
    def values(self):
        is_binary_bundle = 0
        fragment = 0
        binary_bundle_dir = 0
        if self.is_binary_bundle:
            is_binary_bundle = 1
        if self.binary_bundle_dir:
            binary_bundle_dir = 1
        if fragment:
            fragment = 1

        ret = '"'+str(self.id)+'","'+str(self.sym_name)+'","'+str(self.vmajor)+'","'+\
                str(self.vminor)+'","'+str(self.vmicro)+'","'+str(self.vqual)+'","'+\
                str(self.root)+'","'+str(is_binary_bundle)+'","'+str(self.file)+'","'+\
                str(fragment)+'","'+str(self.fragment_host)+'","'+str(binary_bundle_dir)+'"'
        
        print ret
        return ret
class RequiredBundleTuple:
    def __init__(self, bundle_id, required_bundle_name):
        self.bundle_id = bundle_id
        self.required_bundle_name = required_bundle_name
    def values(self):
        return '"'+str(self.bundle_id)+'","'+str(self.required_bundle_name)+'"'
        
class PackageExportTuple:
    def __init__(self, bundle_id, package):
        self.bundle_id = bundle_id
        self.package_name = package.name
        self.pvmajor = package.b_version.major
        self.pvminor = package.b_version.minor
        self.pvmicro = package.b_version.micro
        self.pvqual = package.b_version.qual
        
    def values(self):
        return '"'+str(self.bundle_id)+'","'+str(self.package_name)+'","'+\
            str(self.pvmajor)+'","'+str(self.pvminor)+'","'+str(self.pvmicro)+\
            '","'+str(self.pvqual)+'"'
            
class PackageImportTuple:
    def __init__(self, bundle_id, package):
        self.bundle_id = bundle_id
        self.package_name = package.name        
        
        self.pb_vmajor = package.b_version.major
        self.pb_vminor = package.b_version.minor
        self.pb_vmicro = package.b_version.micro
        self.pb_vqual = package.b_version.qual
        
        self.pe_vmajor = package.e_version.major
        self.pe_vminor = package.e_version.minor
        self.pe_vmicro = package.e_version.micro
        self.pe_vqual = package.e_version.qual
        
    def values(self):
        return '"'+str(self.bundle_id)+'","'+str(self.package_name)+'","'+\
            str(self.pb_vmajor)+'","'+str(self.pb_vminor)+'","'+str(self.pb_vmicro)+'","'+\
            str(self.pb_vqual)+'","'+str(self.pe_vmajor)+'","'+str(self.pe_vminor)+'","'+\
            str(self.pe_vmicro)+'","'+str(self.pe_vqual)+'"'
            
class ExtraLibTuple:
    def __init__(self, bundle_id, extra_lib):
        self.bundle_id = bundle_id
        self.root = extra_lib.root
        self.file = extra_lib.file
        
    def values(self):
        return '"'+str(self.bundle_id)+'","'+str(self.root)+'","'+str(self.file)+'"'
        
class JUnitTuple:
    def __init__(self, bundle_id, junit_root, junit_package_name, junit_file_name):
        self.bundle_name = bundle_id
        self.root = junit_root
        self.package = junit_package_name
        self.file_name = junit_file_name
        
    def values(self):
        return '"'+str(self.bundle_name)+'","'+str(self.root)+'","'+str(self.package)\
            +'","'+str(self.file_name)
        
class ClasspathJarTuple:
    def __init__(self, bundle_id, classpath_jar):
        self.bundle_name = bundle_id
        self.classpath_jar = classpath_jar    
    def values(self):
        return str(self.bundle_name)+','+str(self.classpath_jar)
        
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
    
    def find_junit_tests(self, bundle):
        depth = 1
        for root, dirs, files in os.walk(bundle.root):
            for file in files:
                imports = False
                tests = False
                package = ''
                    
                # XXX - this is not the most desired solution, but it is what
                # I had time to complete.  If someone ever has a problem finding
                # tests, a more robust parser might be necessary.
                if file.endswith(r'.java'):
                    f = open(join(root, file), 'r')
                    jfile = f.read()
                    jfile = re.sub(r'\r','',  jfile)
                    jfile_lines = re.split(r'\n', jfile)
                      
                    for line in jfile_lines:
                        if re.search('import.*;', line):
                            if re.search('org.junit', line):
                                imports = True
                            elif re.search('junit.framework', line):
                                imports = True
                        elif re.search('@Test', line):
                            tests = True
                        elif re.search(\
 'class[ \t\n\r]+[a-zA-Z][a-zA-Z0-9]*[ \t\n\r]+extends[ \t\n\r]+TestCase', line):
                            tests = True                            
                        elif re.search('package', line):
                            package = line.split(' ')[1]
                            package = package.split(';')[0]
                            package = package.strip()
                            
                if imports or tests:
                    file_name = re.sub(r'\.java$', '', file)
                    #print '#####################################################', file_name
                    bundle.junit_tests.append((root, package, file_name))
                    if not tests:
                        logger.warn(join(root, file)+\
                                'has junit imports but no test methods')
                    if not imports:
                        logger.warn(join(root, file)+\
                                'has tests but no junit imports; this test '+\
                                'may not work correctly')
                                
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
                
            self.find_junit_tests(bundle)
            self.bundles.append(bundle)
            #self.bundle_table.add_bundle(bundle)
            
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

class BinaryBundleFinder:
    def __init__(self):
        self.jar_files = []
        self.bundles = []
        self.unique_bundles = {}
        self.target_platform = {}
        
    def load(self):
        tmp = tempfile.mkdtemp()
        #print tmp
        for root, file in self.jar_files:
            shutil.copy(join(root, file), tmp)
        cdir = os.getcwd()
        
        for root, dir, extra_lib_flag in self.target_platform.values():
            print root, dir 
            logger.debug(' looking up directory binary bundle: '+ \
                         join(root, dir, 'META-INF', 'MANIFEST.MF'))
            manifest_des = open(join(root, dir, 'META-INF', 'MANIFEST.MF'), 'r')
            manifest_file = manifest_des.read()
            logger.debug(manifest_file)
            parser = manifest.ManifestParser()
            bundle = parser.parse(manifest_file)
            if bundle == None:
                continue
            bundle.root = root
            bundle.file = dir
            logger.debug(bundle, bundle.sym_name)
            bundle.binary_bundle_dir = True
            assert not bundle.sym_name in self.unique_bundles
            self.unique_bundles[bundle.sym_name] = bundle
            self.bundles.append(bundle)            
                
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
#            print 'parsing ', root, file
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
            #if not(bundle.file in do_not_package_libs):
            self.target_platform[join(bundle.root,bundle.file)] =\
                    (bundle.root, bundle.file, False)
        shutil.rmtree(tmp)
            
    def display(self):
        for i in self.bundles:
            i.display()
            print '-'*80
        
    def find(self, jar_path):
        for i in jar_path:
            logger.debug('jar_path: '+str(i))
            for root, dirs, files in os.walk(i):
                for dir in dirs:
                    if dir == 'META-INF':
                        assert os.path.isdir(root)
                        (parent_root, parent) = os.path.split(root)
                        assert os.path.isdir(parent_root)
                        self.target_platform[join(parent_root,parent)] = \
                            (parent_root, parent, True)
                for file in files:
                    if file.endswith(r'.jar'):
                        self.jar_files.append((root, file))
                

class Dependencies:
    def __init__(self):
        pass        
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
            for bundle in self.src.bundles:
                if self.__partially_order__(bundle):
                    h4x0r = True
                   
        self.src.bundles = sorted(self.src.bundles, key=lambda bundle : bundle.build_level)
        
        #for bundle in src.bundles:
            #print bundle.sym_name, bundle.build_level
        #    pass
        
        return True
        
    def resolve(self):
        import manifest
        c = sqlite3.connect('auto-build.db')
        results = c.execute('select * from bundles')
        bundles = {}
        #print '---------------#######', results.next(), '####################'

        while True:
            result = results.next()
            if not result:
                break
#            print '---------------#######', result, '####################'
            bundle = manifest.Bundle()
            bundle.load_from_database(result)

            print '-------------',bundle.id, '---------------'
            bundles[bundle.id] = bundle
            
            result1 = c.execute('select * from required_bundles where required_bundles.bundle_id = "'+bundle.id+'"')
            try:
                print result1.next()
            except:
                pass

            result1 = c.execute('select * from imports where imports.bundle_id = "'+bundle.id+'"')
            try:
                print result1.next()
            except:
                pass
            
            result1 = c.execute('select * from exports where exports.bundle_id = "'+bundle.id+'"')
            try:
                print result1.next()
            except:
                pass
            
            result1 = c.execute('select * from extra_libs where extra_libs.bundle_id = "'+bundle.id+'"')
            try:
                print result1.next()
            except:
                pass
            
            result1 = c.execute('select * from junit_tests where junit_tests.bundle_id = "'+bundle.id+'"')
            try:
                print result1.next()
            except:
                pass
            
            result1 = c.execute('select * from classpath_jars where classpath_jars.bundle_id = "'+bundle.id+'"')
            try:
                print result1.next()
            except:
                pass
            return
        #    self.bundles
        
        for bundle in self.src.bundles:
            #print bundle.sym_name
            assert not bundle.sym_name in self.bundles 
            self.bundles[bundle.sym_name] = bundle
                
            for package in bundle.epackages:
                self.__add_package__(self.exports, package, bundle)
        #assert False
        
        #print bundles
            
        for bundle in self.jars.bundles:
            #print '--->'+str(bundle.sym_name)+'<---', bundle
            if not bundle.sym_name in self.bundles:
                self.bundles[bundle.sym_name] = bundle
            else:
                #print 'Bundle '+str(bundle.sym_name)+\
                #' found both binary and src;'+\
                #' using the src version (this should be an option)'
                assert join(bundle.root, bundle.file) in self.target_platform
                del self.target_platform[join(bundle.root,bundle.file)]
                
            #print bundle.display()
            for package in bundle.epackages:
                self.__add_package__(self.exports, package, bundle)
        
        #assert False
        #print bundles
        required_jars = {}
        # package.name = [(pacakge, bundle), (package, bundle)]
        for bundle in self.src.bundles:
            
            #if bundle.fragment:
            #    assert bundle.fragment_host.name in self.bundles
              
            for required_bundle_info in bundle.rbundles:
                found = False
                #print 'required bundle', bundle.sym_name, \
                #    required_bundle_info.name
                
                if required_bundle_info.name in self.bundles and \
                    required_bundle_info.is_in_range(\
                        self.bundles[required_bundle_info.name].version):
                    found = True
                    
                    if bundle.fragment and\
                        bundle.sym_name == 'com.ambient.labtrack.test':
                        
                        print 'adding dep '+str(required_bundle_info.name)+\
                           '-'+str(self.bundles[required_bundle_info.name].version),\
                           ' to ', bundle.sym_name
                        
                    print 'Adding the dep bundle = ', required_bundle_info.name,\
                           self.bundles[required_bundle_info.name]
                    
                    bundle.add_dep(self.bundles[required_bundle_info.name])
                    if self.bundles[required_bundle_info.name].is_binary_bundle:
                        required_jars[self.bundles[required_bundle_info.name].sym_name] =\
                        self.bundles[required_bundle_info.name]
                        
                if not found:
                    print 'ERROR could not find matching required bundle ',\
                        required_bundle_info.name, required_bundle_info
                        
            for package in bundle.ipackages:
                found = False
                version_found = []
                if package.name in self.exports:
                    for ex_package, ex_bundle in self.exports[package.name]:
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
                    print re.match(r'javax.xml.namespace', str(self.exports))
                    print 'ERROR: cannot resolve package: ', package.name\
                    +' for bundle '+bundle.sym_name+'; skipping it'
                    #return False
                    
        #print required_jars
        #self.required_jars = required_jars
        #assert False
        return True
        
        
if __name__ == '__main__':
    self.jfinder = BinaryBundleFinder()
    self.sfinder = SourceBundleFinder()
    self.params = Parameters()
        
    self.jfinder.find(self.params.options.jar_path)
    self.jfinder.load()            
    self.sfinder.find(self.params.options.src_path)
    self.sfinder.load()

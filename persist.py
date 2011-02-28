#!/usr/bin/env python

import sqlite3

class RelationManager:   
    def __init__(self):
        self.bundle_id = 0
        self.bundle_rvar = []
        self.import_rvar = []
        self.export_rvar = []
        self.extra_libs_rvar = []
        self.junit_rvar = []
        self.classpath_jar_rvar = []
                                 
    def add_bundle(self, bundle):
        bt = BundleTuple(self.bundle_id, bundle)
        self.bundle_id += 1
        self.bundle_rvar.append(bt)
        
        c = sqlite3.connect('auto-build.db')
        insert_bt = '''insert into bundles values('+bt.values()+')'''
        print insert_bt
        c.execute(insert_bt)
        
        for epackage in bundle.epackages:
            ex = PackageExportTuple(bt.id, epackage)
            insert_ex = 'insert into bundles values('+ex.values()+')'
            print insert_ex
            c.execute(insert_ex)
            self.export_rvar.append(ex)
            
        for ipacage in bundle.ipackages:
            im = PackageImportTuple(bt.id, ipackage)
            insert_im = 'insert into bundles values('+im.values()+')'
            print insert_im            
            c.execute(insert_im)                                 
            self.import_rvar.append(im)
            
        for extra_lib in bundle.extra_libs:
            exlib = ExtraLibTuple(bt.id, extra_lib)
            insert_exlib = 'insert into bundles values('+exlib.values()+')'
            print insert_exlib
            c.execute(insert_exlib)                                 
            self.extra_libs_rvar.append(exlib)
            
        for junit_test in bundle.junit_tests:
            junit = JUnitTuple(bt.id, junit_test[0], junit_test[1], junit_test[3])
            insert_junit = 'insert into bundles values('+junit.values()+')'
            print insert_junit
            c.execute(insert_junit)                                 
            self.junit_rvar.append(junit)
            
        for classpath_jar in bundle.claspath_jars:
            classpathjar = ClasspathJarTuple(bt.id, classpath_jar)
            insert_classpathjar = 'insert into bundles values('+classpathjar.values()+')'
            print insert_classpathjar            
            c.execute(insert_classpathjar)                                 
            self.classpath_jar_rvar.append(classpathjar)

    def create_relations(self):
        bundle_relation = 'create table if not exists bundles'\
                '(id  INT primary key on conflict fail,'\
                'name TEXT, version_major INT version_minor INT,'\
                'version_micro INT, version_qual TEXT, root TEXT,'\
                'is_binary_bundle INT, file TEXT, fragment INT, '\
                'fragment_host TEXT, binary_bundle_dir TEXT)'
        
        required_bundle_relation = 'create table if not exists required_bundles'\
                '(bundle_id  INT primary key on conflict fail, requried_bundle_name TEXT)'
                                    
        package_export_relation = 'create table if not exists exports '\
                '(bundle_id INT primary key on conflict fail,package_name_name TEXT,'\
                'version_major INT, version_minor INT, version_micro INT,'\
                'version_qual TEXT)'
            
        package_import_relation = 'create table if not exists imports '\
                '(bundle_id INT primary key on conflict fail, package_name_name TEXT,'\
                'begin_version_major INT, begin_version_minor INT,'\
                'begin_version_micro INT, begin_version_qual TEXT,'\
                'end_version_major INT, end_version_minor INT, end_version_micro INT,'\
                'end_version_qual TEXT)'
        
        extra_lib_relation = 'create table if not exists extra_libs' \
                '(bundle_id INT primary key on conflict fail, root TEXT, file TEXT)'
        
        junit_relation = 'create table if not exists junit_tests'\
                '(bundle_id INT primary key on conflict fail,'\
                'root TEXT, junit_package_name TEXT, file_name TEXT)'
        
        classpath_jar_relation = 'create table if not exists classpath_jar '\
                '(bundle_id INT primary key on conflict fail,'\
                'classpath_jar_filename TEXT)'

        c = sqlite3.connect('auto-build.db')
        c.execute(bundle_relation)
        c.execute(required_bundle_relation)
        c.execute(package_export_relation)
        c.execute(package_import_relation)
        c.execute(extra_lib_relation)
        c.execute(junit_relation)
        c.execute(classpath_jar_relation)
        
        
class BundleTuple:
    def __init__(self, bundle_id, bundle):
        self.id = bundle_id
        self.sym_name = bundle.sym_name
        self.vmajor = bundle.version.major
        self.vminor = bundle.version.minor
        self.vmicro = bundle.version.micro
        self.vqual = bundle.version.qual
        self.root = bundle.root
        self.is_binary_bundle = bundle.is_binary_bundle
        self.file = bundle.file
        self.fragment = bundle.fragment
        self.fragment_host = bundle.fragment_host
        self.binary_bundle_dir = bundle.binary_bundle_dir
        
    def values(self):
        is_binary_bundle = 0
        fragment = 0
        if self.is_binary_bundle:
            is_binary_bundle = 1
        if fragment:
            fragment = 1
            
        return str(self.id)+','+str(self.sym_name)+','+str(self.vmajor)+','+\
                str(self.vminor)+','+str(self.vmicro)+','+str(self.vqual)+','+\
                str(self.root)+','+str(is_binary_bundle)+','+str(self.file)+','+\
                str(fragment)+','+str(self.fragment_host)+','+str(self.binary_bundle_dir)
                
class RequiredBundleTuple:
    def __init__(self, bundle_id, required_bundle_name):
        self.bundle_id = bundle_id
        self.required_bundle_name = required_bundle_name
    def values(self):
        return str(self.bundle_id)+','+str(self.required_bundle_name)
        
class PackageExportTuple:
    def __init__(self, bundle_id, package):
        self.bundle_id = bundle_id
        self.package_name = package.name
        self.pvmajor = package.bversion.major
        self.pvminor = package.bversion.minor
        self.pvmicro = package.bversion.micro
        self.pvqual = package.bversion.qual
        
    def values(self):
        return str(self.bundle_id)+','+str(self.package_name)+','+str(self.pvmajor)+','+\
            str(self.pvminor)+','+str(self.pvmicro)+','+str(self.pvqual)
            
class PackageImportTuple:
    def __init__(self, bundle_id, package):
        self.bundle_id = bundle_id
        self.package_name = package.name        
        
        self.pb_vmajor = package.bversion.major
        self.pb_vminor = package.bversion.minor
        self.pb_vmicro = package.bversion.micro
        self.pb_vqual = package.bversion.qual
        
        self.pe_vmajor = package.eversion.major
        self.pe_vminor = package.eversion.minor
        self.pe_vmicro = package.eversion.micro
        self.pe_vqual = package.eversion.qual
        
    def values(self):
        return str(self.bundle_id)+','+str(self.package_name)+','+\
            str(self.pb_vmajor)+','+str(self.pb_vminor)+','+str(self.pb_vmicro)+','+\
            str(self.pb_vqual)+','+str(self.pe_vmajor)+','+str(self.pe_vminor)+','+\
            str(self.pe_vmicro)+','+str(self.pe_vqual)
            
class ExtraLibTuple:
    def __init__(self, bundle_id, extra_lib):
        self.bundle_id = bundle_id
        self.root = extra_lib.root
        self.file = extra_lib.file
        
    def values(self):
        return str(self.bundle_id)+','+str(self.root)+','+str(self.file)
        
class JUnitTuple:
    def __init__(self, bundle_id, junit_root, junit_package_name, junit_file_name):
        self.bundle_name = bundle_id
        self.root = junit_root
        self.package = junit_package_name
        self.file_name = junit_file_name
        
    def values(self):
        return str(self.bundle_name)+','+str(self.root)+','+str(self.package)\
            +','+str(self.file_name)
        
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
                
if __name__ == '__main__':
    self.jfinder = BinaryBundleFinder()
    self.sfinder = SourceBundleFinder()
    self.params = Parameters()
        
    self.jfinder.find(self.params.options.jar_path)
    self.jfinder.load()            
    self.sfinder.find(self.params.options.src_path)
    self.sfinder.load()

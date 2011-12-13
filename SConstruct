import os
import re
import subprocess
import tarfile

# Requirements
# * Python
# * PyLint
# * PyChecker
# * PyFlakes
# * Nose


###################
# Builders
###################

def build_lint(target, source, env):
    args = ['pylint']
    args.extend([str(py) for py in source])
    return subprocess.call(args)
bld_lint = Builder(action=build_lint)

def build_check(target, source, env):
    args = ['pychecker']
    args.extend([str(py) for py in source])
    return subprocess.call(args)
bld_check = Builder(action=build_check)

def build_test(target, source, env):
    args = ['nosetests', '--all-modules', 'core', 'parser', 'writer']
    return subprocess.call(args)
bld_test = Builder(action=build_test)


###################
# Filters
###################

source_re = re.compile(r'.*\.py$')
def filter_source(arg, top, names):
    for name in names:
        if source_re.match(os.path.join(top, name)):
            arg.append(File(os.path.join(top, name)))

test_re = re.compile(r'.*/(t|test)/.*_t\.py$')
def filter_test(arg, top, names):
    for name in names:
        if test_re.match(os.path.join(top, name)):
            arg.append(File(os.path.join(top, name)))


###################
# File Lists
###################

all_source = []
os.path.walk('.', filter_source, all_source)

all_tests = []
os.path.walk('.', filter_test, all_tests)

parser_tests = []
os.path.walk('./parser', filter_test, parser_tests)

writer_tests = []
os.path.walk('./writer', filter_test, writer_tests)


###################
# Environment
###################

env = Environment(BUILDERS = {'test': bld_test,
                              'lint': bld_lint,
                              'check': bld_check,
                             },
                  ENV = {'PATH' : os.environ['PATH']},
                  tools = ['default'])

lint = env.lint(['fake_target_to_force_lint'], all_source)
check = env.check(['fake_target_to_force_check'], all_source)
test = env.test(['fake_target_to_force_test'], all_tests)

env.Alias('lint', lint)
env.Alias('check', check)
env.Alias('test', test)
env.Alias('all', '.')

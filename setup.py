from distutils.core import setup
import py2exe
import glob
import os

def find_data_files(source,target,patterns):
    """Locates the specified data-files and returns the matches
    in a data_files compatible format.

    source is the root of the source data tree.
        Use '' or '.' for current directory.
    target is the root of the target data tree.
        Use '' or '.' for the distribution directory.
    patterns is a sequence of glob-patterns for the
        files you want to copy.
    """
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source,pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target,os.path.relpath(filename,      source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path,[]).append(filename)
    return sorted(ret.items())

setup(
    name='AdventureQuest',
    console=['game.py'],
    data_files=find_data_files(
        'source',
        'source',
        ['README','audio/music loops/*', 'audio/one shots/*'
    ]),
    options={
        "py2exe":{
            "unbuffered": True,
            "optimize": 2,
            "excludes": ["email"]
        }
    }

)
# NOTE: whenever a data file (not script) is added to this project, make sure it is included with those other directories in the data_files section so that they are present in the dist folder so the .exe can use them 

# how to exe: http://www.py2exe.org/index.cgi/Tutorial

# python setup.py py2exe <-- run that to build exe (python 3.4 only)
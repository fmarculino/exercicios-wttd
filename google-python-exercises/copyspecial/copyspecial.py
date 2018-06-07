#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""


# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    res = []
    paths = os.listdir(dir)
    for path in paths:
        match = re.match(r'(.*__)(\w+)(__.*)$', path)
        if match:
            res.append(path)

    return res


def copy_to(paths, dir):
    print('Tá copiando os arquivos especiais mai lirou frend.')

    for path in paths:
        shutil.copy(path, dir)

    print('Copiou os especiais para os arquivos õ.O?!')


def zip_to(paths, zippath):
    command = 'zip -j %s %s' % (zippath, ' '.join(paths))
    print('Command I\'m going to do: zip -j', zippath, ' '.join(paths))

    res = subprocess.run(command, shell=True)
    if res.returncode != 0:
        sys.exit(res.returncode)

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

        # +++your code here+++
        # Call your functions
    spaths = get_special_paths(args[0])

    if todir:
        copy_to(spaths, todir)

    if tozip:
        zip_to(spaths, tozip)

if __name__ == "__main__":
    main()

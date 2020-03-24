# Python modules
import os
import getpass
import hashlib
import pathlib
import shutil
import platform
import argparse

# Logger
from logger import Logger
logger = Logger("MyCrypto")

def get_system():
    system = platform.system()
    logger.info(system)
    if 'Linux' == system or 'Darwin' == system or 'Windows' == system:
        return system
    else:
        raise ValueError("MyCrypto: Not supported platform.")

def _encrypt_directory(path, password):
    parent = pathlib.Path(path).parent
    basename = os.path.basename(path)

    target = os.path.join(parent, basename.replace("co_", ""))
    shutil.copytree(path, target)
    
    files = []
    for root, _, filenames in os.walk(target):
        if filenames:
            files += [ os.path.join(root, filename) for filename in filenames ]
            
    for f in files:
        _encrypt_file(f, password)

    shutil.rmtree(path)

def _encrypt_file(path, password):
    parent = pathlib.Path(path).parent
    basename = os.path.basename(path)

def encrypt(path, password):
    logger.info(path)
    logger.info(password)

    if os.path.isdir(path):
        _encrypt_directory(path, password)
    else:
        shutil.copy(path)
        _encrypt_file(path, password)

def _decrypt_directory(path, password):
    parent = pathlib.Path(path).parent
    basename = os.path.basename(path)

    target = os.path.join(parent, "co_{}".format(basename))
    shutil.copytree(path, target)
    
    files = []
    for root, _, filenames in os.walk(target):
        if filenames:
            files += [ os.path.join(root, filename) for filename in filenames ]

    for f in files:
        _decrypt_file(f, password)

    shutil.rmtree(path)

def _decrypt_file(path, password):
    parent = pathlib.Path(abs_path).parent
    basename = os.path.basename(abs_path)

def decrypt(path, password):
    logger.info(path)
    logger.info(password)

    if os.path.isdir(abs_path):
        _decrypt_directory(abs_path, password)
    else:
        _decrypt_file(abs_path, password)

def main(path):
    abs_path = os.path.abspath(path)

    logger.info(abs_path)
    logger.info(basename)
    m = hashlib.sha256()

    if os.path.exists(abs_path):
        m.update(getpass.getpass("password: ").encode())
        password = m.digest()
        if basename.startswith('co_'):
            decrypt(abs_path, password)
        else:
            encrypt(abs_path, password)
    else:
        raise AttributeError("Not valid path")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', action="store", type=str)
    args = parser.parse_args()
    path = args.path
    main(path)
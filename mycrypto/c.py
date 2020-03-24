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


def encrypt(path, password):
    pass

def decrypt(path, password):
    pass

def main(path):
    abs_path = os.path.abspath(path)
    parent = pathlib.Path(abs_path).parent
    basename = os.path.basename(abs_path)

    logger.info(abs_path)
    logger.info(parent)
    logger.info(basename)
    files = []
    m = hashlib.sha256()

    if os.path.exists(abs_path):
        m.update(getpass.getpass("password: ").encode())
        password = m.digest()
        if "co_" in path:
            if os.path.isdir(abs_path):
                target = os.path.join(parent, basename.replace("co_", ""))
                shutil.copytree(abs_path, target)
                shutil.rmtree(abs_path)
                for root, _, filenames in os.walk(target):
                    if filenames:
                        files += [ os.path.join(root, filename) for filename in filenames ]
                for file in files:
                    decrypt(file, password)
            else:
                decrypt(abs_path, password)
        else:
            # encrypt
            if os.path.isdir(abs_path):
                target = os.path.join(parent, "co_{}".format(basename))
                shutil.copytree(abs_path, target)
                shutil.rmtree(abs_path)
                for root, _, filenames in os.walk(target):
                    if filenames:
                        files += [ os.path.join(root, filename) for filename in filenames ]
                for file in files:
                    encrypt(file, password)
            else:
                encrypt(abs_path, password)
        logger.info(files)
        
    else:
        raise AttributeError("Not valid path")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', action="store", type=str)
    args = parser.parse_args()
    path = args.path
    main(path)
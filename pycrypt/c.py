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
logger = Logger("PyCrypt")

def get_system():
    system = platform.system()
    logger.info(system)
    if 'Linux' == system or 'Darwin' == system or 'Windows' == system:
        return system
    else:
        raise ValueError("PyCrypto: Not supported platform.")
000
                        files += [ os.path.join(root, filename) for filename in filenames ]
                logger.info(files)
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
                logger.info(files)
                for file in files:
                    encrypt(file, password)
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
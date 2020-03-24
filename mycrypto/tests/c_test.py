# Python Modules
import os
import platform
import unittest

# MyCryptTest modules
from c import get_system
from c import trace

# logger
from logger import Logger


class MyCryptoTest(unittest.TestCase):
    def setUp(self):
        self.logger = Logger("MyCryptoTest")

    def test_get_system(self):
        system = get_system()
        self.logger.info(system)

        self.assertEqual(platform.system(), system)
        self.assertNotEqual(platform.system(), "not_supported")

    def test_trace(self):
        path = 'test_dir'
        trace(os.path.join(os.path.join(os.path.abspath(os.curdir), 'tests'), path), None)

        self.assertEqual(True, True)
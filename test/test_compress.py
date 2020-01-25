# encoding: utf-8
import json
from datetime import datetime
import unittest
from unittest.mock import Mock, patch, PropertyMock

from compress import Compress

now_str = datetime.now().strftime("%m%d%H%M%S")

class TestCompress(unittest.TestCase):

    def test_run(self):
        Compress('test/ori', 'test/res/' + now_str).run()


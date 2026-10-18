import unittest

class TestCIVerification(unittest.TestCase):
    def test_intentional_failure(self):
        self.fail("intentional ruleset gate validation failure")

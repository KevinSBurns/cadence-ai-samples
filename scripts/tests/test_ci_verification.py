import unittest

class TestCIVerification(unittest.TestCase):
    def test_intentional_failure(self):
        self.fail("intentional first-time fork CI verification failure")

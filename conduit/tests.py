from django.test import TestCase

class ConduitTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

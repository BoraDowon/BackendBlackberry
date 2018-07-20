from django.test import TestCase


# Create your tests here.
class BlackberryTest(TestCase):

    def test_example(self):
        arr = [1, 2, 3, 4]
        self.assertIs(len(arr), 4)

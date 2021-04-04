from HW10_2 import Registration
import unittest
from unittest import mock


class TestRegistration(unittest.TestCase):
    reg = Registration()

    def test_user_name(self):
        names = ['asd123', '123456', '@!&^%', 1234, 1.2123, ' ']
        for name in names:
            with mock.patch('builtins.input', return_value=name):
                print(name)
                assert self.reg.user_name() == False

    def test_user_email(self):
        emails = ['artem@', ' ', '.com', 'ASDFGHSD.COM']
        for email in emails:
            with mock.patch('builtins.input', return_value=email):
                print(email)
                assert self.reg.user_email() == False

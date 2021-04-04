from HW10_3 import Authorization
import unittest
from unittest.mock import patch


class TestAuthorization(unittest.TestCase):
    auth = Authorization()

    def test_check_email(self):
        emails = ['email@asd', 1234, 'ASDASD@GMAIL.COM', 1.123, '123.123@MAIL.UA']
        for email in emails:
            with patch('builtins.input', return_value=email):
                print(email)
                assert self.auth.check_email() == False


    def test_check_password(self):
        paswds = ['email@asd', 12, 'ASDASD@GMAIL.COM', 1.123, '123.123@MAIL.UA', 'asdd1', '!```*7123']
        for pasw in paswds:
            with patch('builtins.input', return_value=pasw):
                print(pasw)
                assert self.auth.check_password() == False



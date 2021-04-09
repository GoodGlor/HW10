from HW10_3 import Authorization
from HW10_2 import Registration
import unittest
from unittest.mock import patch




class TestAuthorization(unittest.TestCase):
    reg = Registration()

    def test_0registred_user(self):
        self.user_test = ['Jon', 'jon@gmail.com', '1234q']
        with patch('builtins.input', side_effect=self.user_test):
            self.reg.registred()


    def test_1check_email(self):
        emails = ['email@asd', 1234, 'ASDASD@GMAIL.COM', 1.123, '123.123@MAIL.UA']
        for email in emails:
            with patch('builtins.input', return_value=email):
                auth = Authorization()
                assert auth.check_email() == False


    def test_2check_password(self):
        password1 = {'jon@gmail.com':'email@asd'}
        password2 ={'jon@gmail.com': 12}
        password3 = {'jon@gmail.com':'ASDASD@GMAIL.COM'}

        passwords = [password1, password2, password3]

        for password in passwords:
            for paswd in password:
                with patch('builtins.input', return_value=paswd):
                    auth = Authorization()
                    assert auth.check_password() == False



    def test_3authorization(self):
        self.email = ['jon@gmail.com', '1234q']
        with patch('builtins.input', side_effect=self.email):
            auth = Authorization()
            auth.check_all()




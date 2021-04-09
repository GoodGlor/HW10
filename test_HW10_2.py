from HW10_2 import Registration
import unittest
from unittest import mock
from unittest.mock import patch


class TestRegistration(unittest.TestCase):
    reg = Registration()

    def test_1registred_user(self):
        self.user_test = ['Jon', 'jon@gmail.com', '1234q']
        with patch('builtins.input', side_effect=self.user_test):
            self.reg.registred()

    def test_2name_already_exist(self):
        self.user_name = 'Jon'
        with mock.patch('builtins.input', return_value=self.user_name):
            assert self.reg.user_name() == False

    def test_3email_already_exist(self):
        self.user_email = 'jon@gmail.com'
        with mock.patch('builtins.input', return_value=self.user_email):
            assert self.reg.user_email() == False

    def test_4user_name(self):
        names_false = ['asd123', '123456', '@!&^%', 1234, 1.2123, ' ', 'Андній']
        for name_false in names_false:
            with mock.patch('builtins.input', return_value=name_false):
                assert self.reg.user_name() == False

        names_true = ['jan', 'TEMA', 'aNdRiI']
        for name_true in names_true:
            with mock.patch('builtins.input', return_value=name_true):
                assert self.reg.user_name() == True

    def test_5user_email(self):
        emails_false = ['artem@', ' ', '.com', 'ASDFGHSD.COM']
        for email_false in emails_false:
            with mock.patch('builtins.input', return_value=email_false):
                assert self.reg.user_email() == False

        emails_true = ['jan@gmail.com', 'JAN123@MAIL.RU', 'k0l0s@ukr.net']
        for email_true in emails_true:
            with mock.patch('builtins.input', return_value=email_true):
                assert self.reg.user_email() == True

    def test_6user_pasw(self):
        passwords_false = ['\tasd1@asd', ' asdd asdasd\t', '\t', ' ', 'rtey  fgh', 'фівфівй']
        for password_false in passwords_false:
            with mock.patch('builtins.input', return_value=password_false):
                assert self.reg.user_pasw() == False

        passwords_true = ['P@ssw0rd', 12344, 'PASSSSSW00RD']
        for pas_true in passwords_true:
            with mock.patch('builtins.input', return_value=pas_true):
                self.assertTrue(self.reg.user_pasw())

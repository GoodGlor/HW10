import openpyxl
import re


class ErrorName(Exception):
    pass


class ErrorMail(Exception):
    pass


class Registration:
    def __init__(self):
        self.user = []
        self.wb = openpyxl.load_workbook('user.xlsx')
        self.sheet = self.wb.active


    def user_name(self):
        try:
            self.name = str(input('Name: ')).capitalize()
            if not self.name.isalpha():
                print('Please use only letters, try again')
                return False
            if self.name.isascii():
                self.check_name = [name.value for name in self.sheet['A']]
                if self.name in self.check_name:
                    raise ErrorName()
                else:
                    self.user.append(self.name)
                    return True
            else:
                print('Try enter only ascii letters')
                return False
        except ErrorName:
            print('User with this name already  created. Try another name.')
            return False

    def user_email(self):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        try:
            self.mail = str(input('Enter your email: ')).lower()
            if not (re.search(regex, self.mail)):
                print('Invalid email. Enter email')
                return False
            if self.mail.isascii():
                self.col_mail = [mail.value for mail in self.sheet['B']]
                if self.mail in self.col_mail:
                    raise ErrorMail()
                else:
                    self.user.append(self.mail)
                    return True
            else:
                print('Try enter only ascii letters')
                return False
        except ErrorMail:
            print('User with this email already  created. Try another mail.')
            return False

    def user_pasw(self):
        self.password = str(input('Enter your password: ')).lower()
        if '\t' in self.password or ' ' in self.password:
            print('Password should be without space and tabulation')
            return False
        elif not self.password.isascii():
            print('Try enter only ascii letters')
            return False
        else:
            self.user.append(''.join(self.password))
            if len(self.user) == 1:
                return self.user.pop()
            return True

    def registred(self):
        while True:

            if Registration.user_name(self) == False:
                self.user.clear()
                break
            elif Registration.user_email(self) == False:
                self.user.clear()
                break
            elif Registration.user_pasw(self) == False:
                self.user.clear()
                break
            else:
                self.sheet.append(self.user)
                self.wb.save('user.xlsx')
                self.user.clear()
                print('200')
                break

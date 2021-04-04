import openpyxl
import uuid


class Authorization:
    def __init__(self):
        self.user = []
        self.wb = openpyxl.load_workbook('user.xlsx')
        self.sheet = self.wb.active

    def check_email(self):
        self.emal = str(input('Enter your email: ')).lower()
        self.ch_emal = [email.value for email in self.sheet['B']]
        if self.emal in self.ch_emal:
            return True
        else:
            print('User with this email does not exist')
            return False

    def check_password(self):
        self.password = str(input('Enter yor password: ')).lower()
        self.ch_password = [paswd.value for paswd in self.sheet['C']]
        if self.password in self.ch_password:
            return True
        else:
            print('Invalid password')
            return False

    def check_all(self):
        while True:
            if Authorization.check_email(self) == True and Authorization.check_password(self) == True:
                print(f'OK -> {uuid.uuid4()}')
                break
            else:
                continue



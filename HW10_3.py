import openpyxl
import uuid


class UserToken :
    success = uuid.uuid4()


class Authorization:
    def __init__(self):
        self.wb = openpyxl.load_workbook('user.xlsx')
        self.sheet = self.wb.active
        self.ch_emal = [email.value for email in self.sheet['B']]
        self.ch_password = [paswd.value for paswd in self.sheet['C']]
        self.user = {self.ch_emal[index]: self.ch_password[index] for index in range(len(self.ch_emal))}
        self.emal = str(input('Enter your email: ')).lower()


    def check_email(self):
        if self.emal in self.user.keys():
            return True
        else:
            print('User with this email does not exist')
            return False

    def check_password(self):
        self.password = str(input('Enter yor password: ')).lower()
        if self.user[self.emal] == self.password:
            return True
        else:
            print('Invalid password')
            return False

    def check_all(self):
        while True:
            if Authorization.check_email(self) == True and Authorization.check_password(self) == True:
                return print(f'OK -> {UserToken.success}')
            else:
                continue








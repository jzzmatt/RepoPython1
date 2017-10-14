'''
PASSWORD STORAGE
Create an Account (Username, Password)
ForgetPassword, Enter 3 Answer to 3 Question for Password Recovery
Encrypted the plain text password and Store it
Recovery an Account password 


'''
import re
import hashlib

class Account(object):
    dbaccount = {}

    def __init__(self, username, password):
        self._credential = {}
        self.username = username
        self.password = HashPassword(self.account_verification(password)).get_hash
        self._credential[self.username] = self.password #Setup the Object Dict
        Account.set_dbaccount(self._credential)  #Setup a Gloab Object Dict


    def get_account(self):
        return self._credential

    def set_account(self, username, newpassword):
        if username in self._credential and self.account_verification(newpassword):
            self._credential[username]= HashPassword(self.account_verification(newpassword)).get_hash

        else:
            raise ValueError("This username {} doesnt' exit".format(username))

    @classmethod
    def show_dbaccount(cls):
        return cls.dbaccount

    @classmethod
    def set_dbaccount(cls, value):
        account = value
        cls.dbaccount.update(account)

    @staticmethod
    def account_verification(userpassword):
        if PasswordValidation(userpassword).pass_all_scan():
            return userpassword
        else:
            raise ValueError("Your Password doesn't meet complexity Requirement")


class PasswordValidation():

    def __init__(self, password):
        self._password = password

    def check_length(self):
        return len(self._password) >= 6


    def check_Number(self):
        if re.search('[0-9]', self._password) != None:
            return True
        return False


    def check_espcial_char(self):
            if re.search('[$#@]', self._password) != None:
                return True
            return False

    def pass_all_scan(self):
        if self.check_length() and self.check_Number() and self.check_espcial_char():
            return True
        return False


class HashPassword():
    def __init__(self, password):
        self._password = password

    @property
    def get_hash(self):
        _hashing_passwd = hashlib.sha1(str.encode(self._password)).hexdigest()
        return _hashing_passwd



osvald = Account("Osvald", "password##200")
print(osvald.get_account())
junior = Account("Junior","raro2099$")
print(junior.get_account())
junior.set_account("Junior", "Nova2010$$")
print(junior.get_account())
osvald.set_account("Osvald", "##$$0ab")
print(osvald.get_account())
print(Account.show_dbaccount())
#print(osvald.get_account())
#print(osvald.show_dbaccount())






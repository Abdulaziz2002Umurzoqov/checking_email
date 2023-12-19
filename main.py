import re

namuna = re.compile("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")
class UserProfile:

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not namuna.fullmatch(value):
            raise ValueError("Error email address.")
        self._email = value


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("The age is incorrect.Make sure that is available")
        self._age = value



user1 = UserProfile('Anvarbek', 'anvar@gmail.com', 25)
print(user1.email)
print(user1.age)

class Employee:

    company = 'ABC'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 15:
            raise ValueError('Name should be less than 15 chars')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, qiymat):
        if qiymat < 0 or qiymat > 18:
            raise ValueError("Age should be up than 18")
        self._age = qiymat

# attribute
# method
# property

emp1 = Employee('Salom', 22)
print(emp1.name, emp1.age)
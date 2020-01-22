# Property Decorators - Getters, Setters and Deleters
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Deleted name!')
        self.first = None
        self.last = None


emp1 = Employee('Humayun', 'Kabir')
emp2 = Employee('Test', 'User')

emp1.first = 'Mark'
emp1.fullname = 'Jack Jones'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname
print(emp1.fullname)

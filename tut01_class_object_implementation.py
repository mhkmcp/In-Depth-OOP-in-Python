# class object implementation
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'


emp1 = Employee('Humayun', 'Kabir', 50000)
emp2 = Employee('Test', 'User', 45000)

print(emp1.fullname())
print(Employee.fullname(emp2))

print(emp1.email)
print(emp2.email)

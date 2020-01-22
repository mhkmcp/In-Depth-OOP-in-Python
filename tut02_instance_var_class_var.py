# instance variable & class variable
class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp1 = Employee('Humayun', 'Kabir', 50000)
emp2 = Employee('Test', 'User', 45000)

print(emp1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print()

emp1.raise_amount = 1.06

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print()

print(Employee.num_of_emps)





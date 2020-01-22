# instance method, class method, static method
import datetime


class Employee:

    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Humayun', 'Kabir', 50000)
emp2 = Employee('Test', 'User', 45000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print()

emp_str_3 = 'Jhon-Smith-65000'
emp3 = Employee.from_string(emp_str_3)
print(emp3.email)
print(emp3.pay)
print()
print(Employee.num_of_emp)
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))





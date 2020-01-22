# inheritance: subclass, superclass
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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev1 = Developer('Humayun', 'Kabir', 50000, 'Python')
dev2 = Developer('Test', 'User', 45000, 'Java')

mgr1 = Manager('Sue', 'Smith', 85000, [dev1])

print(dev1.email)
print(dev2.pro_lang)
print()

# print(help(Developer))

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
print()

print(mgr1.email)
mgr1.add_emp(dev2)
mgr1.remove_emp(dev2)
mgr1.print_emps()

print(isinstance(dev1, Employee))
print(isinstance(dev1, Developer))
print(isinstance(mgr1, Developer))
print()
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))



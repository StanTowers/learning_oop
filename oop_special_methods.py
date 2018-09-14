class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        pass

    def __str__(self):
        pass

emp_1 = Employee("Corey", "Schaefer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1)
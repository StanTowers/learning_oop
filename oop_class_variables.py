# Python Object-Oriented Programming


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# 2nd Tutorial: Class Variables
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Corey", "Schaefer", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_1.raise_amount = 1.05
emp_1.apply_raise()
emp_2.apply_raise()

print(Employee.num_of_emps)
print(emp_1.pay)
print(emp_2.pay)

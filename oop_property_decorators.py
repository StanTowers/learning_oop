class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee('Coolio', 'McMaster')

print(emp_1.email)
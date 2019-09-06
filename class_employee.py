# Python object oriented programming.

class employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = last + "." + first + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last)


emp_1 = employee("abhilash", "neerati", "50000")
emp_2 = employee("test", "user", "60000")


# print(emp_1)
# print(emp_2)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())




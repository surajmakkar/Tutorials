import math


class FirstClass:
    def setdata(self, value):
        self.data=value
    def display(self):
        print(self.data)
x=FirstClass()
y=FirstClass()

x.setdata("king aurthur")
y.setdata("3.1419")
x.display()
y.display()
class SecondClass(FirstClass):
    def display(self):
        print('current value="%s"'%self.data)
z=SecondClass()
z.setdata(42)
z.display()
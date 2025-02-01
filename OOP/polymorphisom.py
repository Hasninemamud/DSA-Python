#Method Overriding
class Car:
    def intro(self):
        return "BMW is a name of a car brand"
class Honda(Car):
    def intro(self):
        return "BMW is a name of a bike brand"
f = Honda()
# print(f.intro())


#Method Overloading

class Calculator:
    def sum(self, a, b=10):
        return a + b
obj1 = Calculator()
# print(obj1.sum(5))

class Calculator2:
    def sum(self, *args):
        return sum(args)
obj2 = Calculator2()
print(obj2.sum(5))
print(obj2.sum(5, 5))
print(obj2.sum(5, 5, 5))
print(obj2.sum(5, 5, 5, 5))
print(obj2.sum(5, 5, 5, 5, 5))
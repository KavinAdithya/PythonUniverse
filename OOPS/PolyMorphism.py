class A:
    def feature(self):
        print('In Class A feature')

class B(A):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def feature(self):
        print('In Class B feature')
    def add(self, a, b, c = 0):
        return a + b + c
    def __add__(self, other):
        return (self.a - other.a) + (self.b - other.b)

# a = A()
# a.feature()

b = B(2, 3)
b1 = B(1, 2)
print(b + b1)
# b.feature()
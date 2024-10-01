class A:
    def __init__(self):
        self.a = 21
        super().__init__()
        print('A Initialization', self.a)
    def feature1(self):
        print('In Class A feature 1')
    def feature2(self):
        print('In Class A feature 2')

class B(A):
    def __init__(self):
        super().__init__()
        self.a = 20
        print('B Initialization', super().a)
    def feature3(self):
        print('In Class B feature 3')
    def feature4(self):
        print('In Class B feature 4')

class C(A):
    def __init__(self):
        self.a = 5
        super().__init__()
        print('C Initialization',super().a)
    def feature5(self):
        print('In Class C feature 5')
    def feature4(self):
        print('In Class C feature 6')

class D(B, C):
    def __init__(self):
        self.a = 10
        super().__init__()
        print('D initialization', super().a)
b = D()



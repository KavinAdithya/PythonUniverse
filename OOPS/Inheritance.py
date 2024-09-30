class A:
    def __init__(self):
        print('A Initialization')
    def feature1(self):
        print('In Class A feature 1')
    def feature2(self):
        print('In Class A feature 2')

class B(A):
    def __init__(self):
        super().__init__()
        print('B Initialization')
    def feature3(self):
        print('In Class B feature 3')
    def feature4(self):
        print('In Class B feature 4')

class C(B):
    def __init__(self):
        super().__init__()
        print('C Initialization')
    def feature5(self):
        print('In Class C feature 5')
    def feature4(self):
        print('In Class C feature 6')
b = C()

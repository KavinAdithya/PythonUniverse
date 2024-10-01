class A:
    def __init__(self):
        self.name = 'Kavin'
        print('A Constructor')

class B(A):
    def __init__(self):
        super().__init__()
        self.name = 'KavinAdithya'
        print('B Constructor')

    def printNames(self):
        print(super().name , '', self.name)

b =  B()
b.printNames()




class Student:
    def __init__(self, name, age, register_number):
        self.name = name
        self.age = age
        self.register_number = register_number
        self.lap1 = self.Laptop('Apple','i7', 32)

    def show(self, lap):
        print('Name : ', self.name)
        print('Age : ', self.age)
        print('Register Number : ', self.register_number)
        self.lap1.show()
        lap.show()

    class Laptop:
        def __init__(self, name, process, ram):
            self.name = name
            self.process = process
            self.ram = ram

        def show(self):
            print('Name : ' , self.name)
            print('Processor', self.process)
            print('Ram : ', self.ram)


student = Student('Kavin', 20, 710722104043)
laptop = student.Laptop('Techno', 'i5', 16)

student.show(laptop)
# laptop.show()
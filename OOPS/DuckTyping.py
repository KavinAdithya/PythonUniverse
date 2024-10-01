class Dog:
    def bark(self):
        print('Dog is Barking')
class Human:
    def bark(self):
        print('Human is Shouting')

def action(act):
    act.bark()

action(Dog())
action(Human())
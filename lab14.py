
class Dog:
    name = ''
    tricks = []

    def __init__(self, name):
        self.name = name
        print("New dog's name is " + self.name)

    def updateTricks(self, tricks):
        self.tricks.append(tricks)
        print("Tricks: " + str(self.tricks))


dog = Dog('Toby')
dog.updateTricks('catch')
dog.updateTricks('spin')
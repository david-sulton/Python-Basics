class Animal:
    sound = ''
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Pig(Animal):
    sound = 'oink'

class Cow(Animal):
    sound = 'Mooo'

cow = Cow('Mary')
pig = Pig('Agus')

cow.speak()
pig.speak()

class Clothing:
    material = ""
    def __init__(self, name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name ,self.material))

class Shirt(Clothing):
    material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
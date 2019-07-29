class Pokemon(object):
    #constructor
    def __init__(self, name, type, sex):
        self.name = name
        self.type = type
        self.sex = sex

    def attack(self, move):
        print('my name is ' + self.name + ' and I choose ' + move)


class Pikachu(Pokemon):
    def __init__(self, name, type, sex, voltage, current):
        super(Pokemon, self).__init__(name, type, sex)
        self.voltage = voltage
        self.current = current


class Charizard(Pokemon):
    #constructor
    def __init__ (self, name, type, sex, tailFlame):
        Pokemon.__init__(self,name,type,sex)
        self.tailFlame = tailFlame
    def burnGuy(self):
        print('*flames*')

Charizard = Charizard('charry', 'fire/fly', 'Male', 'large')

print(Charizard.attack('burn'))
print(Charizard.burnGuy())

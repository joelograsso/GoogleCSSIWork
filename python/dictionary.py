#  state1 = "New York"
# abbr1 = 'NY'
#  state2 = 'California'
#  abbr2 = 'CA'
#
# print(abbr2 + ' is short for ' + state2)
#
# states = ['CA = California', 'NY = New York']
# stateAbbr = ['CA', 'NY']
# states = ['California', 'New York']
# for index in range(len(states)):
#     print(stateAbbr[index] + ' is short for ' + states[index])



#key and value; keys unlock values
states = {
    'NY': 'New York',
    'MI': 'Michigan',
    'FL': 'Florida'
}

pet = {
    'name': 'Skeemer',
    'animal': 'dog',
    'breed': 'bichon frise',
    'age': 16
}
#store dictionary in array
pets = [
    pet,
    {
    'name': 'Michael',
    'age': 5
    }
]
# print(pets)

#modify
print(pet['name'] + ' is no longer')
pet['name'] = 'Simba'
print(pet['name'] + ' is what he shall be known as')

#add
pet['favorite'] = 'milkbone'
print(pet['favorite'])

#removes
print(pet)
pet.pop('age')
print(pet)



# print(states['MI'])
# print(states)

#gives only keys in loops
for state in states:
    print('key is ' + state)
    print('Value is ' +states[state])

life = {
    'name': 'Joe',
    'age': 16,
    'movies': {
        'name': "Avenger's End Game",
        'rating': 'PG-13',
    }
}


# for key in life:
    print('key is ' + key)
    print('value is ' + str(life[key]))


###############################################################################

class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('Bark Bark Bark')
myPet = Pet('Doge', 12)
myPet.bark()

# print('my new pet is ' + myPet.name + ' and he is ' + str(myPet.age))

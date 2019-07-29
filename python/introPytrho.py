#keep imports at top
import random


#create variables
michaelB = 15
kevTeach = 27

#if else conditions
if michaelB > kevTeach:
    print("michaelB wins")
elif michaelB == kevTeach:
    print ("they bothe great")
else
    print ("kev wins")

#for loops   str == string. turns num into string **** not including 21 ****
print("how many tacos can i buy?")
for numTacos in range(1, 21):
    print(str(numTacos)) + "tacos"

# functions
def createRapName(first, last):
    return 'lil ' + first + ' the ' + last

rapName1 = createRapName('Joe', "LoGrasso")

#array
otherNickname = ['Jman', 'J', 'J logs']
for index in range(len(otherNickname)):
    print('joe aka ' + otherNickname[index])

#while loop -----> will stop on 'stop'
name = raw_input("name")
while name =! "stop":
    name = raw_input("gimme name")
#infinite loop. break moves to next line
while True:
    name = raw_input('gimmr name')
    if name == 'stop':
        break
    print('name is ' + name)

#random numbers
print(random.randint(1, 10))

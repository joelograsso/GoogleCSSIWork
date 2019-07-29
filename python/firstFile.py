# firstName = raw_input('first name? ')
# number = raw_input('number ')
#
# print('lil ' + firstName + ' from the ' + number)


# ageString = raw_input('what is your age ')
# age = int(ageString)
#
# if age < 18:
#     print("you can't vote")
# else:
#     print("you can vote")

# num1 = int(raw_input('number 1 '))
# num2 = int(raw_input('number 2 '))
# num3 = int(raw_input('number 3 '))
#
# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)
#
# player1 =raw_input('rock, paper, scissors? ')
# player2 =raw_input('rock, paper, scissors? ')
#
# if player1 == 'rock' and player2 == 'paper':
#     print('player 2 wins')
# elif player1 == 'scissors' and player2 == 'rock':
#     print('player 2 wins')
# elif player1 == 'paper' and player2 == 'scissors':
#     print('player 2 wins')
# elif player1 == 'paper' and player2 == 'paper':
#     print('Tie. Play again')
# elif player1 == 'scissors' and player2 == 'scissors':
#     print('Tie. Play again')
# elif player1 == 'rock' and player2 == 'rock':
#     print('Tie. Play again')
# else:
#     print('player 1 wins')

import random
def drawCard():
    randNum = random.randint(2, 11)
    print("you drew a " + str(randNum))
    return randNum

score = 0
while True:
    choice = raw_input('draw again? ')
    if choice == 'no':
        break
    elif choice == 'yes':
        newCard = drawCard()
        score = score + newCard
        if score > 21:
            print('you lose')
            break
        print('score: ' + str(score))
print('final score: ' + str(score))






#
# hit = raw_input('hit, yes or no? ')
# score = 0
# while hit == 'yes':
#     card = drawCard()
#     score = score + card
#     print('your score is ' + str(score))
#     if score > 21:
#         print('you bust')
#     if score < 21:
#         hit = raw_input('hit, yes or no? ')
#     if hit == 'no':
#         print('your score is ' + str(score))
#         break



















# number = random.randint(1, 10)
# guess = int(raw_input("what number do you guess?"))
# while guess != number:
#     if guess > number:
#         print('lower')
#         guess = int(raw_input("what number do you guess?"))
#     if guess < number:
#         print('higher')
#         guess = int(raw_input("what number do you guess?"))
#     if guess == number:
#         print('Congrats you got it')
#         break

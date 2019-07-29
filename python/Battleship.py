# Simplified Battleship!
import random
import sys

SEA_LENGTH = 20
SHIP_LENGTH = 3
SHIP_COUNT = 3
HASHES_STRING = '#' * (SEA_LENGTH+2)
MAX_RETRIES = 1000

# given an index  checks if indax
def isValidPlacement(sea, index):
    if index < 0 or index > SEA_LENGTH - SHIP_LENGTH:
        return False

    for i in range(SHIP_LENGTH):
        if (sea[index + i] == '*'):
            return False
    return True


def generateShipPlacements(sea_length, ship_length, ship_count):
  # FYI: lines 9-11 can be shortened to a 'list comprehension' via
  # array = [0 for i in range(sea_length)]
  # but we haven't covered this shorthand :)
  sea = []
  for i in range(sea_length):
    sea.append('0')

  # now that we have our sea, let's fill it with a ship
  count = 0
  retries = 0
  while count < SHIP_COUNT and retries < MAX_RETRIES:
      rand_index = random.randint(0, len(sea) - SHIP_LENGTH)
      if isValidPlacement(sea, rand_index):
          count += 1
          for i in range(SHIP_LENGTH):
              sea[rand_index + i] = '*'
      else:
          retries += 1
  return sea

def printSea(sea):
    print(HASHES_STRING)
    sys.stdout.write('#')
    for i in sea:
        sys.stdout.write(i)
    print '#'
    print(HASHES_STRING)

'''
Battleship is a game where you attempt to discover your opponent's ship locations in a hidden sea.

The player has a matching 'sea' where they can track previous attempts to discover a ship.

If a player successfully guesses the location of a ship, the opponent must tell them so that the player can use that information to guess future shots. This is what the player 'sea' board is for.

Objective:
 Continually ask the user to shoot a slot with a missile
 If it is a hit, mark that index in 'player_sea' with a *
 If it is a miss, mark that index in the 'player_sea' with a X so they know not to shoot there again!
 End the game when all 'ships' have been 'sunk' (when all '*'s in the player_sea board map to the '*'s in the 'opponent_sea')
 After each choice, you should reprint the player_sea array using printSea function defined above

 STRETCH: Implement the computer AI to take its turn after each choice you make and see who wins.
'''
#1 make a function that presents user with input prompts
#2 ask user what index to shoot Continually
#2b ability for user to quit or forfeit game from #1
#3 write function that checks if a choice is a hit in opponent_sea
#4 print current state of sea before user raw_input
#5 if function from num3 turns false, mark player sea with # # XXX:
#6 if function from #3 returns true, mark with a *
#7 write function to check if player's sea has hit all of the ships in the opponent_sea


########################################
#      YOUR CODE BELOW THIS LINE       #
########################################

# this represents the 'hidden' board that you are attempting to shoot
opponent_sea = generateShipPlacements(SEA_LENGTH, SHIP_LENGTH, SHIP_COUNT)

# this represents the players board which tracks where you
# have previously attempted to shoot
player_sea = ['-' for i in range(SEA_LENGTH)]

def shotLocation():
    shootIndex = raw_input('what index would you like to shoot or type exit to leave. ')
    if shootIndex == 'exit':
        exit()
    else:
        shootIndex = int(shootIndex)
    return shootIndex

def hit(index, hit_count):
    if "*" in opponent_sea[index]:
        print('hit')
        player_sea[index] = '*'
        hit_count = hit_count + 1
    return hit_count

def miss(index):
    if "0" in opponent_sea[index]:
        print('miss')
        player_sea[index] = 'X'

hitCount = 0
while True:
    printSea(player_sea)
    index = shotLocation()
    hitCount = hit(index, hitCount)
    miss(index)
    if hitCount == 9:
        print('GAME OVER')
        break

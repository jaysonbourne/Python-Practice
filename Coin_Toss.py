print("Terminator would never happen.")

import random
import math

# def CoinToss():
#     for x in range(0,count):
#         if x%2 == 0:
#             print ("Heads")
#         else:
#             print ("Tails")
# CoinToss()

def CoinToss():
    H = 0
    T = 0
    for x in range(0,10):
        chance = round(random.random())
        if chance == 0:
            T += 1
            toss = "Tails"
        else:
            H += 1
            toss = "Heads"
        print("Tossing a coin... It's a {}! Got {} heads and {} tails thus far".format(toss, str(H), str(T)))
    print ("After {} tosses you got {} heads and {} tails".format(str(x+1), str(H), str(T)))
CoinToss()

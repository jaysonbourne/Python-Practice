print ("hello world.")
import random
import math

# def ScoresGrades():
#     for x in range(0,100):
#         if x >= 90:
#             print({} and "You're grade is an A")
#         else:
#             print("Nothing.")
#
# ScoresGrades()
def ScoresGrades():
    for x in range(0,10):
        grade = ""
        scores = math.floor((random.random()*40)+60)
        if scores >= 95:
            grade = "A+"
        elif scores >= 90:
            grade = "A-"
        elif scores >= 85:
            grade = "B+"
        elif scores >= 80:
            grade = "B-"
        elif scores >= 75:
            grade = "C+"
        elif scores >= 70:
            grade = "C-"
        elif scores >= 65:
            grade = "D+"
        elif scores >= 60:
            grade = "D"
        else:
             grade = "F"
        print("Score is {}; Your grade is {}".format(str(scores), grade))
ScoresGrades()

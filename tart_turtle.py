print ("hello world.")

import turtle, random
from turtle import *
color('red', 'purple')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
# DIST = 100
# for x in range(0,6):
#     print ("x", x)
#     for y in range(1,5):
#         print ("y", y)
#         # turn the pointer 90 degrees to the right
#         turtle.right(90)
#         # advance according to set distance
#         turtle.forward(DIST)
#     # add to set distance
#     DIST += 20

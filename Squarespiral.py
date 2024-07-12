from turtle import *
speed(-1000)
def draw(x):
    right(10)
    for i in range(4):
        forward(x)
        right(90)
        forward(x)
x = 100
for j in range(10):
    for k in range(36):
        draw(x)
    x -= 10

done()
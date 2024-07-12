from turtle import *
bgcolor('black')
speed(5)
setposition(0,0)
setheading(90)
for i in range(1,7):
    down()
    color('pink')
    width(3)
    for x in range(6):
        fd(150)
        rt(60)
    rt(60)

done()
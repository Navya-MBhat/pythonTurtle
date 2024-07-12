from turtle import *
speed(100)
bgcolor('black')
colors = ['red', 'dark red']
for i in range(400):
    forward(i+1)
    right(89)
    pencolor(colors[i%2])
done()
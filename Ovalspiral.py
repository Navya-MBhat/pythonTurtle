from turtle import *
import colorsys
tracer(3)
h = 0.7
bgcolor('black')
pensize(2.5)
for i in range(190):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.003
    circle(190-i,90)
    lt(90)
    lt(20)
    circle(190-i,90)
    lt(18)
done()
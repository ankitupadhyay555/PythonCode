from turtle import *
import tkinter as TK

color('green')
bgcolor('black')
speed(10)
hideturtle()

b = 0
while b < 200:
    right(b)
    forward(b*3)
    b = b+1


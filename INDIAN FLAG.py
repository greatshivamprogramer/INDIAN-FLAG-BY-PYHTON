import turtle  
from turtle import *  
  
screen = turtle.Screen()  
# Defining a turtle Instance  
t = turtle.Turtle()  
speed(200)  
# Orange Rectangle  
#white rectangle  
 
# initially penup()  
t.penup()  
t.goto(-400,250)  
t.pendown()  

t.color("orange")  
t.begin_fill()  
t.forward(800)  
t.right(90)  
t.forward(167)  
t.right(90)  
t.forward(800)  
t.end_fill()  
t.left(90)  
t.forward(167)  

# Draw Green Rectangle  
 
t.color("green")  
t.begin_fill()  
t.forward(167)  
t.left(90)  
t.forward(800)  
t.left(90)  
t.forward(167)  
t.end_fill()  
  
# Big Blue Circle  

t.penup()  
t.goto(70, 0)  
t.pendown()  
t.color("navy")  
t.begin_fill()  
t.circle(70)  
t.end_fill()  
  
# Big White Circle  

t.penup()  
t.goto(60, 0)  
t.pendown()  
t.color("white")  
t.begin_fill()  
t.circle(60)  
t.end_fill()  

#Mini Blue Circles of Flag  

t.penup()  
t.goto(-57, -8)  
t.pendown()  
t.color("navy")  
for i in range(24):  
    t.begin_fill()  
    t.circle(3)  
    t.end_fill()  
    t.penup()  
    t.forward(15)  
    t.right(15)  
    t.pendown()  
  
# Small Blue Circle  

t.color("navy")  
t.penup()  
t.goto(10, 0)
t.pendown()  
t.begin_fill()  
t.circle(10)  
t.end_fill()  
  
#The spokes of India Flag  

t.penup()  
t.goto(0, 0)  
t.pendown()  
t.pensize(1)  
for i in range(24):  
    t.forward(60)  
    t.backward(60)  
    t.left(15)  


  
turtle.done()  
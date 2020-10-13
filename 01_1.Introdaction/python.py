print("Hello World\\")
print("\"Hello World\"")
print("\'Hello World\'")
print("Hello World")

import datetime
print(datetime.datetime.now())

print("Hello")
print("World")
print("Hello\nWorld")
print("Hello", "World")
print("Hello" + "World")
#end = ' ' - переход на новую строку
print("Hello", end=' ')
print("World")
a = "World"
print("Hello {}".format(a))

a = 1
b = 0
print(f"Pupils = {a} Students={b}")
print("small", "medium", "large")
print("small", "medium", "large", sep="")
print("small", "medium", "large", sep=", ")
name = input("Your name: ")
print("Hello, " + name)


a = 8
b = 2
print(a+b)

# comments
'''
comments
comments
comments
'''
a = 8
b = 0.8
c = "string"
d = True

a = "Happy"
b = " New Year"
print(a + b)
'''
a = "Happy New Year"
b = 2020
print(a + b)
'''

import turtle
window = turtle.Screen()
turtle.Pen()
turtle.shape("turtle")
window.exitonclick()

import turtle
window = turtle.Screen()
turtle.reset()
turtle.shape("turtle")
turtle.bgcolor("red")
turtle.color("white")
turtle.speed(2)
turtle.pensize(3)
turtle.forward(150)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(75)
window.exitonclick()

import turtle
window = turtle.Screen()
turtle.reset()
turtle.shape("turtle")
turtle.bgcolor("white")
turtle.color("red")
turtle.speed(2)
turtle.pensize(3)
turtle.circle(80)
turtle.penup()
turtle.forward(80)
turtle.pendown()

turtle.circle(80)
turtle.penup()
turtle.forward(80)
turtle.pendown()
turtle.circle(80)
window.exitonclick()
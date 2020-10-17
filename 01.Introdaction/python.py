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
#etnring info
name = input("Your name: ")
print("Hello, " + name)


a = 8
b = 2
print(a+b)
print(a/b)
print(a*b)
print(a**b)
print(a//b)
print(a%b)


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

print("Hello world") #string
print(2 + 5 )        #number
print(10 - 2)
print(8/2)
print(8*2)
print(2**2)         #cтепінь
print(25//5)        #ділення 
print(25%5)         #остача від ділення
print("Hello world")

name = input("What is your namegg?")
print("Hello", name)

#Типи даних
test = 12
print(test)
test = "string"
print(test)

num_1 = int(input("Enter first num:"))
num_2 = float(input("Enter second num:"))
res = num_1 + num_2
print("Res = ", res)
res += 5
print("Res = ", res)
res *= 5
print("Res = ", res)
res -= 5
print("Res = ", res)
res /= 5
print("Res = ", res)
del res #delete number


#turtle graphics
import turtle
window = turtle.Screen()  #create window
turtle.Pen()              #pen
turtle.shape("turtle")    #body - "arrow", "circle", "square", "triangle", "classic"
window.exitonclick()      #close window after click

import turtle
window = turtle.Screen()
turtle.reset()           #clean screen
turtle.shape("turtle")
turtle.bgcolor("red")    #background color
turtle.color("white")    #line color
turtle.speed(2)          #speed move
turtle.pensize(3)        #thick line
turtle.forward(150)      #lenght line - moving turtle toward / back moving 
turtle.left(90)  
turtle.forward(75)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(75)
window.exitonclick()
#draw circle
import turtle
window = turtle.Screen()
turtle.reset()
turtle.shape("turtle")
turtle.bgcolor("white")
turtle.color("red")
turtle.speed(2)
turtle.pensize(3)
turtle.circle(80)
turtle.penup()     #поднять перо
turtle.forward(80)
turtle.pendown()   #опустить перо

turtle.circle(80)
turtle.penup()
turtle.forward(80)
turtle.pendown()
turtle.circle(80)
window.exitonclick()
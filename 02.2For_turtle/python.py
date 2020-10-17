#dunamic type
a = 8
b = 0.8
c = "string"
d = True
print(type(a), type(b), type(c), type(d))

#<class 'int'> (-765, 0, 20)
# <class 'float'> для чисел с плавающей запятой (-15.0, 0.1, 225.5)
# <class 'str'>строка ("Tom", "Hello World")
# <class 'bool'>(True/False)

import turtle
window = turtle.Screen()
turtle.reset()

turtle.shape("turtle")
turtle.bgcolor("dark slate gray")
turtle.color("alice blue")
turtle.speed(2)
turtle.pensize(3)
turtle.left(20)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.left(20)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.left(20)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
window.exitonclick()

####example 2
import turtle
window = turtle.Screen()
turtle.reset()
turtle.shape("turtle")
turtle.bgcolor("dark slate gray")
turtle.color("alice blue")
turtle.speed(4)
turtle.pensize(3)
for i in 1,2,3,4,5,6:
    turtle.left(30)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
window.exitonclick()

#use range
for i in range(10, 0, -1):
    print(i)

import turtle
window = turtle.Screen()
turtle.reset()
turtle.shape("turtle")
turtle.bgcolor("dark slate gray")
turtle.color("alice blue")
turtle.speed(4)
turtle.pensize(3)   
for i in range(12):
    turtle.left(30)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
window.exitonclick() 

#circle
import turtle
window = turtle.Screen()
turtle.reset()
turtle.shape("turtle")
turtle.bgcolor("black")
turtle.pencolor("purple")

turtle.speed(10)
turtle.pensize(2)
for i in range(30):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)
turtle.exitonclick()

#spirale
import turtle
window = turtle.Screen()
turtle.reset()
turtle.shape("turtle")
turtle.bgcolor("black")
turtle.pencolor("yellow")
turtle.speed(10)
turtle.pensize(2)
for i in range(360):
    turtle.pensize(i/100 + 1)
    turtle.forward(i)
    turtle.left(59)
turtle.exitonclick()


# if - else
a = 5
b = 6
if (a < b):
    print("a severely b")
else:
    print("a strictly b")

time = input("Enter the time: ")
if time < 12:
    print("The first half of the day!")
else:
    print("Afternoon!")    

import math
print(math.ceil(2.5)) # ceil(2.5) ≈ 3
print(math.floor(2.5)) # floor(2.5) ≈ 2
print(math.pow(2, 4)) # pow(2, 4) =2*2*2*2 = 16.0
print(math.sqrt(16)) # sqrt(16) = 4*4 = 4.0    

import random
print(random.random()) # 0.4956579385740163
print(random.randint(0, 1)) # 0
print(random.randint(1, 100)) # 66
print(random.randint(10, 20)) # 16
#Sum
a = 2
a += 1 # a = a+1
print(a)
#Minus
a = 2
a -= 1 # a = a-1
print(a)

import math
a = 2
a = math.pow(a, 2) # a = a**2
print(a)
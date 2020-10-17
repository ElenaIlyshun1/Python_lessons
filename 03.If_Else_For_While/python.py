a = 5
b = 2
if (a < b):
    print("a < b")
else:
     print("a > b")   

time = int(input("Enter time of day: "))
if time < 12:
      print("The first half of day")
else:
    print("Afternoon!")            

import random
print(random.random())  
print (random.randint(5,80))  

import math
print(math.ceil(2.5))  # =3
print(math.floor(2.5))  # =2
print(math.pow(2,4))  # =2*2*2*2 піднесення до степеня
print(math.sqrt(16))  # =4*4 корінь квадратний
#while
str1 = "+"
i = 0
while i < 10:
    print(str1)
    i = i + 1



i = 0
while (i<=20):
    if (i%2==0):
        print (i)  
    i = i + 1

#month
i= 0
while (i <= 12):
    month = int(input("Enter number of month: "))   
    if (month == 1):
        print("January")
    elif (month == 2):
        print("February")
    elif (month == 3):
        print("March")
    elif (month == 4):
        print("April")
    elif (month == 5):
        print("May")
    elif (month == 6):
        print("June")
    elif (month == 7):
        print("Julay")
    else:
        print("There isn't this momth")
    i = i + 1  

a = int(input())
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
    a = int(input())
else:
    print('Ни одного отрицательного числа не встретилось')

n = int(input())
for i in range(n):
    a = int(input())
    if a < 0:
        print('Встретилось отрицательное число', a)
        break    
else:
    print('Ни одного отрицательного числа не встретилось')

for c in range (random.random(10,50)):
    print (c)

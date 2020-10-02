# num1 = 21
# str = "Hello"
# num2 = float(input("Enter num 2"))
# num3 = str(input("Enter num 2"))
# num4 = int(input("Enter num 2"))
# res = int(num1 + num2)
# print("Res = ", res)
# #del res
# res += 5
# print (res)
# res -=9
# print (res)
# res *=10
# print (res)
# res/=2
# print (res)

#списки
l = []
lis = [1,56,'x', 2.56, "Thanks", ['s', 't', 'r','o','k','a']]
print(lis)

s = "Красива осінь вишиває клени "
print (s)
s = "Красива осінь вишиває клени\nЧервоним, жовтим, срібним, золотим.\nА листя просить: – Виший нас зеленим!\nМи ще побудем, ще не облетим."
print (s)
#n - перенос на інший рядок
#t - табуляціяб тобто відступ
print("Start:\n\tstring\n\tstring\n\tstring\nEnd")
#Конкатенація - обєднання строк
s1 = "Hello"
s2 = "World"
print(s1+s2)
#дублювання строки
s3 = "Hello"
print(s1*3)
#string lenght
print(len(s3)) 
#индексация
s = "Hello world"
print("symbol[0]: " + str(s[0]))
print("symbol[6]: " + str(s[6]))
i = len(s)
print (i)
#print(s[i]) - error

#Method
invitation = "heLLo WoRLd "
print(invitation.capitalize())#перший сомвол велика буква всі інші малі
print(invitation.title())#слова починаються з великої букви
print(invitation.upper())#верхній регістр
print(invitation.lower())#нижній регістр

#find and refind
#find шукає зліва направо
s = "message"
print(s.index("m"))
print(s.find("m"))
print(s.find("s"))
print(s.find("e"))
print(s.find("x"))
#rfind шукає зправа наліво
s = "message"
print(s.rfind("m"))
print(s.rfind("s"))
print(s.rfind("e"))
print(s.rfind("x"))
#method replace(old,new,num)
s = "best regards best"
print(s.replace("best","kind"))
print(s.replace("best","kind",1))


#count
s = "Hello world"
print(s.count("l"))
print(s.count("o",5))

password = "Qwerty123@"
print("\nTry isalpha:")
for symbol in password:
    alpha = symbol.isalpha()
    print(f"{symbol} - {alpha}")
    if(not alpha) and (symbol == "@"):
        print(f"It is {symbol}")

#slice
s = "message"
print(s[0:]) 
print(s[2:5]) 
print(s[2:-1]) 
print(s[1:5:2]) 
print(s[:5])  
print(s[:3] + "www" + s[3:])   
print(s[:2] + "www" + s[3:])    #change letter

import random
s1 = "ABCDEFGHIJKLMNOPQRSTUW"
s2 = "1234567890"
s3 = "][{}+=:;>,.&^%$#@!"
s = s1.upper() + s1.lower() + s2 + s3
password  = ""
for i in range(15):
    p = random.choice(s)
    print(p, end="")
    password = password + p
print(f"\nNew password [{i}] : {password}")    

#module string
import string
#string.ascii_lowercase + string.ascii_uppercase
s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation
s = s1 + s2 + s3
password  = ""
for i in range(15):
    p = random.choice(s)
    print(p, end="")
    password = password + p
print(f"\nNew password [{i}] : {password}")   
a = ['ass??' , 'ddje???', 'djjskd??kmdckd']
print (a)
for i in a :
    print(i.replace("?", "*"))
#join
t = ['25','15',"36","55"]
print("hello".join(t))    
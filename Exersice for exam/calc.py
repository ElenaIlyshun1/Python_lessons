print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
   print('{} + {} = '.format(number_1, number_2))
   print(number_1 + number_2)

elif operation == '-':
   print('{} - {} = '.format(number_1, number_2))
   print(number_1 - number_2)

elif operation == '*':
   print('{} * {} = '.format(number_1, number_2))
   print(number_1 * number_2)

elif operation == '/':
   print('{} / {} = '.format(number_1, number_2))
   print(number_1 / number_2)

else:
   print('You have not typed a valid operator, please run the program again.')        
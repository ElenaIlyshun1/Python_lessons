#create list
students = []
list1 = [ 1 , 5, 8, 'cool', 'hello', ['s', 'c' ,'h', 'o', 'o','l']]
print(list1)
pupils = ['Lilli', 'Olivia', 'Emily', 'Sophia']
pupils[0] == 'Lilli'
pupils[0] == 'Olivia'
pupils[0] == 'Emily'
pupils[0] == 'Sophia'

pupils[-1] == 'Lilli'
pupils[-2] == 'Olivia'
pupils[-3] == 'Emily'
pupils[-4] == 'Sophia'

student = "Lilli"
print("lenght string = ")
print( len(student))
print("lenght list = ")
print(len(pupils))

#change element in list
shop_list = ['coffe', 'tea', 'sugar', 'chesse', 'juice']
shop_list[2]='milk'
print("New list", shop_list)
list_len = len(shop_list)
print("len list = ", list_len)
index = list_len - 1
print("Last element: ", shop_list[index])

#find element
fruits = ['orange', 'apple', 'banana', 'pineapple', 'coconat','banana']
count = fruits.count('banana')
print(f"There are {count} bananas")

#add element in the end of list
pupils = ['Lilli', 'Olivia', 'Emily', 'Sophia']
pupils.append("Anna")
print(pupils)
#add two list in one
pup = ["Roma", "Oleg"]
pupils.extend(pup)
print(pupils)

#add element by index
pupils = ['Lilli', 'Olivia', 'Emily', 'Sophia']
pupils.insert(1,'Sasha')
pupils.insert(4,"Olya")
print(pupils)
#sort
pupils.sort()
print(pupils)

#delete element by index or last element in  list
pupils = ['Lilli', 'Olivia', 'Emily', 'Sophia']
pupils.pop()
print(pupils)
pupils.pop(1)
print(pupils)

#remove by name: first elemen which find
pupils = ['Lilli', 'Olivia', 'Emily', 'Sophia']
pupils.remove('Lilli')
print(pupils)

#index
print(pupils.index("Olivia"))

pupils.reverse()
print(pupils)
#delete all
pupils.clear()



#game random state
import random
stats = []
attributes = 5
print('Stats: ', end = "")
for i in range(attributes):
    r = random.randint(40,70)
    stats.append(r)
    print(stats[i], '  ', end = '')

print("\n\t[1] - Strenght\
    \n\t[2] - Dexterity\
    \n\t[3] - Intelligence\
    \n\t[4] - Wisdom\
    \n\t[5] - Charisma")

select = int(input("Select :"))
select -=1

stats[select] = stats[select] + random.randint(5,10)

for i in range(len(stats)):
    if i == select:
        continue
    stats[i] = stats[i] - random.randint(5,10)

print("Stats : ", end = "")
for i in range(attributes):
    print(stats[i], end = " ")    

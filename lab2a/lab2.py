import math
print("ЗАВДАННЯ 2і")

print("Перша константа", None)
print("Друга константа", NotImplemented)
print("Третя константа", Ellipsis)


print("ЗАВДАННЯ 2іі")


s = 'Lviv Polytechnic'
d = len(s)
print(d)

numbers = [2, 5, 7, 3, 5]
numbers_sum = sum(numbers)
print(numbers_sum)


print("ЗАВДАННЯ 2ііi")
print("Цикл 1")
i = 10
while i < 20:
    print(i)
    i = i + 3
print("Цикл 2")
for i in '000202031':
    if i == '3':
        break
    print(i)


print("ЗАВДАННЯ 2іv")


try:
    result = math.log(-5)
except ValueError:
    result = "неможливо взяти логарифм з від'ємного числа"
print(result)


print("ЗАВДАННЯ 2v")

with open("README.md", "w") as f:
    f.write("it's a lab 2a")

print("ЗАВДАННЯ 2vi")

add = lambda x, y: x + y
print( add(750, 200))

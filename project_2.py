# Task 1
name = input("Enter your name please: ")
print("Hello," " " + name + "!")
# Task 2
some_var = int(input("Please enter your number: "))
print("Next number for number" " " + str(some_var) + " " "is" " " + str(some_var + 1))
print("Previous number for number" " " + str(some_var) + " " "is" " " + str(some_var - 1))
# Task 3
t = int(input("Please enter time for Vasya: "))
v = int(input("Please enter speed for Vasya: "))
way = int(t * v)
if v > 0:
    print("Вася рухається у позитивному напрямку")
elif v < 0:
    print('Вася рухається у негативному напрямку')
if way < 100:
    print("Вася подолає відстань у кількості  - " + str(way) + "км")
else:
    print("Вкажіть інші вхідні данні швідкості та часу!")
# Task 4
year = (input("Enter number of year please: "))
if int(year) % 4 == 0 and int(year) % 100 != 0:
    print("Високосний")
elif int(year) % 400 == 0:
    print("Високосний")
else:
    print("Не високосний")
# Task 5
x = int(input("Some number:"))
if x > 0:
    print("sign(x) = 1")
elif x < 0:
    print(" sign(x) = -1")
elif x == 0:
    print(" sign(x)")
# Task 6
m = float(input("Please enter your favorite number: "))
my_list = (list(range(10, 101, 10)))
print(abs(m) in my_list)
# Task 7
zirka = int(input("Enter numbers of stars: "))
print("*" * zirka)


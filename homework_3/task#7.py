factorial = int(input("Введіть число: "))
some_number = 1
while factorial > 1:
    some_number *= factorial
    factorial -= 1
print(some_number)
list_of_six = list(element for element in range(100, 197, 6))
for element in list_of_six:
    if element % 5 == 0 and element < 150:
        print(element)

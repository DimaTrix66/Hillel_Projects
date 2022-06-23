g_1 = int(input("Кінь стоїть на горизонталі 1-8: "))
v_1 = int(input("Кінь стоїть на вертикалі  1-8: "))
g = int(input("Введіть горизонталь на якій має стояти від 1-8: "))
v = int(input("Введіть вертикаль на якій має стояти 1-8: "))
# if g_1 - g and v_1-v == abs(1 or 2):
if abs(g_1-g == 1 or 2) and abs(v_1-v == 1 or 2):
    print("Yes")
else:
    print("No")
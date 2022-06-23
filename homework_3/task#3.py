print(list(reversed(range(10, 51, 10))))

#Або таким способом
some_list = list(i for i in range(10, 60, 10))
some_list.reverse()
print(some_list)
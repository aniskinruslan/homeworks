# Найди и замени!
mylist1 = [2, 5, 11, 19, 27, 31, 40, 53, 65, 77, 80, 99]
for item in mylist1:
    print(item)
a = int(input("Введите число на которое хотите заменить "))
mylist1[2] = a
print(mylist1)

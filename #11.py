# Найди и замени!
# Необходимо создать функцию, которая будет генерировать список, выводить его в консоль.
# После чего, просить пользователя ввести число от 0 до максимального значения спика (номера по порядку последнего элемента списка) и заменять этот элемент списка на введеное число.
# Пример:
# Сгенерирован список [1.4.5.84.145.7.5.64.14]
# Введено число 3
# "84" из списка заменяется на "3"
mylist1 = [2, 5, 11, 19, 27, 31, 40, 53, 65, 77, 80, 99]
for item in mylist1:
    print(item)
a = int(input("Введите число на которое хотите заменить "))
mylist1[2]=a
print(mylist1)

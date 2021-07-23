# Hello World
print("Hello World")

# 2

a=5
b=3

c=a+b
d=a-b
e=a*b
f=a/b

print(c,d,e,f)

# Задание 3. Функции
def results(a,b):
    return a+b,a-b,a*b,a/b
print(results(5,3))

# Задание 4. А что, если?
def compare(a,b):
    if a>b: print("A>B")
    if a<b: print("A<B")
    if a==b: print("A=B")
compare(10,5)
compare(5,10)
compare(5,5)

#Задание 5. Списки
my_list = [num * 1 for num in range(0,10)]
print(my_list)

my_list2= [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in my_list2:
    print(item)

my_list3 = list(range(10))
print(my_list3)

# Задание 6. Найди меня!
my_list4=[1,5,7,6,1,10,8,3,9,4]
elem  =  my_list4[3]
print("Число " + str(elem) + " находится в списке под индексом 3")

# Задание 7. Пока не разлучит нас!
a=3
b=10
c=1
while a<b:
    print(str(a) + "<" +str(b))
    a=a+c
print("Ну наконец-то я это сделал!")

#Задание 8. Конкатенация!
word1=input("В задании №8 сказано " )
word2=input("Про ")
print(word1 + " " + word2)

#Задание 10. Посчитай
num = int(input("Введите число: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма элементов числа равна: ",sum)



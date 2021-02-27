import random

print("Задание № 1")
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]
print("ДАНО:", lst)
print("Получено:")
dic = {}
for i in range(len(lst)):
    dic[i] = lst[i]
    i += 1
print("dic =", dic)
print(50 * "-")

print("Задание № 2: УГАДАЙ ЧИСЛО")
n = 0
x = random.randint(1, 20)
while n < 5:
    y = int(input("Попробуйте угадать: "))
    n += 1
    if y < x:
        print("Слишком мало...")
    if y > x:
        print("Слишком много...")
    if y == x:
        break

if y == x:
    print("Класс! Вы угадали число!")
if y != x:
    x = str(x)
    print("Всё! Вы не выиграли. Число равно:", x, "! Игра завершилась.")
print(50 * "-")

print("Задание № 3")
some_string = "Adverts"
print("ДАНО:", some_string)
k = round(len(some_string) / 2)
print("Получено:")
print(some_string[int(k - 2):int(k + 1)])
print(50 * "-")

print("Задание № 4")
first_name = "Aidana"
second_name = "Adilet"
print("ДАНО:", first_name, "и", second_name)
f = 0
mix = []
for f in range(len(first_name)):
    mix.append(first_name[f] + second_name[f])
    f += 1 
output = "".join(mix)
print("Получено:")
print(output)
print(50 * "-")

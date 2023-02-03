# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение.
# Помогите Кате отгадать задуманные Петей числа.
#        Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3
from random import randint as ri
x = ri(1, 10)
y = ri(1, 10)

res1 = x * y
res2 = x + y
x_if = int(input(f'{res1}, {res2}, напишите X: '))
y_if = int(input('напишите Y: '))

if x_if * y_if == res1 and x_if + y_if == res2 :
    print("Всё верно!")
else:
    print(f"Не верно, x = {x}, y = {y}")
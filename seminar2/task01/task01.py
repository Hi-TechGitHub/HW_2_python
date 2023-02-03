from random import randint

count_coins = int(input("Сколько всего монеток?: "))
count_up = 0;
count_down = 0;
for _ in range(1, count_coins + 1):
    coins = randint(0, 1)
    print(f'{coins}')

    if coins == 0:
        count_down += 1

    if coins == 1:
        count_up += 1

if count_down < count_up:
    print(f"Нужно перевернуть {count_down} монеток.")

if count_down > count_up:
    print(f"Нужно перевернуть {count_up} монеток.")
else:
    print("Монетки равны.")

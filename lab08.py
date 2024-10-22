import random

N = int(input("Введіть розмір масиву (N): "))

array = [3**i for i in range(N)]
print("Початковий масив:")
print(array)

random.shuffle(array)
print("Перемішаний масив:")
print(array)

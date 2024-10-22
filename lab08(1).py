line1 = list(map(int, input("Введіть перший рядок чисел (через пробіл): ").split()))
line2 = list(map(int, input("Введіть другий рядок чисел (через пробіл): ").split()))

M = [line1, line2]

P = [sum(column) for column in zip(*M)]

print("\nДвовимірний масив M:")
for row in M:
    print(row)

print("\nМасив P з сумами у стовпчиках:")
print(P)

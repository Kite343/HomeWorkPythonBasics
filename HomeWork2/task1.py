n = input("Введите вещественное число:\n")
sum = 0
for i in n:
    if i.isdigit():
        sum += int(i)
print(sum)

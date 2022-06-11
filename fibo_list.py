n = int(input('Введіть кількість чисел'))
fibo_list = [0, 1]
while len(fibo_list) < n:
    next_value = fibo_list[-1] + fibo_list[-2]
    fibo_list.append(next_value)
print(fibo_list)

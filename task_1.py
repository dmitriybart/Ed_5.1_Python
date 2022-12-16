# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 5 6 7 9

with open('task_1.txt', 'r') as data:
    my_str = data.readline().split()
int_my_str = list(map(int, my_str))
print(int_my_str)
for i in range(1, len(int_my_str)):
    if (int_my_str[i]-1 != int_my_str[i-1]):  
        with open('task_1.txt', 'a') as data_2:
            data_2.write(f'\n{int_my_str[i]-1} ') 

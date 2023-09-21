# дискретная задача о рюкзаке

import random

# Создаёт список элементов: n-количество m-нижний предел k-верхний предел
# Первое число вес, второе стоимость
def Make_list(n, m, k):
    with open('input.txt', 'w+') as f:
        for i in range(n):
            s = str(random.randint(m, k)) + ' ' + str(random.randint(m, k)) + '\n'
            f.write(s)
        f.close()

def Get_arr():
    arr = []
    i = 0
    with open('input.txt', 'r') as f:
        for s in f:
            arr.append([i, int(s.split()[0]), int(s.split()[1])])
            i += 1
    return arr

def sort_key(a):
    return a[2]/a[1]

def Reverse(arr):
    for i in range(int(len(arr)/2)):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr

def Greed_alg(arr, n):
    cost = 0
    final = []
    arr = Reverse(sorted(arr, key=sort_key))
    print(*arr)
    while n > 0:
        if len(arr) > 0:
            if n - arr[0][1] > 0:
                n = n - arr[0][1]
                cost += arr[0][2]
                final.append(arr[0])
            arr.pop(0)
        else:
            break
    return final

def Items_list(n):
    arr = Get_arr()
    total_cost = 0
    total_weight = 0
    res = Greed_alg(arr, n)
    for item in res:
        total_cost += item[2]
        total_weight += item[1]
    print('Взяты вещи:', *res)
    print(f'На сумму {total_cost}, общий вес {total_weight}')


n = 100
Make_list(10, 1, 60)
Items_list(n)
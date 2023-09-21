import random

# Создаёт список элементов: n-количество m-нижний предел k-верхний предел
# Первое число вес, второе стоимость
def make_list(n,m,k):
    f = open('input.txt','w+')
    for i in range(n):
        y = str(random.randint(m,k))
        s = y+' '+ y+'\n'
        f.write(s)
    f.close()
# Считывает из txt массив значений
def txt_read(s):
    s1 = str(s)+'.txt'
    f = open(s1, 'r')
    arr = []
    for line in f:
        arr.append([int(line.split()[0]),int(line.split()[1])])
    return arr

def sort_key(e):
    return e[0]/e[1]

# Таблица значений по весу
def Get_table(arr, A=100):
    # Считывание имеющегося массива
    cost = []
    weight = []
    for i in range(len(arr)):
        cost.append(int(arr[i][1]))
        weight.append(int(arr[i][0]))
    n = len(cost)

    # создаём таблицу из нулевых значений
    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            # базовый случай
            if i == 0 or a == 0:
                V[i][a] = 0
            elif weight[i - 1] <= a:
                V[i][a] = max(cost[i - 1] + V[i - 1][a - weight[i - 1]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]
    #print(V)
    return V, weight, cost


def Get_selected_items_list(arr, A=100):
    V, weight, cost = Get_table(arr)
    n = len(cost)
    res = V[n][A]  # начинаем с последнего элемента таблицы
    a = A  # начальный вес - максимум
    items_list = []  # список веса и ценности

    for i in range(n, 0, -1):  # идём в обратном порядке
        if res <= 0:  # условие прерывания
            break
        if res == V[i - 1][a]:  # ничего не делаем
            continue
        else:
            items_list.append([weight[i - 1], cost[i - 1]])
            res -= cost[i - 1]  # отнимаем значение ценности от общего
            a -= weight[i - 1]  # отнимаем вес от общего

    return items_list

def Pack(arr,N): # макс обьём контейнера
    louse_arr = []
    m_i = 0
    end_arr = []
    print('Начальный массив:', arr)
    for i in arr: # Удаление элементов которые нельзя упаковать
        if i[0] > N:
            louse_arr.append(i)
    for i in louse_arr:
        while i in arr:
            arr.remove(i)
    print('Допустимые элементы:',arr)
    print('Недопустимые элементы:', louse_arr)
    while arr != []:
        end_arr = Get_selected_items_list(arr, N)
        for i in range(len(end_arr)):
            #print(i)
            arr.remove(end_arr[i])
        print('Контейнер ',m_i+1,' - ',end_arr)
        m_i += 1
    return m_i

make_list(20, 1, 100)

arr = txt_read('input')

print(f"Необходимо {Pack(arr, 100)} контейнеров")
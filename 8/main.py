#алгортм дейкстры
import math

def Graf_go():
    N = 0
    with open('input.txt', 'r') as f:
        for s in f:
            N += 1
    arr = []
    with open('input.txt', 'r') as f1:
        for s in f1:
            arr.append(s)
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    return arr

#последовательно находим путь до всех неисследованных вершин
#и фиксируем один наименьший на каждом шаге
#затем сравниваем старое значение с расстоянием из новой фиксированной вершины
#и выбираем наименьшее
#повторяем пока все вершины не исследуются
def Dejkstra(n):
    arr = Graf_go()
    if n > len(arr):
        return ["Ошибка"]
    discovered = []
    paths = [math.inf]*len(arr)
    paths[n] = 0
    while len(discovered) < len(arr):
        min = math.inf
        min_i = 0
        for i in range(len(paths)):
            if i not in discovered:
                if min > paths[i]:
                    min = paths[i]
                    min_i = i
        discovered.append(min_i)
        for i in range(len(arr[min_i])):
            if int(arr[min_i][i]) != 0:
                if i not in discovered:
                    if paths[i] > int(arr[min_i][i]) + paths[min_i]:
                        paths[i] = int(arr[min_i][i]) + paths[min_i]
    return paths

n = int(input("Введите начальную вершину:"))
res = Dejkstra(n)
if res[0] == "Ошибка":
    print(*res)
else:
    print("Расстояния до остальных вершин равны:", *res)
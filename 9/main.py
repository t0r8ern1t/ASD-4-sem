#алгоритм беллманна-форда

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

def Get_edges(arr):
    edges = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if int(arr[i][j]) != 0:
                edges.append([int(arr[i][j]), i, j])
    return edges

#исходя из того что кратчайший путь должен содержать не больше, чем
#n-1 ребер, перебираем все пути, состоящие из одного ребра и выбираем
#кратчайший, затем из двух и так далее до n-1
#сложность о(ve)

def Bellman_ford(n):
    arr = Graf_go()
    edges = Get_edges(arr)
    paths = [math.inf]*len(arr)
    paths[n] = 0
    for i in range(len(arr) - 1):
        for edge in edges:
            if paths[edge[1]] != math.inf and paths[edge[1]] + edge[0] < paths[edge[2]]:
                paths[edge[2]] = paths[edge[1]] + edge[0]
    for edge in edges:
        if paths[edge[1]] != math.inf and paths[edge[1]] + edge[0] < paths[edge[2]]:
            return ["Ошибка"]
    return paths


n = int(input("Введите начальную вершину:"))
res = Bellman_ford(n)
if res[0] == "Ошибка":
    print(*res)
else:
    print("Расстояния до остальных вершин равны:", *res)
#алгоритм прима

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


def Get_min(edges, united):
    min = [math.inf, -1, -1]
    for a in united:
        for edge in edges:
            if (edge[1] == a or edge[2] == a) and (edge[1] not in united or edge[2] not in united):
                if edge[0] < min[0]:
                    min = edge
    return min

def Prim():
    arr = Graf_go()
    edges = Get_edges(arr)
    united = {0}
    tree = []
    while len(united) < len(arr):
        min = Get_min(edges, united)
        if min[1] == -1:
            print('Минимальное остовное дерево не существует')
        else:
            tree.append(min)
            united.add(min[1])
            united.add(min[2])
    return tree


tree = Prim()
weight = 0
for i in tree:
    weight += i[0]
print('Минимальное остовное дерево:', tree)
print('Вес равен', weight)
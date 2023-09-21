#алгоритм крускала

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


def Kruscal():
    arr = Graf_go()
    edges = Get_edges(arr)
    edges = sorted(edges, key=lambda x: x[0])
    united = set() #список соединенных вершин
    groups = {} #словарь с изолированными группами
    tree = []

    #алгоритм: проверяем соединены ли две вершины
    #если обе изолированы, то создаем элемент словаря с обеими вершинами
    #если в словаре нет одной из них то добавляем в список с ключом
    #второй вершины первую или наоборот
    for edge in edges:
        if edge[1] not in united or edge[2] not in united:
            if edge[1] not in united and edge[2] not in united:
                groups[edge[1]] = [edge[1], edge[2]]
                groups[edge[2]] = groups[edge[1]]
            else:
                if not groups.get(edge[1]):
                    groups[edge[2]].append(edge[1])
                    groups[edge[1]] = groups[edge[2]]
                else:
                    groups[edge[1]].append(edge[2])
                    groups[edge[2]] = groups[edge[1]]
            tree.append(edge)
            united.add(edge[1])
            united.add(edge[2])

    #объединяем разные группы вершин
    for edge in edges:
        if edge[2] not in groups[edge[1]]:
            tree.append(edge)
            tmp = groups[edge[1]]
            groups[edge[1]] += groups[edge[2]]
            groups[edge[2]] += tmp
    return tree

tree = Kruscal()
weight = 0
for i in tree:
    weight += i[0]
print('Минимальное оставное дерево:', tree)
print('Вес равен', weight)
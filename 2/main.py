#Заполняем массив по мартице
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


def BFS(a, b):
    arr = Graf_go()
    if (a > len(arr)) or (b > len(arr)):
        return False
    elif a == b:
        return 0
    q = []
    discovered = [a]
    length = [-1]*len(arr)
    length[a] = 0
    for i in range(len(arr[a])):
        if int(arr[a][i]) == 1:
            q.append(i)
            length[i] = length[a]+1
    while q != []:
        k = q.pop(0)
        if k == b:
            discovered.append(k)
            print('Путь найден')
            print('Длина пути:', length[b])
        else:
            if k not in discovered:
                discovered.append(k)
                for i in range(len(arr[k])):
                    if int(arr[k][i]) == 1:
                        if i not in q:
                            q.append(i)
                            if i not in discovered:
                                length[i] = length[k] + 1
    if length[b] == -1:
        print('Между узлами нет связи')


a = int(input('Введите номер первого узла: '))
b = int(input('Введите номер второго узла: '))
BFS(a, b)

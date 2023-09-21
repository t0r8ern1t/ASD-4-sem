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

order = []
arr = Graf_go()
discovered = [False for i in range(len(arr))]

def Invert():
    arr2 = [[0 for j in range(len(arr))] for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '1':
                arr2[j][i] = '1'
    return arr2


def DFS(a):
    discovered[a] = True
    for i in range(len(arr[a])):
        if arr[a][i] == '1':
            if not discovered[i]:
                DFS(i)
    order.append(a)

def DFS2(a):
    arrg = Invert()
    discovered[a] = True
    for i in range(len(arrg[a])):
        #print(a, i, arrg[a][i])
        if arrg[a][i] == '1':
            if not discovered[i]:
                DFS2(i)


k = 0
for i in range(len(arr)):
    if not discovered[i]:
        DFS(i)
discovered = [False for i in range(len(arr))]

order = order[::-1]
for a in order:
    if not discovered[a]:
        DFS2(a)
        k += 1
        component = []
        for i in range(len(discovered)):
            if discovered[i]:
                component.append(i)
        print(f"Компонента {k}:", *component)
print("Всего компонент", k)
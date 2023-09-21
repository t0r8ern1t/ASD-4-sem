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


def DFS(a, discovered):
    arr = Graf_go()
    discovered.append(a)
    for i in range(len(arr[a])):
        if arr[a][i] == '1':
            if i not in discovered:
                DFS(i, discovered)
    return discovered

def Find_Components():
    arr = Graf_go()
    dict = {}
    k = 1
    for i in range(len(arr)):
        dict[i] = 0
    for i in dict.keys():
        if dict[i] == 0:
            component = DFS(i, [])
            for j in component:
                dict[j] = k
            k += 1
    for i in range(1, k):
        c = []
        for j in dict.keys():
            if dict[j] == i:
                c.append(j)
        print("компонента", i)
        print(*c, "\n")

Find_Components()

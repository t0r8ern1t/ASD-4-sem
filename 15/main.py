# задача о раскраске графа

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

def Coloring():
    arr = Graf_go()
    colors = [0]*len(arr) #список цветов вершин

    def Get_neighbors(a):
        taken = []
        for i in range(len(arr[a])):
            if int(arr[a][i]) == 1:
                if colors[i] != 0:
                    taken.append(colors[i])
        return taken

    for a in range(len(arr)):
        taken = Get_neighbors(a)
        color = 1
        while color in taken:
            color += 1
        colors[a] = color

    return colors

arr = Graf_go()
colors = Coloring()
for i in range(len(arr)):
    print(f'Вершина {i}, цвет {colors[i]}')

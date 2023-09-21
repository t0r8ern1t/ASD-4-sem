#------Минимальная выпуклая оболочка (алгоритм Грэхема)-----
#Поворот для точек образующих вогнутый угол
def rotate(A1,A2,A3):
  return (A2[0]-A1[0])*(A3[1]-A2[1])-(A2[1]-A1[1])*(A3[0]-A2[0])
#Алгоритм

def grahamscan(points):
  n = len(points) # число точек
  order = [i for i in range(n)] # список номеров точек
  for i in range(1, n):
    if points[order[i]][0] < points[order[0]][0]: # если i-ая точка лежит левее 0-ой точки
      order[i], order[0] = order[0], order[i] # меняем местами номера этих точек
  for i in range(2, n): # сортировка вставкой
    j = i
    while j > 1 and (rotate(points[order[0]], points[order[j-1]], points[order[j]]) < 0):
      order[j], order[j-1] = order[j-1], order[j]
      j -= 1
  mvo = [order[0], order[1]]
  for i in range(2, n):
    while rotate(points[mvo[-2]], points[mvo[-1]], points[order[i]]) < 0:
      del mvo[-1]
    mvo.append(order[i])
  return mvo


print('Кол-во точек: ')
count = int(input())
print('Введите координаты (х и у в отдельных строках):')
A = [0]*count
for i in range(count):
    A[i]=[0]*2
    a, b = int(input()), int(input())
    A[i][0]=a
    A[i][1]=b

s = grahamscan(A)
for i in s:
  print(f"Точка {i}, координаты: {A[i]}")


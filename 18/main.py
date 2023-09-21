# задача о суммах подмножеств

import random

def Make_list(n, m, k):
    f = open('input.txt','w+')
    for i in range(n):
        d = random.randint(m, k)
        if d == 0:
            d = 1
        s = str(d)+'\n'

        f.write(s)
    f.close()

def Read_file():
    arr = []
    with open("input.txt", "r") as f:
        for line in f:
            arr.append(int(line))
    return arr

def Greed_alg(arr):
    for j in range(len(arr)):
        d = int(arr[j])
        end_arr = []
        end_arr.append(arr[j])
        for i in range(len(arr)):
            if d == 0:
                #print(j,' ',i)
                print('Последовательность найдена!')
                return end_arr
            if abs(d + arr[i]) < abs(d):
                d += arr[i]
                end_arr.append(arr[i])
    print('Последовательность не найдена!')
    return end_arr



#Make_list(100,-50,50)
arr = Read_file()
#print(sorted(arr,key=abs))
print('Последовательность: ', *Greed_alg(arr))
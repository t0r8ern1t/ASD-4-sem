# алгортим кнута-морриса-пратта
# используется когда в строке много повторяющихся символов
# сложность о(n+m)

#префикс-функция
def Prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v



def KMP(str, sub):
    sub_len = len(sub)
    str_len = len(str)
    #print(str_len, sub_len)
    if not str_len or sub_len > str_len:
        return []
    P = Prefix(sub) #префикс-массив для подстроки
    #print(P)
    entries = []
    i = j = 0
    while i < str_len and j < sub_len:
        if str[i] == sub[j]:
            if j == sub_len - 1: #если количество совпавших символов подряд равно длине подстроки
                entries.append(i - sub_len + 2)
                j = 0
            else: #сравниваем пока не дойдем до длины подстроки
                j += 1
            i += 1
        elif j: #сдвиг на предыдущее значение из массива префиксов
            j = P[j - 1]
        else:
            i += 1
    return entries

#str = input("Введите строку:")
#sub = input("Введите подстроку:")
str = 'abcababcabcabd bacad abcabd'
sub = 'abcabd'

print("Вхождения обнаружены начиная с индексов:", *KMP(str, sub))
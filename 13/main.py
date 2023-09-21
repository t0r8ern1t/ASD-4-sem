#алгоритм бойера-мура

#таблица сдвигов
def Shift_table(patern):
    skip_list = {}
    for i in range(0,len(patern)):
        skip_list[patern[i]] = max(1, len(patern)-i-1)
    return skip_list

def Boyer_mur(str, sub):
    s_char = Shift_table(sub)
    print(s_char)
    i = len(sub)-1 #итератор для строки
    entries = []
    while i <=  len(str)-1:
        j = 0 # итератор для подстроки
        while j < len(sub) and sub[len(sub)-j-1] == str[i-j]:
            j+=1
        if j == len(sub): #подстрока совпадает с шаблоном
            entries.append(i-len(sub)+2)
            i += 1
            continue
        else:
            shift = s_char.get(str[i+j], len(sub)) #получаем сдвиг по строке из таблицы
            if shift == 0: # псли сдвига нет перемещаемся на длину шаблона
                shift = len(sub)-1
            skip = shift-j
            i += skip
    return entries

#str = input("Введите строку:")
#sub = input("Введите подстроку:")
str = 'abcababcabcabd bacad abcabd'
sub = 'abcabd'

print("Вхождения обнаружены начиная с индексов:", *Boyer_mur(str, sub))
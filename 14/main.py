#алгоритм рабина

alph_size = 128
q = 397

def Get_hash(text):
    res = 0
    for i in range(len(text)):
        res = (alph_size * res + ord(text[i])) % q
    return res

def Rabin(text, sub):
    text_len = len(text)
    sub_len = len(sub)
    multiplier = 1
    for i in range(1, sub_len):
        multiplier = (multiplier * alph_size) % q
    sub_hash = Get_hash(sub)
    text_hash = Get_hash(text[:sub_len])
    entries = []
    for i in range(text_len - sub_len + 1):
        if sub_hash == text_hash:
            #print(sub, text[i:i+sub_len])
            if text[i:i+sub_len] == sub:
                entries.append(i+1)
        if i < text_len - sub_len:
            text_hash = ((text_hash - ord(text[i]) * multiplier) * alph_size + ord(text[i+sub_len])) % q
        if text_hash < 0:
            text_hash += q
    return entries

#text = input("Введите строку:")
#sub = input("Введите подстроку:")
text = 'abcababcabcabd bacad abcabd'
sub = 'abcabd'
print("Вхождения обнаружены начиная с индексов:", *Rabin(text, sub))
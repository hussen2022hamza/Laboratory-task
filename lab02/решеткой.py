import numpy as np

def rot90(matrix):
    return np.rot90(matrix).tolist()

def udalenie(largelist, inn, k):
    for i in range(k*2):
        for j in range(k*2):
            if largelist[i][j] == inn:
                largelist[i][j] = " "
                return

def cardangrille():
    k = int(input("Введите число k: "))
    s = 1
    lists = [[s + j + i*k for j in range(k)] for i in range(k)]
    
    lists1 = rot90(lists)
    lists2 = rot90(lists1)
    lists3 = rot90(lists2)
    
    largelist = [[1 for _ in range(2*k)] for _ in range(2*k)]
    
    for i in range(k):
        for j in range(k):
            largelist[i][j] = lists[i][j]
            largelist[i][j+k] = lists1[i][j]
            largelist[i+k][j+k] = lists2[i][j]
            largelist[i+k][j] = lists3[i][j]
    
    text = "договорподписали"
    largelist_a = [[" " for _ in range(2*k)] for _ in range(2*k)]
    
    li = list(range(1, k**2 + 1))
    
    for inn in li:
        udalenie(largelist, inn, k)
    
    for _ in range(4):
        for i in range(k*2):
            for j in range(k*2):
                if largelist[i][j] == largelist_a[i][j] and text:
                    largelist_a[i][j] = text[0]
                    text = text[1:]
        largelist = rot90(largelist)
    
    stri = input("Введите пароль: ")
    
    if len(stri) > k*2:
        stri = stri[:k*2]
    else:
        stri = stri.ljust(k*2, "z")
    
    largelist_a.append(list(stri))
    
    result = ""
    spisok = sorted(largelist_a[-1])
    
    for i in spisok:
        col_index = largelist_a[-1].index(i)
        for j in range(len(largelist_a)-1):
            if largelist_a[j][col_index] != " ":
                result += largelist_a[j][col_index]
    
    print(result.replace(" ", ""))

cardangrille()
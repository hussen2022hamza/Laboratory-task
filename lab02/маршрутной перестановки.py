def marhsrutshifr():
    text = input("Введите текст: ").replace(' ', '')
    n = int(input("Введите число n: "))
    m = int(input("Введите число m: "))
    parol = input("Введите слово-пароль: ")
    
    lists = [['a' for _ in range(n)] for _ in range(m)]
    it = 0
    
    for i in range(m):
        for j in range(n):
            if it < len(text):
                lists[i][j] = text[it]
                it += 1
    
    lists.append(list(parol))
    
    spisok = sorted(lists[-1])
    result = ""
    
    for i in spisok:
        col_index = lists[-1].index(i)
        for j in range(m):
            result += lists[j][col_index]
    
    print(result)

marhsrutshifr()
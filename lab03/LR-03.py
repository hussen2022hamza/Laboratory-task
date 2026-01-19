
dict_r = {"а":1,"б":2,"в":3,"г":4,"д":5,"е":6,"ё":7,"ж":8,"з":9,"и":10,
          "й":11,"к":12,"л":13,"м":14,"н":15,"о":16,"п":17,"р":18,"с":19,
          "т":20,"у":21,"ф":22,"х":23,"ц":24,"ч":25,"ш":26,"щ":27,"ъ":28,
          "ы":29,"ь":30,"э":31,"ю":32,"я":33}
inv_dict = {v:k for k,v in dict_r.items()}

def gamma_cipher(text, gamma):
    t_digits = [dict_r[ch] for ch in text]
    g_digits = [dict_r[ch] for ch in gamma]
    
    encrypted = []
    g_idx = 0
    for val in t_digits:
        total = val + g_digits[g_idx]
        if total > 33:
            total %= 33
        encrypted.append(total)
        g_idx = (g_idx + 1) % len(g_digits)
    
    enc_text = ''.join(inv_dict[num] for num in encrypted)
    
    decrypted = []
    g_idx = 0
    for val in [dict_r[ch] for ch in enc_text]:
        diff = val - g_digits[g_idx]
        if diff < 1:
            diff += 33
        decrypted.append(diff)
        g_idx = (g_idx + 1) % len(g_digits)
    
    dec_text = ''.join(inv_dict[num] for num in decrypted)
    
    print("Числа текста:", t_digits)
    print("Числа гаммы:", g_digits)
    print("Числа шифра:", encrypted)
    print("Зашифрованный текст:", enc_text)
    print("Расшифрованный текст:", dec_text)

gamma_cipher("примертекста", "гаммаключ")

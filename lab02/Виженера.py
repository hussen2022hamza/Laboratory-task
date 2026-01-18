import sys

def encode_val(word):
    return [ord(ch) for ch in word]

def decode_val(list_in):
    return [chr(code) for code in list_in]

def comparator(value, key):
    return {i: [value[i], key[i % len(key)]] for i in range(len(value))}

def full_encode(value, key):
    dic = comparator(value, key)
    print('Compare full encode', dic)
    return [(dic[i][0] + dic[i][1]) % 127 for i in range(len(value))]

def full_decode(value, key):
    dic = comparator(value, key)
    print('Deshifre=', dic)
    return [(dic[i][0] - dic[i][1] + 127) % 127 for i in range(len(value))]

def vijer():
    word = "Hello world"
    key = "key"
    
    sys.stdout.write(word)
    sys.stdout.write(key)
    
    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
    
    sys.stdout.write(str(key_encoded))
    sys.stdout.write(str(value_encoded))
    
    shifre = full_encode(value_encoded, key_encoded)
    print('Шифр=', ''.join(decode_val(shifre)))
    
    decoded = full_decode(shifre, key_encoded)
    print('Decode list=', decoded)
    
    decode_word_list = decode_val(decoded)
    print('Word=', ''.join(decode_word_list))

vijer()
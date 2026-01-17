def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('а') if char.islower() else ord('А')
            result += chr((ord(char) - shift_base + shift) % 32 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

plain_text = "привет мир"
key = 3
encrypted = caesar_encrypt(plain_text, key)
decrypted = caesar_decrypt(encrypted, key)

print(f"Исходный текст: {plain_text}")
print(f"Зашифрованный текст: {encrypted}")
print(f"Расшифрованный текст: {decrypted}")

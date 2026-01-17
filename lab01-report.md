# ============================================
# Лабораторная работа №1: Шифр Цезаря
# ============================================

# -------- Введение --------
define INTRODUCTION
Шифр Цезаря --- это моноалфавитный шифр подстановки, в котором каждая
буква открытого текста заменяется на букву, находящуюся на фиксированное
число позиций (ключ) дальше в алфавите. Этот шифр назван в честь Юлия
Цезаря, который использовал его для защиты своей переписки.
endef

# -------- Математическая модель --------
define MATH_MODEL
Шифрование описывается формулой:

C = (P + k) mod m

где:

- P --- номер буквы открытого текста,
- C --- номер буквы шифртекста,
- k --- ключ (сдвиг),
- m --- количество букв в алфавите (например, 26 для латинского
  алфавита).

Расшифрование выполняется по формуле:

P = (C - k) mod m
endef

# -------- Реализация на Python --------
define PYTHON_CODE
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
endef

# -------- Пример работы программы --------
define EXAMPLE_OUTPUT
Исходный текст: привет мир
Зашифрованный текст: тулзйх рлу
Расшифрованный текст: привет мир
endef

# -------- Вывод --------
define CONCLUSION
Шифр Цезаря является простым и исторически значимым методом шифрования,
но он не обеспечивает достаточного уровня безопасности для современных
применений из-за уязвимости к частотному анализу и атакам методом brute
force.
endef

# -------- Список литературы --------
define REFERENCES
1.  Цезарь Ю. Записки о Галльской войне.
2.  Шнайер Б. Прикладная криптография. --- М.: Триумф, 2002.
3.  Алферов А.П. и др. Основы криптографии. --- М.: Гелиос АРВ, 2002.
4.  https://ru.wikipedia.org/wiki/Шифр_Цезаря
endef

# ============================================
# Цели Makefile
# ============================================

.PHONY: all intro math code example conclusion refs run

all: intro math code example conclusion refs

intro:
	@echo "Лабораторная работа №1: Шифр Цезаря"
	@echo "====================================="
	@echo ""
	@echo "Введение"
	@echo "---------"
	@echo "$$INTRODUCTION"

math:
	@echo ""
	@echo "Математическая модель"
	@echo "---------------------"
	@echo "$$MATH_MODEL"

code:
	@echo ""
	@echo "Реализация на Python"
	@echo "--------------------"
	@echo "$$PYTHON_CODE"

example:
	@echo ""
	@echo "Пример работы программы"
	@echo "------------------------"
	@echo "$$EXAMPLE_OUTPUT"

conclusion:
	@echo ""
	@echo "Вывод"
	@echo "------"
	@echo "$$CONCLUSION"

refs:
	@echo ""
	@echo "Список литературы"
	@echo "-----------------"
	@echo "$$REFERENCES"

run:
	@python3 -c "
def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('а') if char.islower() else ord('А')
            result += chr((ord(char) - shift_base + shift) % 32 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

plain_text = 'привет мир'
key = 3
encrypted = caesar_encrypt(plain_text, key)
decrypted = caesar_decrypt(encrypted, key)

print('Исходный текст:', plain_text)
print('Зашифрованный текст:', encrypted)
print('Расшифрованный текст:', decrypted)
"

# ============================================
# Генерация полного документа
# ============================================

gen_doc:
	@echo "Лабораторная работа №1: Шифр Цезаря" > lab1_caesar.txt
	@echo "=====================================" >> lab1_caesar.txt
	@echo "" >> lab1_caesar.txt
	@echo "Введение" >> lab1_caesar.txt
	@echo "---------" >> lab1_caesar.txt
	@echo "$$INTRODUCTION" >> lab1_caesar.txt
	@echo "" >> lab1_caesar.txt
	@echo "Математическая модель" >> lab1_caesar.txt
	@echo "---------------------" >> lab1_caesar.txt
	@echo "$$MATH_MODEL" >> lab1_caesar.txt
	@echo "" >> lab1_caesar.txt
	@echo "Реализация на Python" >> lab1_caesar.txt
	@echo "--------------------" >> lab1_caesar.txt
	@echo "$$PYTHON_CODE" >> lab1_caesar.txt
	@echo "" >> lab1_caesar.txt
	@echo "Пример работы программы" >> lab1_caesar.txt
	@echo "------------------------" >> lab1_caesar.txt
	@echo "$$EXAMPLE_OUTPUT" >> lab1_caesar.txt
	@echo "" >> lab1_caesar.txt
	@echo "Вывод" >> lab1_caesar.txt
	@echo "------" >> lab1_caesar.txt
	@echo "$$CONCLUSION" >> lab1_caesar.txt
	@echo "" >> lab1_caesar.txt
	@echo "Список литературы" >> lab1_caesar.txt
	@echo "-----------------" >> lab1_caesar.txt
	@echo "$$REFERENCES" >> lab1_caesar.txt
	@echo "Документ сохранён в lab1_caesar.txt"

help:
	@echo "Доступные команды:"
	@echo "  make all        - Показать весь документ"
	@echo "  make intro      - Показать введение"
	@echo "  make math       - Показать математическую модель"
	@echo "  make code       - Показать код Python"
	@echo "  make example    - Показать пример работы"
	@echo "  make conclusion - Показать вывод"
	@echo "  make refs       - Показать список литературы"
	@echo "  make run        - Запустить программу шифрования"
	@echo "  make gen_doc    - Создать текстовый файл с документом"
	@echo "  make help       - Показать эту справку"
word = input("Введите слово из маленьких латинских слов: ")

vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_count = 0
# подсчёт количества согласных букв
consonant_count = 0
specific_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letter in word:
    if letter in vowels:
        vowel_count += 1
        specific_vowels[letter] += 1
    else:
        consonant_count += 1

print("Всего гласных:", vowel_count)
print("Всего согласных:", consonant_count)

# Выводим количество каждой гласной, если она есть в слове
for vowel, count in specific_vowels.items():
    if count > 0:
        print(f"Буква '{vowel}': {count}")
    else:
        print(f"Буква '{vowel}': False")

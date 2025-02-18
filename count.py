word = input("Введите слово: ")


word = word.lower()

vowels = ['a', 'e', 'i', 'o', 'u']


vowel_count = 0
consonant_count = 0


for char in word:
    if char.isalpha():  
        if char in vowels:  
            vowel_count += 1
        else: 
            consonant_count += 1


print("Гласных букв:", vowel_count)
print("Согласных букв:", consonant_count)

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
def count_syllables(word):
    vowels = "аеёиоуыэюяaeiouy"
    return sum(1 for char in word.lower() if char in vowels)


def check_rhythm(poem):
    phrases = poem.split()

    if len(phrases) <= 1:
        return "Количество фраз должно быть больше одной!"

    syllable_counts = [count_syllables(phrase.replace('-', '')) for phrase in phrases]

    return "Парам пам-пам" if all(count == syllable_counts[0] for count in syllable_counts) else "Пам парам"


result = check_rhythm(stroka)
print(result)

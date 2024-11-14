from collections import defaultdict
import re

def generate_bigrams(text):
    # Розбиваємо текст на слова та видаляємо зайві символи
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Створюємо словник для зберігання біграм
    bigrams = defaultdict(list)
    
    # Заповнюємо словник біграм
    for i in range(len(words) - 1):
        first_word = words[i]
        second_word = words[i + 1]
        bigrams[first_word].append(second_word)
    
    return bigrams

def analyze_text(text):
    bigrams = generate_bigrams(text)
    
    # Виводимо кількість унікальних біграм
    unique_bigrams = sum(len(set(followers)) for followers in bigrams.values())
    print(f"Кількість унікальних біграм: {unique_bigrams}")
    
    # Виводимо кількість випадків для кожного слова
    for word, followers in bigrams.items():
        print(f"Слово '{word}' зустрічається перед: {', '.join(set(followers))}")

# Приклад використання
text = """
У цьому прикладі тексту ми будемо створювати ланцюги біграм, які складаються з пари слів.
Цей текст допоможе нам зрозуміти, як працюють ланцюги біграм у цьому тексті і додомо пару слів, які повторюються.
"""

analyze_text(text)

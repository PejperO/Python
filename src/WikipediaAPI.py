import string
import wikipediaapi


def read_titles(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def get_article(title):
    w_api = wikipediaapi.Wikipedia('en')
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""


def count_unique_letters(text):
    letters = set(text.lower())
    letters -= set(string.punctuation + string.whitespace)
    return len(letters)


def calculate_average_letter_count():
    total_count = 0
    article_count = 0
    for title in read_titles('small.txt'):
        article = get_article(title)
        if article:
            letter_count = count_unique_letters(article)
            total_count += letter_count
            article_count += 1

    if article_count > 0:
        average_count = total_count / article_count
        return average_count
    else:
        return 0


average_letter_count = calculate_average_letter_count()
print(f"Średnia liczba liter na artykuł: {average_letter_count}")

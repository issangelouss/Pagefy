import requests
from bs4 import BeautifulSoup

url = 'https://www.kinomania.ru/news'
ans = requests.get(url)
soup = BeautifulSoup(ans.text, 'html.parser')


def get_cinema_news():
    news_massive = soup.find_all('div', class_='pagelist-item clear')
    article_name_dictionary_cinema = {}

    # формирование словаря с артиклями и ссылками на статью
    for page in news_massive:
        if len(article_name_dictionary_cinema) == 25:
            break
        try:
            article = page.find('div', class_='pagelist-item-title').find('a').get_text(strip=True).replace('\xa0', ' ')
            link_to_new = 'https://www.kinomania.ru' + page.find('div', class_='pagelist-item-title').find('a').get('href')
            article_name_dictionary_cinema[article] = link_to_new
        except Exception:
            pass

    article_description_dict_cinema = {}
    for key in article_name_dictionary_cinema.keys():
        try:
            article_page = BeautifulSoup(requests.get(article_name_dictionary_cinema[key]).text, 'html.parser')
            first_sentence_finder = article_page.find('p').text.replace('\xa0', ' ')
            first_sentence_finder = first_sentence_finder[:first_sentence_finder.index('.') + 1]
            article_description_dict_cinema[key] = first_sentence_finder
        except Exception:
            pass

    return article_description_dict_cinema

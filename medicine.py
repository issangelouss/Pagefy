import requests
from bs4 import BeautifulSoup

url = 'https://www.rbc.ru/tags/?tag=%D0%BC%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BD%D0%B0'
ans = requests.get(url)
soup = BeautifulSoup(ans.text, 'html.parser')


def get_medicine_news():
    news_massive = soup.find_all('div', class_='search-item js-search-item')
    article_name_dictionary_medicine = {}

    # формирование словаря с артиклями и ссылками на статью
    for page in news_massive:
        if len(article_name_dictionary_medicine) == 25:
            break
        try:
            article = page.find('span', class_='search-item__title').get_text(strip=True).replace('\xa0', ' ')
            link_to_new = page.find('a').get('href')
            article_name_dictionary_medicine[article] = link_to_new
        except Exception:
            pass

    article_description_dict_medicine = {}
    for key in article_name_dictionary_medicine.keys():
        try:
            article_page = BeautifulSoup(requests.get(article_name_dictionary_medicine[key]).text, 'html.parser')
            first_sentence_finder = article_page.find('div', class_='article__text__overview').find('span').text.replace('\xa0', ' ')
            article_description_dict_medicine[key] = first_sentence_finder
        except Exception:
            pass

    return article_description_dict_medicine

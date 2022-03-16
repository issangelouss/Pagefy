import requests
from bs4 import BeautifulSoup

url = 'https://www.gazeta.ru/politics/news/'
ans = requests.get(url)
soup = BeautifulSoup(ans.text, 'html.parser')


def get_politics_news():
    news_massive = soup.find_all('div', class_='b_ear m_techlisting')
    article_name_dictionary_politics = {}

    # формирование словаря с артиклями и ссылками на статью
    for page in news_massive:
        if len(article_name_dictionary_politics) == 25:
            break
        article = page.find('div', class_='b_ear-textblock').find('div', class_='b_ear-title').get_text(strip=True).replace('\xa0', ' ')
        link_to_new = 'https://www.gazeta.ru/' + page.find('div', class_='b_ear-textblock').find('div', class_='b_ear-title').find('a').get('href')
        article_name_dictionary_politics[article] = link_to_new

    article_description_dict_politics = {}
    for key in article_name_dictionary_politics.keys():
        try:
            article_page = BeautifulSoup(requests.get(article_name_dictionary_politics[key]).text, 'html.parser')
            first_sentence_finder = article_page.find('div', class_='b_article-text').find('p').text.replace('\xa0', ' ')
            article_description_dict_politics[key] = first_sentence_finder
        except Exception:
            pass

    return article_description_dict_politics



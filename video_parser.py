from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://www.youtube.com/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path='C:\\Users\\Admin\\PycharmProjects\\flaskproj\\chromedriver.exe',
    options=options
)
driver.get(url)
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


def get_video_previews():
    previews_massive = soup.find_all('div', class_='style-scope ytd-rich-item-renderer')
    previews = {}

    # формирование словаря с названиями и превью видео
    for preview in previews_massive:
        if len(previews) == 10:
            break
        try:
            name = preview.find('a', id='video-title-link').get('title')
            link_to_photo = preview.find('img', class_='style-scope yt-img-shadow').get('src')
            if link_to_photo:
                previews[name] = link_to_photo
        except Exception:
            pass

    return previews



import requests
from bs4 import BeautifulSoup

testURL = 'https://www.scrapethissite.com/pages/simple/'

page = requests.get(testURL)
soup = BeautifulSoup(page.text, "html.parser")

country_names = []

for names in soup.find_all('h3', class_='country-name'):
    country_names.append(names.text.strip())

print(country_names)

print('There is', len(country_names), 'country names in our list.')

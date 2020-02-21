import pandas
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.amazon.in/s?k=earphone&ref=nb_sb_noss_2')

earphones = BeautifulSoup(page.content, 'html.parser')

items = earphones.find(class_='a-carousel')


desc = items.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")
prices = items.find_all(class_='a-price-whole')

descpriction = [item.get_text() for item in desc]
price = [item.get_text() for item in prices]



print(len(prices))
print(len(descpriction))

earphones1 = pandas.DataFrame({
    'details': descpriction,
    'price': price,
})

print(earphones1)
earphones1.to_csv('earphones1.csv')


# print(earphones)
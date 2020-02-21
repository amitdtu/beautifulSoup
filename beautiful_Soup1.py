import pandas
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XirZPWgzbIU')
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.find_all('a'))

week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())
# print(week.find_all(class_='period-name'))

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descripttion = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]
# print(period_names)
# print(short_descripttion)
# print(temp)

weather = pandas.DataFrame({
    'period': period_names,
    'short_description': short_descripttion,
    'temp': temp
})

weather.to_csv('weather_info1.csv')

print(weather)


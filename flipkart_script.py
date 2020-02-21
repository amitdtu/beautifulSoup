import pandas
from bs4 import BeautifulSoup
import requests

df = pandas.DataFrame(columns=['model','price'])
for i in range(6,11):
    if i == 0:
        pass
    else:
        response = requests.get('https://flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DAsus&otracker=nmenu_sub_Electronics_0_Asus&page=' + str(i))

        page = BeautifulSoup(response.content, 'html.parser')
        
        mobile = page.find_all(class_='_1HmYoV hCUpcT')
        print(len(mobile))
        models = mobile.find_all(class_='_3wU53n')
        prices = mobile.find_all(class_='_1vC4OE _2rQ-NK')
        ratings = mobile.find_all(class_='hGSR34')

        model_text = [model.get_text() for model in models]
        price = [(price.get_text()).replace('₹', 'Rs ') for price in prices]
        # rating = [rate.get_text() for rate in ratings]

        print(len(model_text), i)
        print(len(price), i)
        print(mobile)

        df1 = pandas.DataFrame({
            'model': model_text,
            'price': price,
            })

        df = df.append(df1, ignore_index=True)

    # print(len(price))
    # print(model_text)
    # print(mobile)
    # df = pandas.DataFrame(columns=['model_text'])
    # df1 = df.append({'model': model_text}, ignore_index=True)
    # if i == 1:
    #     df1 = pandas.DataFrame({
    #     'model': model_text,
    #     'price': price,
    #     'rating': rating
    #     })
    #     # print(df1)
    # else:
    #     globals() ['df1']
    #     df2 = pandas.DataFrame({
    #     'model': model_text,
    #     'price': price,
    #     'rating': rating
    #     })
    #     df1.append(df2, ignore_index=True)
    #     print(df1)



df.to_csv('asus2.csv')
print(df)







# print(price)
# print(model_text)
# print(mobile)


# mobiles.to_csv('flipkart_mobiles1.2.csv')
# print(mobiles)
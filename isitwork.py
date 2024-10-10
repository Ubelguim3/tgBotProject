import requests

domens = ['.ru', '.com', '.рф', '.net', '.org', '.ru.net', '.pro', '.ua', ]

# print("Введите название сайта c доменом:")
website = input()
site =  f'https://www.{website}'
try:
    response = requests.get(site)
    print(f'сайт {site} можно открыть в России')
except:
    print(f'Сайт {site} невозможно открыть в России')

import requests
from bs4 import BeautifulSoup
import multiprocessing as mp


def convert_number(number):
    if 'k' in str(number):
        if '.' in str(number):
            number = number.replace('k','')
            number = str(float(number)*1000)
        else:
            number = number.replace('k', '000')
    return number


def melbourne_user_count(page_count):
    print('Doing page count:', page_count)

    res = requests.get('https://stackoverflow.com/users?page=' + str(page_count) + '&tab=reputation&filter=all')
    soup1 = BeautifulSoup(res.text, 'html.parser')
    users = soup1.select('.user-info')

    for user in users:
        user_reputation = user.select('.reputation-score')[0].getText()
        user_location = user.select('.user-location')[0].getText()

        if user_location != '':
            return [convert_number(user_reputation), user_location]


if __name__ == "__main__":
    page_number = 1
    response = requests.get('https://stackoverflow.com/users?page='+str(page_number)+'&tab=reputation&filter=all')

    soup = BeautifulSoup(response.text, 'html.parser')
    page_numbers = soup.select('.page-numbers')
    pool = mp.Pool(mp.cpu_count())

    file_handler = open('scrape-results/scrape-location-melbourne.txt', 'w+', encoding="utf-8")

    max_pages = 2  # int(page_numbers[len(page_numbers)-2].getText())
    # for i in range(1, max_pages, 30):
    for i in range(1, max_pages):
        result = pool.map(melbourne_user_count, range(i, i+30))
        result = filter(None, result)
        for items in list(result):
            file_handler.write(','.join(items) + '\n')

    file_handler.close()
    pool.close()

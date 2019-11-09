import requests
from bs4 import BeautifulSoup
import multiprocessing as mp

# user_list = list()

def convert_number(number):
    '''
    Function to convert k to integer thousand
    :param number: String
    :return: converted number
    '''
    if 'k' in str(number):
        if '.' in str(number):
            number = number.replace('k','')
            number = str(float(number)*1000)
        else:
            number = number.replace('k', '000')
    return number


def melbourne_user_count(page_count):
    '''
    Function to scrape information from Users page in StackOverflow
    Takes page_number as param to iterate between pagination
    :param page_count: page number
    :return: list of extracted information
    '''
    print(page_count)
    res = requests.get('https://stackoverflow.com/users?page=' + str(page_count) + '&tab=reputation&filter=all')
    soup1 = BeautifulSoup(res.text, 'html.parser')
    users = soup1.select('.user-info')
    user_list = list()
    for user in users:
        user_reputation = user.select('.reputation-score')[0].getText()
        user_location = user.select('.user-location')[0].getText()
        user_list.append([convert_number(user_reputation), user_location])
        # if user_location != '':
    print(user_list)
    return user_list


if __name__ == "__main__":
    page_number = 1
    response = requests.get('https://stackoverflow.com/users?page='+str(page_number)+'&tab=reputation&filter=all')

    soup = BeautifulSoup(response.text, 'html.parser')
    page_numbers = soup.select('.page-numbers')
    pool = mp.Pool(mp.cpu_count())

    file_handler = open('djstack\\stackoverflowapi\\scrape-file\\scrape-location-melbourne.csv', 'w+', encoding="utf-8")

    # Commented total pages to limit the number of request sent to stackoverflow
    # Can be increased or decreased based on demand
    max_pages = 2  # int(page_numbers[len(page_numbers)-2].getText())
    result = [pool.apply(melbourne_user_count, args=(i,)) for i in range(1, max_pages)]  # Divide task between cores
    for items in result:
        for pages in items:
            file_handler.write(','.join(pages) + '\n')

    file_handler.close()
    pool.close()

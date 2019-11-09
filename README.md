# stackoverflow-user-rank

An application built to calculate and display the StackOverflow user rank based on his current reputation number. 

## Installation
Make sure you have Anaconda installed in your system.
#### 1. Install and run Django server
Open Anaconda Prompt

cd djstack 

install pipenv

pipenv install

pipenv shell

python manage.py runserver

#### 2. Install npm packages and run react app
cd scrapeui

npm install

yarn start

## Flow

Below is the overall flow of the program:
#### 1. Stackoverflow Data Scraper
Language: Python
Location: /

The StackOverflow data was extracted from page https://stackoverflow.com/users?tab=Reputation&filter=all using BeautifulSoup into a CSV file scrape-location-melbourne.csv. This data is then filtered by people based in Melbourne for the scope of this project.
The throttle limit set by StackOverflow limits the number of user that can be extracted through web scrapper but data containing all users can still be extracted from https://data.stackexchange.com/stackoverflow/queries using SQL query. This data is stored in QueryResults.csv.

#### 2. Django service
Language: Python
Location: djstack/

The Django acts as a service to take URL input from the UI and calculate the rank of user based on his current reputation level compared to other users from Melbourne.
Currently UI initiates a GET request to django server with stackoverflow url as query param.

#### 3. UI
Language: Javascript
Location: scrapeui/

It is a minimalistic UI built using ReactJS and MaterialUI to display the user's rank and his other attributes such as badges, reputation, votes, etc. This data can be toggled using the user-option.json.

# Getting the source code from wikipedia
import pickle # Serialises any python object, basically to save SP 500 list
import requests
# Beautiful Soup Webscraper 
import bs4 as bs
import pandas_datareader as web
import datetime

start = datetime.datetime(2010, 12, 1)
end = datetime.datetime(2018,1,31)

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml') # beautifulsoup object
    table = soup.find('table', {'class': 'wikitable sortable'}) # Uses Soup to find the S & P 500 list
    tickers = []
    for row in table.findAll('tr')[1:]: # Each table row without the title
        ticker = row.findAll('td')[0].text
        ticker= ticker[:-1]
        tickers.append(ticker)
        
        
    with open("sp500tickers.pickle", 'wb') as f:
        pickle.dump(tickers, f)
        
    print(tickers)    
    return tickers

save_sp500_tickers()
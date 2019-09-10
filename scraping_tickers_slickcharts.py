# Getting the source code from slickcharts
import pickle # Serialises any python object, basically to save SP 500 list
import requests
# Beautiful Soup Webscraper 
import bs4 as bs
import pandas_datareader as web
import datetime

start = datetime.datetime(2010, 12, 1)
end = datetime.datetime(2018,1,31)

def save_sp500_companies_tickers():
    resp = requests.get('https://www.slickcharts.com/sp500')
    soup = bs.BeautifulSoup(resp.text, 'lxml') # beautifulsoup object
    table = soup.find('table', {'class': 'table table-hover table-borderless table-sm'}) # Uses Soup to find the S & P 500 list
    tickers_2 = []
    company = []
                        
    for row in table.findAll('tr')[1:]: # Each table row without the title
        ticker1 = row.findAll('td')[2].text
        tickers_2.append(ticker1)
                        
        company1 = row.findAll('td')[1].text
        company.append(company1)
        
        
    with open("sp500tickers_2.pickle", 'wb') as a:
        pickle.dump(tickers_2, a)
        
    with open("sp500company.pickle", 'wb') as b:
        pickle.dump(company, b)
                        
    print(tickers_2)   
    print(company)
    return tickers_2, company

save_sp500_companies_tickers()
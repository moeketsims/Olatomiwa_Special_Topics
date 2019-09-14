# Taking the Entire dataset from yahoo and storing it locally on my pc.
# Workin with the list of SPM 500 companies
# working with the company's data
import os
import pandas as pd

def get_data_from_yahoo2(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_companies_tickers()
    else:
        with open('sp500tickers_2.pickle', 'rb') as a:
            tickers = pickle.load(a)
            
    if not os.path.exists('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/slickcharts'):
        os.makedirs('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/slickcharts')
        
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/scraped stocks/slickcharts/{}.csv'.format(ticker)):
            df = web.DataReader(ticker.replace('.','-'), 'yahoo', start)
            df.to_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/slickcharts/{}.csv'.format(ticker))
        else:
            print('Already have ()'.format(ticker))
            
get_data_from_yahoo2()
# Taking the Entire dataset from yahoo and storing it locally on my pc.
def get_data_from_yahoo(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open('sp500tickers.pickle', 'rb') as f:
            tickers = pickle.load(f)
            
    if not os.path.exists('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks'):
        os.makedirs('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks')
        
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/scraped stocks/{}.csv'.format(ticker)):
            df = web.DataReader(ticker.replace('.','-'), 'yahoo', start)
            df.to_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/{}.csv'.format(ticker))
        else:
            print('Already have ()'.format(ticker))
            
get_data_from_yahoo()
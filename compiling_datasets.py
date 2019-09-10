# Compiling all the data frames into 1 huge data set sp_500_ALL
def compile_data():
    with open('sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    
    # empty dataframe object
    main_df1 = pd.DataFrame()
    main_df2 = pd.DataFrame() 
    main_df3 = pd.DataFrame()
    
    # begin iterating through the tickers we have instead of the files in the directory
    for count, ticker in enumerate(tickers):
        df1 = pd.read_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/{}.csv'.format(ticker))
        df2 = pd.read_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/{}.csv'.format(ticker))
        df3 = pd.read_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/{}.csv'.format(ticker))
        
        df1.set_index('Date', inplace = True)
        df2.set_index('Date', inplace = True)
        df3.set_index('Date', inplace = True)
        
        company = []
        
        df1.rename(columns = {'Adj Close':ticker+' Adj Close'}, inplace = True)
        df1.drop(['Open','High','Low','Close', 'Volume'], axis = 1, inplace = True)
        
        df2.rename(columns = {'Volume':ticker+' Volume', 'Adj Close':ticker+' Adj Close'}, inplace = True) # changing name to organisation name
        df2.drop(['Open','High','Low','Close'], axis = 1, inplace = True)
        
        df3.rename(columns = {'Volume':ticker+' Volume'}, inplace = True)
        df3.drop(['Open','High','Low','Close', 'Adj Close'], axis = 1, inplace = True)

        
        if main_df1.empty:
            main_df1 = df1
        else:
            main_df1 = pd.concat([main_df1, df1], axis = 1)
            
        if main_df2.empty:
            main_df2 = df2
        else:
            main_df2 = pd.concat([main_df2, df2], axis = 1)
              
        if main_df3.empty:
            main_df3 = df3
        else:
            main_df3 = pd.concat([main_df3, df3], axis = 1)
        
            
        if(count % 10 == 0):
            print(count)
      
    print(main_df1.head()) # Adj Close Seperately
    print(main_df2.head()) # Both
    print(main_df3.head()) # Volume Seperately
    main_df1.to_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/sp500_close.csv')  
    main_df2.to_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/sp500_ALL.csv')  
    main_df3.to_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/sp500_volume.csv')  
compile_data()
# Putting datasets on top of each other & Including Company ticker
def compile_data2():
    with open('sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    
    # empty dataframe object
    main_df1 = pd.DataFrame()
    
    # begin iterating through the tickers we have instead of the files in the directory
    for count, ticker in enumerate(tickers):
        df = pd.read_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/{}.csv'.format(ticker))
        
        df['Company'] = ticker
        
        if main_df1.empty:
            main_df1 = df
        else:
            main_df1 = pd.concat([main_df1, df])
        
            
        if(count % 10 == 0):
            print(count)
      
    print(main_df1.head())
    print(main_df1.tail())
    main_df1.to_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/sp500_concat.csv')  

compile_data2()
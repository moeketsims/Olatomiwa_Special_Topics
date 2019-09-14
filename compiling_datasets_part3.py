# Putting datasets on top of each other & Including Company Name
def compile_data3():
    with open('sp500tickers_2.pickle', 'rb') as a:
        tickers = pickle.load(a)
    with open('sp500company.pickle', 'rb') as b:
        company = pickle.load(b)
        
        
    # empty dataframe object
    main_df1 = pd.DataFrame()
    
    # begin iterating through the tickers we have instead of the files in the directory
    for count, ticker in enumerate(tickers):
        df = pd.read_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/slickcharts/{}.csv'.format(ticker))
        
        df['Company'] = company[count]
        
        if main_df1.empty:
            main_df1 = df
        else:
            main_df1 = pd.concat([main_df1, df])
        
            
        if(count % 10 == 0):
            print(count)
      
    print(main_df1.head())
    print(main_df1.tail())
    main_df1.to_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/2nd Semester/Special Topics/scraped stocks/slickcharts/sp500_new.csv')  

compile_data3()
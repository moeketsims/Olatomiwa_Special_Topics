sp500_concat.drop("Unnamed: 0", axis = 1, inplace = True)
sp500_concat[sp500_concat['Company'] == "MMM"]
sp500_concat.dropna(axis = 0, inplace = True)
sp500_All.dropna(axis = 1, inplace = True)
sp500_close.dropna(axis = 1, inplace = True)
sp500_volume.dropna(axis = 1, inplace = True)

for i in range(int(len(tickers))):
    sp500_close[tickers[i]+' Adj Close'] = sp500_close[tickers[i]+' Adj Close'].fillna(method = 'ffill', inplace = True)
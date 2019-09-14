# each model will be Per company basis
# each company takes into account of all other companies within the S & P 500

def process_data_for_labels(ticker):
    days = 7 # Number of days
    df = pd.read_csv('C:/Users/Olatomiwa/Documents/SOL PLAATJE UNIVERSITY/HONOURS 2019/RESEARCH/STOCK_DFS/sp500_joined_closes.csv', index_col = 0)
    tickers = df.columns.values #.tolist() not necessary
    df.fillna(0, inplace = True)
    
    for i in range(1, days + 1):
        # Company name and days into the future
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker] 
        # .shift shifts up to get the future value old - new divided by 
        
    df.fillna(0, inplace = True)
    return tickers, df

process_data_for_labels('MMM')

# takes the 7 day percent changes for the prices in the future
def buy_sell_hold(*args): # *args lets us pass any parameters, any number of arguments which becomes an iterable
    cols = [c for c in args] # passing each column mapping it row wise
    requirement = 0.02 # if the stock price changes by 2%
    for col in cols:
        if(col > requirement):
            return(1)   # GAIN
        if(col < -requirement):
            return(-1)  # FALL
    return(0) # if both statements are false therefore Hold

from collections import Counter

def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)
    days = 7 # Number of days
    
    # The new column will have the mapped answer of buy_sell_hold
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold, *[df['{}_{}d'.format(ticker, i)]for i in range(1, days+1)]))
    
    vals = df['{}_target'.format(ticker)].values #.tolist optional 
    str_vals = [str(i) for i in vals]
    
    print('Data spread: ', Counter(str_vals)) # seeing th way in which buys/sell/hold are distributed
    df.fillna(0, inplace = True) # replacing prior nans with 0 (percent change)
    
    df = df.replace([np.inf, -np.inf], np.nan) # replacing infinite changes with nan
    df.dropna(inplace = True)
    
    # creating the feature sets and target labels (pct_change() is basically normalising the prices as regards to one day)
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace = True)
    
    # x_features and y_target
    
    x_features = df_vals.values 
    y_target = vals
    
    return x_features, y_target, df

extract_featuresets('MMM')

# Feeding the data into a classifier

from sklearn import svm, neighbors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

# Machine Learning function
def do_ml(ticker):
    features, target, df = extract_featuresets(ticker)
    
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size = 0.25, stratify = target)
    
    # x_train is the percent change
    classifier = neighbors.KNeighborsClassifier()
    classifier.fit(x_train, y_train)
    
    confidence = classifier.score(x_test, y_test)
    print('Accuracy', confidence)
    
    predictions = classifier.predict(x_test)
    print('Prediction Spread: ', Counter(predictions))
    
    return(confidence)

# Testing with a single company's stock
do_ml('BAC')

"""
A voting Classifier consisting of multiple classifiers that will vote on which one is best, Consists of:
+ Linear Support Vector Classifier
+ K-Neighbors Classifier
+ Random Forest
"""

def do_ml_vote(ticker):
    features, target, df = extract_featuresets(ticker)
    
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size = 0.25, stratify = target)
    
    # x_train is the percent change
    classifier = VotingClassifier([('lvsc', svm.LinearSVC()),
                                   ('knn', neighbors.KNeighborsClassifier()),
                                   ('rfor', RandomForestClassifier())])
    
    classifier.fit(x_train, y_train)
    
    confidence = classifier.score(x_test, y_test)
    print('Accuracy', confidence)
    
    predictions = classifier.predict(x_test)
    print('Prediction Spread: ', Counter(predictions))
    
    return(confidence)

# Testing with a single company's stock
do_ml_vote('BAC')
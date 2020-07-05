import pandas as pd 
  
df = pd.read_excel('HDFC.NS#HOUSING DEVELOPMENT FINANCE CORP ORD (D).xlsx') 


def changeDateFomat(x):
    import datetime
    
    if isinstance(x, str):
        # print(x)
        if x.endswith(' 12:00:00 AM'):
            x = x[:-12]
        # print(x)
        x = datetime.datetime.strptime(x,'%m/%d/%Y')
        # print(x)
        return x.strftime('%Y-%m-%d')
    # print(x.strftime('%d-%m-%Y'))

    return x.strftime('%Y-%d-%m')
    

# changeDateFomat("1/13/2000 12:00:00 AM")
df['DATE'] = df['DATE'].apply(changeDateFomat)
df = df.drop(['SYMBOL', 'INTERVAL'], axis=1)
df.to_csv("data.txt", index = False)

import pandas as pd
import numpy as np

data = {
    'Property_ID': [1001, 1002, 1003, 1004, 1001, 1005, 1006],
    'Area_sqft': [1200, 2500, np.nan, 1800, 1200, 50000, 2200], 
    'City_Zone': ['North', 'South', 'East', 'North', 'North', 'West', 'South'],
    'Base_Price': ['50000', '80000', '60000', '70000', '50000', '90000', '75000'],
    'Construction_Date': ['2015-01-01', '2010-05-20', '2018-03-15', '2012-11-10', '2015-01-01', '2020-01-01', '2014-06-01']
}

df = pd.DataFrame(data)
df=df.drop_duplicates()
df['Construction_Date']=pd.to_datetime(df['Construction_Date'])
df['House_Age'] = 2026 - df['Construction_Date'].dt.year
df['Area_sqft']=df['Area_sqft'].fillna(df['Area_sqft'].median())
df=df[df['Area_sqft']<10000]
df['Base_Price']=df['Base_Price'].astype(int)
df['Total_Tax'] = (df['Base_Price'] * 0.05) + (df['House_Age'] * 100)
df=pd.get_dummies(df,columns=['City_Zone'])
numpy_dataset = df.to_numpy()
print(df['Total_Tax'])
print(df)
print(numpy_dataset)

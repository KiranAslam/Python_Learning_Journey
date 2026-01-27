import pandas as pd
import numpy as np
#project_01
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
numpy_dataset =df[['Area_sqft', 'House_Age', 'Total_Tax']].to_numpy()
print(df['Total_Tax'])
print(df)
print(numpy_dataset)
print("======================================")
#project_02
np.random.seed(42)

employees = {
    'Emp_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR', 'Sales'],
    'Monthly_Salary': [5000, 4500, 6000, 3500, 4000, 5500, 4800, 3800],
    'Projects_Done': [5, 2, 8, 3, 4, 7, 1, 5],
    'Experience_Years': [3, 1, 10, 2, 4, 8, 1, 5]
}

df_emp = pd.DataFrame(employees) 
filtering=df_emp[df_emp['Projects_Done']>5]['Emp_ID'].values
df_emp['Performance_Score']=(df_emp['Projects_Done']*0.7)+(df_emp['Experience_Years']*0.3)
df_emp['Bonus']=np.where(df_emp['Performance_Score']>5,1000,200)
avg_sal=df_emp.groupby('Department')['Monthly_Salary'].mean()
Z_Score=(df_emp['Monthly_Salary']-df_emp['Monthly_Salary'].mean())/df_emp['Monthly_Salary'].std()
print(f"Z_score of Monthly Salary:{Z_Score}")
print(f"Average Salary of Each department: {avg_sal}")
filt=df_emp[(df_emp['Department']=='IT') & (df_emp['Performance_Score']>7)]
numpy_emp_data=df_emp[['Monthly_Salary','Bonus']].to_numpy()
total=np.sum(numpy_emp_data,axis=0)
raise_map = {
    'IT': 1.10,    
    'Sales': 1.05, 
    'HR': 1.02    
}
df_emp['New_Salary']=df_emp['Monthly_Salary']*df_emp['Department'].map(raise_map)
print(df_emp[['Department', 'Monthly_Salary', 'New_Salary']])
print(numpy_emp_data)
print("------------------")
print(f"Total of Monthly salary and Bonus\n{total}")
print(filt)
print(df_emp['Bonus'])
print(df_emp['Performance_Score'])
print(filtering)
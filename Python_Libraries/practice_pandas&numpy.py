import pandas as pd
import numpy as np 
import random

#========Practice numpy========
#TAsk 01
single_plant=np.array([15.5, 3.2, 28.0])
plant_datasets=np.array([
    [15.5, 3.2, 28.0],
    [14.0, 2.9, 27.5],
    [18.2, 3.5, 30.1]
])

print(plant_datasets.shape)
print(single_plant.shape)
normalized_data=plant_datasets/10
print(normalized_data)


#Task 02  (min max scaling)
prices=np.array([20000, 50000, 35000, 90000])
p_min=np.min(prices)
p_max=np.max(prices)

normalized_price=(prices-p_min)/(p_max-p_min)
print(f"original prices: {prices}")
print(f"normalized prices: {normalized_price}")

#task 03 (Z-score standardization)

scores = np.array([88, 92, 70, 50, 100, 200])

mean_val=np.mean(scores)
std_val=np.std(scores)
standardization=(scores-mean_val)/std_val
print(f"Original score: {scores}")
print(f"Mean value: {mean_val}")
print(f"standard deviation: {std_val}")
print(f"Standardized (Z-score) Data: {standardization}")

#verification

print(f"new mean value {np.mean(standardization).round()}")
print(f"new std deviation {np.std(standardization)}")


#Task 04 (Reshaping)

raw_data=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
image_format=raw_data.reshape(3,4)
print(f"original data: {raw_data}")
print(f"Reshaped data:{image_format}")

auto_reshaped=raw_data.reshape(2,-1)
print(f"Auto reshaped:{auto_reshaped}")

#task 05 (Vectorization)

prices_usd=np.array([12,14,11,16.22,18,25,56])
prices_pkr=prices*280
print(f"USD price: {prices_usd}")
print(f"PKR price:{prices_pkr}")

image=np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

bright_image=image+50
print(f"brightened image pixels: {bright_image}")

#Task 06 (mean squared Error)

actual = np.array([100, 200, 300 , 400,500])
predicted = np.array([110, 190, 320,410,480])

error=actual-predicted
squared_error=error**2
mse=np.mean(squared_error)
print(f"Individual error : {error}")
print(f"squared error : {squared_error}")
print(f"MSE : {mse}")

#Task 07 (dot product)

inputs=np.array([0.8, 0.9, 0.4])
weights=np.array([10.0,8.0,2.0])

prediction_score=np.dot(inputs,weights)
print(f"Prediction score is : {prediction_score}")
if prediction_score>15:
    print("Loan approved")
else:
    print("Loan rejected")

#Task 08 (broadcasting)

data=np.array([[10, 20], 
               [30, 40], 
               [50, 60]])
adjustment=np.array([10,15])
new_data=data+adjustment
print(f"original data {data}")
print(f"adjusted data {new_data}")

#Task 09
y_true=np.array([1,0,1,1,0])
y_predicted=np.array([0.9, 0.1, 0.8, 0.4, 0.2])

abs_error=abs(y_true-y_predicted)
mean_error=np.mean(abs_error)
arg_max=np.argmax(y_true)
print(f"Arg max value {arg_max}")
print(f"absolute error {abs_error}")
print(f"Mean Error {mean_error}")
if mean_error<0.2:
    print("Model is good")
else:
    print("model needs training")

#Task 10
weights=np.zeros([3,2])
line_point=np.linspace(0,10,5)
print(f"initial weights: {weights}")
print(f"line points: {line_point}")

#task 11 (Matrix Transpose)

X=np.array([[1,2],[3,4],[5,6]])
X_T=X.T
print(f"original shape {X.shape}")
print(f"transposed shape {X_T.shape}")

#Task 12

probs=np.array([0.1, 0.8, 0.4, 0.9, 0.3])
labels=np.where(probs>0.5,1,0)
print(f"Model Probabilities:{probs}")
print(f"final classification: {labels}")

#Task 13

students_data=np.array([[4,70],
                        [3,60],
                        [8,90],
                        [6,80]])

mean_val=np.mean(students_data,axis=0)
std_val=np.std(students_data,axis=0)
normalized_data = (students_data - mean_val) / std_val
weights=np.random.rand(2,1)
scores=np.dot(normalized_data,weights)
lebals=np.where(scores>0 ,'pass','fail')
print("--- Prediction Results ---")
print("Scores:\n", scores)
print("\nFinal Decisions:\n", lebals)
pass_count=np.sum(lebals=='pass')
print(f"total students passed: {pass_count}")

#=======Practice pandas=======

#Task 01 
data=np.array([ [4,70],
                [3,60],
                [8,90],
                [6,80]])
df=pd.DataFrame(data, columns=["Hours","Attendence"])
print("Student data")
print(df)

data_dic={
    'Name': ['Samiya', 'Rehan', 'Kiran', 'Aslam'],
    'Hours': [4, 3, 8, 6],
    'Attendance': [70, 60, 90, 80]
}
df1=pd.DataFrame(data_dic)
print("student data")
print(df1)
print(df1.describe())
print(df1["Name"])
print(df1.shape)
print(df1.head(2))
print(df1.tail(1))
print(df1.info())

#Task 02 Selection
position=df.iloc[0:2,0:2]
print(position)
print(df.loc[0,"Hours"])

max_att=df["Attendence"].max()
print(f"max attendence {max_att}")
mean_att=df["Attendence"].mean()
print(f"mean of Attendence {mean_att}")

#filtering 
busy_stud=df[df["Hours"]>5]
print(f"busy student list:\n{busy_stud}")

data = {
    'Name': ['Ali', 'Sara', 'Zain', 'Dua', 'Ahmed', 'Hira'],
    'Marks': [85, 92, 500, 78, -10, 88]  
}
df2=pd.DataFrame(data)
clean_data=df2[(df2["Marks"]>0) & (df2["Marks"]<100)]
print(f"cleaned data: { clean_data}")
print(f"original data: {df2}")
print(f"Mean of original data {df2["Marks"].mean()}")
print(f"Mean of cleaned data: {clean_data["Marks"].mean()}")
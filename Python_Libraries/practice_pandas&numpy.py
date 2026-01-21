import pandas as pd
import numpy as np 

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
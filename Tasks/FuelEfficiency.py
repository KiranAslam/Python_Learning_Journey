distance=float(input("Enter the distance how long your vehicle traveled:"))
fuel=float(input("how many liters your vehicle consumed fuel: "))
efficiency=distance/fuel
economical=efficiency>15
print("the efficiency of your vehicle in ", distance ," km distance comsuming ", fuel , " liter fuel is :", efficiency)
print("the vehicle is economical: ", economical)
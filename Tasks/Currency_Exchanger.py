USD=float(input("Enter the amount in USD:"))
USD_in_PK=280
PKR=USD_in_PK*USD
bank_fee=(2/100)*PKR
total_PKR=PKR-bank_fee
print(USD ," USD dollar in PKR is" , total_PKR, " After cuting 2% bank fee")
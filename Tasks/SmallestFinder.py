nums = [25, 12, 45, 8, 33, 19]
smallest=nums[0]
for n in nums:
    if n<smallest:
        smallest=n
print("Smallest number in list is: ", smallest)
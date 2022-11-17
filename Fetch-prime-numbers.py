# Creating an array that is having user defined inputs and with the help of for loop, fetching all the prime numbers                      
    
a = []
n = int(input('Enter the number of elements'))
for i in range(n):
    j = int(input("Enter the number"))
    a.append(j)

print(f"Here is your list: {a}") 

import numpy as np
arr = np.array(a)
print(f"Converted to array: {arr}")
print("Fetching prime numbers from the array")

for k in arr:
    if k>1:
        for l in range(2,k):
            if k%l==0:
                print(f"{k} is not a prime number")
                break
        else:
            print(f"{k} is a prime number")
    else:
        print(f"{k} is not a prime number")  

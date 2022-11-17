# Writing a function to take an array and returning another array that contains members of first array that are even

a = []
n = int(input("Enter the number of elements"))
for i in range(n):
    b = int(input("Enter the number"))
    a.append(b)
print(f"Here is the list: {a}")
import numpy as np
arr1 = np.array(a)
print(f"Converting into array: {arr1}")
print(" ")
print("Fetching even numbers from array")
print(" ")
even_list = []

for j in arr1:
    if j%2==0:
        even = j
        print(f"{j} is an even number")
    else:
        print(f"{j} is not an even number")
        
    even_list.append(even)

even_list1 = list(set(even_list))
even_arr = np.array(even_list1)

print(" ")
print(f"This is the list of even numbers extracted: {even_list1}")
print(" ")
print(f"This is the array of even numbers: {even_arr}")            
    
     
    

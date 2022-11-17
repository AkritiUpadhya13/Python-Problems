# For a given dictionary with numbers from 1-10 as key and their squares as values, creating a for loop to obtain each key value pair.

keys=[]
for i in range(1,11):
    keys.append(i)

values = []
for i in range(1,11):
    values.append(i**2)

square_dict={}
i=0
for i in range(0,10):
    sd={keys[i]:values[i]}
    square_dict.update(sd)
print("For Given Dictionary:",square_dict) 

list_items=list(square_dict.items()) 
for i in range(0,10):
    print(f"Displaying key-value pair of index {i}:",list_items[i])    
     

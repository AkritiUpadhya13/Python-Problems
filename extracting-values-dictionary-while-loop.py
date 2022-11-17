# For a given dictionary with numbers containg first 10 natural numbers as key and their cubes as values.
# Creating a while loop to obtain each key value pair.

keys=[]
for i in range(1,11):
    keys.append(i)

values=[]
for j in range(1,11):
    values.append(j**3)    

cube_dict={}
k=0
while k<10:
    cd={keys[k]:values[k]}
    cube_dict.update(cd)
    k+=1

print("For the given dictionary:",cube_dict)

cube_list_items=list(cube_dict.items())
x=0
while x<10:
    key_value_pair=cube_list_items[x]
    x+=1 
    print(f"The key-value pair {x}:",key_value_pair)   
       
                

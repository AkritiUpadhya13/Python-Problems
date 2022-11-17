# Using while loop, printing even numbers from a list of natural numbers 1-100

nn_list=[]
even_nn_list = []
j=0
for i in range(1,101):
    nn_list.append(i) 

print("For given numbers in list:",nn_list) 
print(" ")
print("Even numbers extracted using while loop:")   
while j<len(nn_list):
    if nn_list[j]%2 == 0:
        print(nn_list[j],end=' ')
    j = j + 1    
         

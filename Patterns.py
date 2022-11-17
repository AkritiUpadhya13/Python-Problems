# A nested loop to print increasing and decreasing pattern

n=int(input("Enter number of rows"))

# Left side increasing pattern
for i in range(n):
    for j in range(i+1):  
        print("*",end=" ")
    print() 
print(" ")
# Left side decreasing pattern    
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")  
    print()
print(' ')
# Right side increasing pattern    
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print() 
print(' ')   
#Right side decreasing pattern 
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
    
     
# A nested loop for printing pyramid pattern 


num= int(input("Enter number of rows:"))

# Pyramid
for i in range(num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print() 
    
print(" ")
# Reversed Pyramid
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,num-1):
        print("*",end=" ")
    for j in range(i,num):
        print("*",end=" ") 
    print() 
    
    
                                   
                 

           

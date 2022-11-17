# Writing a table using a while loop demonstrating the usage of break,continue and pass statements along with if-else statements
N = list(range(0,10000))
print("Get the table of any number less than 10000")
i=0
j=int(input("Enter a number:"))
print(f"Here is the table of {j}:")
while i<len(N): 
    i+=1 
    if i > 0:
        pass    
        if i%j == 0:
          print(N[i])
          continue
        if i == int(str(j)+'1'):
          break    

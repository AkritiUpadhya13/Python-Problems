# Creating Fibonacci sequence using if-else statement


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)    

fibo_list=[]   
n = int(input("Enter a positive integer:"))
if n>0:
    for i in range(0,n):
        fibo_list.append(fibo(i))
    print(f"The Fibonacci sequence for {n} is {fibo_list}")
else:
    print("Input is not a positive integer")            
    

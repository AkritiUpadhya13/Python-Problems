# To check if the given number is a prime number or not

x = int(input('Enter the number:'))

case = False
if x > 1:
    for i in range(2,x):
        if (x % i) == 0:
            print(x, 'is not a prime number')
            break
    else:
        print(x, 'is a prime number')
else:
    print(x,'is not a prime number')        
        

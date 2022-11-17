# To check if the given number is an armstrong number

x = int(input('Enter a number:'))

n = len(str(x))
sum = 0

num = x
while num > 0:
    digit = num % 10
    sum += digit**n
    num //= 10
    
if x == sum:
    print(x, 'is an Armstrong number')
else:
    print(x,'is not an Armstrong number')            

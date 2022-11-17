# Take three user inputs and find the greatest number

x = float(input('Enter first number:'))
y = float(input('Enter second number:'))
z = float(input('Enter third number:'))

if x > y and x > z or x == y > z or x > y == z:
    print(x, 'is the greatest number')
elif y > x and y > z or  x == z < y:
    print(y, 'is the greatest number')
elif z > x and z > y or  x == y < z or y == z > x or x == z > y:
    print(z, 'is the greatest number')
else:
    print('All numbers are equal')
        

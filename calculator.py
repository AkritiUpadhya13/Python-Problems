# Creating a calculator program

def calculate():
    print('Select an Operation')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    
    operation = int(input("Select an operation:"))
    
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
        
    if operation in (1,2,3,4):
        if operation == 1:
            print(x, '+' ,y ,'=' , x+y)
        elif operation == 2:
            print(x, '-' , y, '=' , x-y)
        elif operation == 3:
            print(x,'*', y, '=' , x*y)  
        elif operation ==4:
            if y == 0:
                print('Infinity')
            else:
                print(x, '/', y, '=' , x/y)    
    else:
        print("Invalid Selection")
    again()           
        
def again():
    another=input("Do you want another calculation? (Y/N):")    
    if another == 'Y':
        calculate()
    else:
        print('Thank you!')
                      
calculate()

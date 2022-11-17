# Writing a function to check whether year number is a leap year

def Check_LeapYear():
    Year= int(input("Enter a year:"))
    if Year%4==0:
        print(Year, "is a leap year")
    else:
        print(Year, "is not a leap year")
        
Check_LeapYear()            

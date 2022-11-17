# Extracting vowels using a for loop demonstrating the usage of break,continue and pass statements along with if-else statements


l=[]
import string
for letter in string.ascii_lowercase:
    l.append(letter)

print("Alphabet in lowercase:")    
print(l)
print("Extracted Vowels from alphabet:")
vowels=[]
vowels.append(l[0])
for i in range(len(l)):
    if i >2:
        pass
        if i % 4 == 0:
            vowels.append(l[i])
            continue
        if i > 7:
            break
for i in range(len(l)):        
    if i > 10:
        pass
        if i % 6== 2:
            vowels.append(l[i])
            continue
        if i > 21:
            break    
print(vowels)

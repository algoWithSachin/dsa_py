n  = 123321

# copy the number
num = n 

# result value
result = 0

while num>0 :
    id = num%10 # if 
    result = result*10 + id
    num = num // 10

print(result)
if n == result:
    print(f"Yes!! given number {n} is palindrome number")
else:        
    print(f"Noo! given number {n} is not palindrome number")    
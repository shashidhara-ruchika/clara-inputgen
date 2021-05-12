x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
  
# Swapping using xor 
x = x ^ y 
y = x ^ y 
x = x ^ y 
  
print("Value of x:", x) 
print("Value of y:", y) 
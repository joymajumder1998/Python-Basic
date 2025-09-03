a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

largest = a
if (b > a):
    largest = b
    
lcm = largest

while(lcm <= a*b):
    if (lcm%a == 0 and lcm%b == 0 ):
        break
    lcm += 1
    
print(lcm)

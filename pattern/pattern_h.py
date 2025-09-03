n = int(input("Enter the number on lines : "))

if (n % 2 == 0):
    print("Number of line should odd number.")
    
else:
    result = ""
    for i in range(1, n+1):
        result += "*"
        for j in range( (n-1)//2 ):
            if (i == (n+1)/2 ):
                result += '*'
            else:
                result += " "
        result += "*\n"
        
    print(result)
        
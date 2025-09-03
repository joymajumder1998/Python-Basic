n = int(input("Enter the number of numbers : "))

if (n < 2):
    print("Minimun two numbers required")

else:
    arr = []
    for i in range(n):
        arr.append(int(input("Enter the number : ")))
        
    print("Numbers : ", arr)

    min_lcm = arr[0] # Maximun value of array
    max_lcm = 1
    
    # Calculating max value of array (min_lcm)
    for i in range(1, n):
        if arr[i] > min_lcm:
            min_lcm = arr[i]
    
    # Calculating multiplication of every element of the array (max_lcm)
    for i in range(n):
        max_lcm *= arr[i]
        
    lcm = min_lcm
    while(lcm <= max_lcm):
        is_lcm = True
        for i in range(n):
            if (lcm % arr[i] != 0):
                is_lcm = False
        if (is_lcm == True):
            break
        lcm += 1
    print(lcm)
    
        
# Check all digits of a number even or not
all_even_flag = True
n = int(input("Enber a number : "))
temp = n
while temp > 0:
    digit = temp % 10
    if digit % 2 != 0:
        all_even_flag = False
        break
    temp = temp // 10

if all_even_flag == True:
    print("All number is even")
else:
    print("All number is not even")

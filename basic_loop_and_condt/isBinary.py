n = int(input("Enter a number : "))
is_binary = True
temp = n
while temp > 0:
    digit = temp % 10
    if digit != 0 and digit != 1:
        is_binary = False
        break
    temp //= 10

if is_binary is True:
    print("Number is binary")
else:
    print("Number is not not binary")

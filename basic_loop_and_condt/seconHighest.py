n = int(input("Enter a number  : "))
temp = n
highest = 0
highest_2 = 0

while temp > 0:
    digit = temp % 10
    if digit > highest_2 and digit < highest:
        highest_2 = digit
    if digit > highest:
        highest = digit
    temp //= 10

print(highest_2)

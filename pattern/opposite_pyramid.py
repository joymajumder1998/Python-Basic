"""
*****
 ****
  ***
   **
    *
"""

lines = int(input("Enter the number of lines : "))
result = ""
for i in range(1, lines+1):
	for space in range(lines-i):
		result += " "
	for j in range(1, i+1):
		result += " *"
	result += "\n"
for i in range(1, lines+1):
    for j in range(0, i):
        result += ' '
    
    for j in range(lines - i + 1 ,1, -1):
        result += " *"
    result += '\n'
print(result)

   

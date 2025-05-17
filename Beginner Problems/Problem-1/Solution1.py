string = 'bongodev'

reverse_string = ""

for item in range(len(string)-1, -1, -1):
    reverse_string = reverse_string + string[item]
    
print(reverse_string)

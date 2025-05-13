my_list = [4,8,7,4,3,6,2,1,9]

found = False
for items in my_list:
    if(items == 6):
        found = True
        break
    
if found:
    print("6 is available on the list")
else:
    print("6 is not availabe on the list")
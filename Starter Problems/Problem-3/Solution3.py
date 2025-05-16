def whoiselder(b1,b2):
    if (b1>b2):
        print(f'Brother with the age {b1} is the elder one.')
    elif (b1<b2):
        print(f'Brother with the age {b2} is the elder one.')
    else:
        print("Both of them are of the same age")
        
#input
brother1 = input("Age of brother1 ")
brother2 = input("Age of brother2 ")
whoiselder(brother1,brother2)

#hardcoded values
whoiselder(12,34)
whoiselder(20,20)
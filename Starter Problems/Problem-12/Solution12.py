list1 = [3, 5, 7, 4, 8, 8]

list2 = [4, 9, 8, 7, 1, 1, 13]

commonlist = []

for item1 in list1:
    if item1 in list2 and item1 not in commonlist:
            commonlist.append(item1)

print(sum(commonlist))




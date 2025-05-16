dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}

dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

common_keys = {}

for key in dict1:
    if key in dict2:
        common_keys[key] = (dict1[key],dict2[key])
    
print(common_keys)

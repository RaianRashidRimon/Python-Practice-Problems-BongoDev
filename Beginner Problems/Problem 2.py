string = "Data Science is awesome"

vowel_list = ['a','e','i','o','u']

count = 0

for item1 in string.lower():
    if item1 in vowel_list:
        count += 1
            
print(count)
# output is 10 


# the answer in the problem is given as 9 which is wrong. the test case
# "dAtA scIEncE Is AwEsOmE" has 10 vowels, not 9.
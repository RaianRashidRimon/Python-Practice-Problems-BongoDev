def missingnumber(num):
    n = len(num) + 1 
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(num)
    return expected_sum - actual_sum


numbers = [1, 2, 4, 5]



missing_number = missingnumber(numbers)
print(missing_number)  

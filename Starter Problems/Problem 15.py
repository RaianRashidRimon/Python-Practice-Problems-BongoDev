student_1 = [40, 35, 70, 90, 56]

student_2 = [57, 35, 80, 98, 46]



def passorfail(list):
    for item in list:
        if item < 40:
            print("Your have failed")
            return
        
            
    print("Youre average mark is")
    return print(sum(list)/len(list))
    
passorfail(student_1)
passorfail(student_2)

student_3 = [57, 45, 80, 98, 46]
passorfail(student_3)
def fizzbuzz(a):
    if(a%3==0 and a%5==0):
        print("FizzBuzz")
    elif(a%3==0):
        print("Fizz")
    elif(a%5==0):
        print("Buzz")
    else:
        print("Not Fizz-buzz number")

fizzbuzz(2)
fizzbuzz(6)
fizzbuzz(10)
fizzbuzz(15)
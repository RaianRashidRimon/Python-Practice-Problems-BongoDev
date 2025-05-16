def guess(gnumber):
    if(gnumber==5):
        print("Your guess is correct")
    elif(gnumber<5):
        print("Your guess is almost there")
    else:
        print("Your guess is highter")
        
guess_number = int(input("Enter your guess: "))
guess(guess_number)
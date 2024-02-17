# the guessing game  is the computer guesses the number that the user has in mind
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
while guess != secret_word and guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1
    if guess_count == 3:
        print("You have reached the maximum number of tries")
    elif guess_count < 3:
        print("You have " + str(guess_limit - guess_count) + " tries left")
    else:
        print("You have reached the maximum number of tries")   
        
        
        
num = int (input(" enter a number :"))
if(num %2  ):
    print(" the number is even")

elif(num == 0):
    print("the number is zero")
    
else:
    print(" the number is odd")
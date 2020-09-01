import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

quit = False
range = 100
while not quit:
    random_number = random.randint(1,range)

    number = input("Please guess a number between 1 and {}: ".format(range))
    number = int(number)
    count = 1
    while int(number) != random_number:
        #We can't compare a string "5" with an integer 5, convert one to other

            print("Sorry, that's incorrect.")
            if number > random_number:
                print("You guessed higher than the number")
            if number < random_number:
                print("You guessed lower than the number")
            number = input("Try again! Please guess a number between 1 and {}:".format(range) )
            number = int(number)
            count = count + 1
    print("Congratulations, you got it right in {} tries!".format(count))
    play_again = input("Would you like to play again? ")
    if play_again == "yes" or play_again == "Yes" or play_again == "YES":
        quit = False
    else:
        quit = True
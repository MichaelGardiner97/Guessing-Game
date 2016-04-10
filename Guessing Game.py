# Michael Gardiner
# Due: 10-1-15
# Guessing Game for user

"""
A game will be created where the user has 3 chances to guess a randomly-generated number.
If the user guesses lower than the generated number, s/he will be hinted to guess higher.
If the user guesses higher than the generated number, s/he will be hinted to guess lower.
If the user guesses correctly at any point in the game, s/he will be told s/he won, and asked if s/he would like to play again.
If the user uses all 3 guesses and still does not guess the number, s/he will be told s/he lost, and asked if s/he would like to play again.
If the user enters a number greater than 10, s/he will lose a turn and be returned an error message.

"""

import random
    
def game():    
    #Creating a function that can be called upon to start the guessing game

    #Create a random number between 1 and 10:
    rand_num = random.randint(1,10)
    #Create variables tht will help dictate the game
    tries = 0
    remaining = 3

    #Gives the user 3 tries to guess the right number
    while tries < 3:
        guess = int(input("Please type your guess:    "))
        #Add 1 to tries. Will max out at 3 and end the game. Take 1 away from remaining. Game ends when remaining = 0
        tries += 1
        remaining -= 1

    #Ensure that the user gives a number between 1 and 10:
        if guess > 10 :
            print("ERROR. NUMBER MUST BE BETWEEN 1 AND 10. YOU LOSE A TRY")

        elif guess == rand_num:
            print("CORRECT!!")
            print("IT TOOK YOU", tries, "TRIES")
            #End the game: 
            break 

        elif guess < rand_num:
            #If the the guess is smaller than the number, the user will be hinted their number was too low
            if remaining > 0 :
                print("I'M SORRY, THAT NUMBER WAS LOW. YOU HAVE",remaining,"TRIES REMAINING")
                #Let the user continue the game:
                continue
            else:
                print("SORRY, BUT MY NUMBER WAS:   ",rand_num)
                print("YOU ARE OUT OF TRIES. BETTER LUCK NEXT TIME!")

        elif guess > rand_num:
            #If the the guess is larger than the number, the user will be hinted their number was too high
            if remaining > 0:
                print("I'M SORRY, THAT NUMBER WAS HIGH. YOU HAVE",remaining,"TRIES REMAINING")
                #Let the user continue the game:
                continue
            else:
                print("SORRY, BUT MY NUMBER WAS:   ",rand_num)
                print("YOU ARE OUT OF TRIES. BETTER LUCK NEXT TIME!")

def main():   
    #Explaining the game to the user:
    
    print("WELCOME TO THE GUESSING GAME. YOU WILL HAVE 3 ATTEMPTS AT GUESSING A RANDOM NUMBER BETWEEN 1 AND 10, INCLUSIVE. GOOD LUCK")
    answer = "yes"
    #Setting answer = 'yes' will automatically begin the game for the user after explanation
    
    while answer == "yes":
        game()
        answer = input("WOULD YOU LIKE TO PLAY AGAIN!? YES/NO:   ")
        #After game is over, the user now has the option of changing what answer equals. If yes, game will run again. If no, game quits.
        if answer == "no":
            print("SEE YOU NEXT TIME!")

main()

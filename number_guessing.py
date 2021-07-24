import random
import time

score = 0

print("====================== Hi Folks .. Welcome to Prediction Arena =====================")
print("\n\n-------------------------------Rules for the game--------------------------------")
print("\n\t 1. You are allowed to guess 3 random numbers between 1 and 5")
print("\n\t 2. For wrong guesses clue will be provided and score will be reduced by 5")
print("\n\t 3. Maximum 3 clues")

def random_number(chance):
    '''
    method for generating random number
    '''
    time.sleep(1)
    print("\n\n|\t mmmh..let me select {} random number".format(chance))
    random_number = random.randint(1,5)       #random number between 0 & 100 generating variable
    return random_number

def check_multiple_divisible(number):
    if number%2 == 0:
        return "\n|\t Number divisible by 2"
    else:
        return "\n|\t Number not divisible by 2"

def guess_check(random_number,guessed_number):
    if random_number == guessed_number:
        print("\n\n|\t Hurray!!! You have guessed it right .. You have 5 points")
        global score
        score += 5
        print("Your Current Score:{}".format(score))
        return True

def greater_or_lower(number):
    if number > 1:
        print("\n|\tNumber greater than 1 and less than 4") 

random_first =random_number("1st")
time.sleep(2)
print("\n|\t Yes..Good to go.. Your turn to guess")
print("\n|\t Here is the 1st clue: ")
print(check_multiple_divisible(random_first))
print(random_first)
print("\n|\t Please enter the guess:")
guess_number_one = int(input())


if guess_check(random_first,guess_number_one):
    random_second = random_number("2nd")
    print("\n|\t Here is the 2nd clue: ")
    print(check_multiple_divisible(random_first))
    print(random_second)
    print("\n|\t Please enter the guess:")
    guess_number_two = int(input())
    if guess_check(random_second,guess_number_two):
        random_third = random_number("3rd")
        print("\n|\t Here is the 3rd clue: ")
        print(check_multiple_divisible(random_third))
        print(random_third)
        print("\n|\t Please enter the guess:")
        guess_number_three = int(input())
        if guess_check(random_third,guess_number_three):
            print("You Won")
        else:
            print("\n\n|\t Oopss..Wrong guess..")
            score -= 5
            print("\n|\t Here is the 2nd clue:",greater_or_lower(random_third))
            print("\n|\t Please enter the guess2:")
            print("Your Current Score:{}".format(score))
    else:
        print("\n\n|\t Oopss..Wrong guess..")
        score -= 5
        print("\n|\t Here is the 2nd clue:",greater_or_lower(random_second))
        print("\n|\t Please enter the guess2:")
        print("Your Current Score:{}".format(score))
else:
    print("\n\n|\t Oopss..Wrong guess..")
    score -= 5
    print("\n|\t Here is the 2nd clue:",greater_or_lower(random_first))
    print("\n|\t Please enter the guess2:")
    print("Your Current Score:{}".format(score))


import random
import time

score = 0

print(
    "====================== Hi Folks .. Welcome to Prediction Arena ====================="
)
print(
    "\n\n-------------------------------Rules for the game--------------------------------"
)
print("\n\t 1. You are allowed to guess 3 random numbers between 1 and 5")
print(
    "\n\t 2. For wrong guesses clue will be provided and score will be reduced by 5"
)
print("\n\t 3. Maximum 3 clues")


def random_number(chance):
    '''
    method for generating random number
    '''
    time.sleep(1)
    print("\n\n|\t mmmh..let me select {} random number".format(chance))
    random_number = random.randint(
        1, 5)  #random number between 0 & 100 generating variable
    return random_number


def clues(number):
    '''
    method for generating random clues
    '''
    clue_list = []
    divisible = check_divisible(number)
    clue_list.append(divisible)
    even_odd = check_even_odd(number)
    clue_list.append(even_odd)
    return clue_list

def check_even_odd(number):
    '''
    method for checking whether number
    is even or odd
    '''
    if number % 2 == 0:
        return "\n|\t Number is even"
    else:
        return "\n|\t Number is odd"

def check_divisible(number):
    '''
    method for checking whether number
    is divisible by 2
    '''
    if number % 2 == 0:
        return "\n|\t Number divisible by 2"
    else:
        return "\n|\t Number not divisible by 2"


def guess_check(random_number, guessed_number):
    '''
    method for comparing random number and guessed number
    '''
    if random_number == guessed_number:
        print(
            "\n\n|\t Hurray!!! You have guessed it right .. You have 5 points")
        global score
        score += 5
        print("Your Current Score:{}".format(score))
        return True


def greater_or_lower(number):
    '''
    method for comparing whether the number is 
    greater or lower than limits 
    '''
    if number > 1 and number < 4:
        print("\n|\tNumber greater than 1 and less than 4")
    else:
        print("\n|\tNumber less than 1 and greater than 4")


random_first = random_number("1st")
time.sleep(2)
print("\n|\t Yes..Good to go.. Your turn to guess")
print("\n|\t Here is the 1st clue: ")
print(random.choice(clues(random_first)))
try:
    print("\n|\t Please enter the guess:")
    guess_number_one = int(input())
except ValueError:
    print("|\tInvalid entry .Enter a number only")
    print("|\t Please enter the guess:")
    guess_number_one = int(input())

if not guess_check(random_first, guess_number_one):
    print("\n\n|\t Oopss..Wrong guess..")
    if score > 0:
        score -= 5
    print("\n|\t Here is the 2nd clue:", greater_or_lower(random_first))
    print("\n|\t Please enter the guess2:")
    guess_chance_two = int(input())
    print("Your Current Score:{}".format(score))

random_second = random_number("2nd")
print("\n|\t Here is the 2nd clue: ")
print(random.choice(clues(random_second)))
print("\n|\t Please enter the guess:")
guess_number_two = int(input())

if not guess_check(random_second, guess_number_two):
    print("\n\n|\t Oopss..Wrong guess..")
    if score > 0:
        score -= 5
    print("\n|\t Here is the 2nd clue:", greater_or_lower(random_second))
    print("\n|\t Please enter the guess2:")
    guess_chance_two = int(input())
    print("Your Current Score:{}".format(score))

random_third = random_number("3rd")
print("\n|\t Here is the 3rd clue: ")
print(random.choice(clues(random_third)))
print("\n|\t Please enter the guess:")
guess_number_three = int(input())

if not guess_check(random_third, guess_number_three):
    print("\n\n|\t Oopss..Wrong guess..")
    if score > 0:
        score -= 5
    print("\n|\t Here is the 2nd clue:", greater_or_lower(random_third))
    print("\n|\t Please enter the guess2:")
    guess_chance_two = int(input())
    print("Your Current Score:{}".format(score))

if score > 10:
    print("You Won")
else:
    print("Better luck next time")

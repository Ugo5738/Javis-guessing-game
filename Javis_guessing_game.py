import random

number_limit = 20
minimum_number = 0
random_number = int(number_limit * random.random()) + 1
guess = 0
positive = 'yes'
negative = 'no'
go_back = 'positive'

print("Hi, I am Javis but you can call my Jay")
name = input("What about you? What's your name? ")
question = input(f"Nice to meet you {name}, I'm a little bored, would like you to play a guessing game with me? ")
while go_back != negative:
    random_number = int(number_limit * random.random()) + 2
    if question == positive:
        guess = int(input('Take a guess of a number from 0 to 20, what whole number do you think I am thinking about: '))
        if guess > random_number:
            print('This number is larger than the number I have in mind!')
        elif guess < random_number:
            print('This number is smaller than the number I have in mind!')
        if guess < minimum_number or guess > number_limit:
            print('You have to select a number from 1 to 20')
            go_back = input('Would you like to try again? ')
            if go_back == negative:
                print(f'Okay, thanks {name} for trying. It was nice getting to know you. Have an awesome day!')
                break
        elif guess == random_number:
            go_back = input(f'Cool {name}! You got the number right! Would you like to play again? ')
            if go_back == negative:
                print(f'Okay {name}, thanks for your company. See you later!')
                break
    elif question == negative:
        print(f"Okay, that's fine. it was nice getting to know you {name}. Have a beautiful day!")
        break
    else:
        go_back = input('You have to select either Yes or No: ')
        if go_back == negative:
            print("Bummer! was looking forward to playing with you. Anyways, i'll see you latter")
            break
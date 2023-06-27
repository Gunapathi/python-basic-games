import random

rock = 'rock'
papper = 'papper'
scissors = 'scissors'

def choices(option, user):
    if option == 0:
        print(f'{user} choice is Rock\n')
    elif option == 1:
        print(f'{user} choice is Papper\n')
    else:
        print(f'{user} choice is Scissors\n')

def result(user, comp):
    if (user == comp):
        print('This match is Tie')
    elif (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
        print('You loose')
    elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
        print('You Win')
    else:
        print('Wrong Option, You Loose')

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Papper & 2 for Scissors - '))
choices(user_choice, 'user')

comp_choice = random.randint(0, 2)
choices(comp_choice, 'Computer')

result(user_choice, comp_choice)


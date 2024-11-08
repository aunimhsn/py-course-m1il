from random import randint

difficulty = input('1. Easy 0-10 -- 2. Medium 0-100 -- 3. Hard 0-1000 : ')
levels_allowed = [1, 2, 3]

while difficulty not in levels_allowed:
    difficulty = input('1. Easy 0-10 -- 2. Medium 0-100 -- 3. Hard 0-1000 : ')

maximum = 100

if difficulty == '1':
    maximum = 10
elif difficulty == '2':
    maximum = 100
elif difficulty == '3':
    maximum = 1000

secret:int = randint(0, maximum)
user_input = int(input(f'Veuillez saisir un nombre entre 0 et {maximum} : '))
attempts = 1

while secret != user_input:
    if secret < user_input:
        print('C\'est moins')
    else:
        print('C\'est plus')

    # print('C\'est moins') if secret < user_input else print('C\'est plus')
    
    user_input = int(input(f'Veuillez saisir un nombre entre 0 et {maximum} : '))
    attempts += 1
    
print(f'Bravo, vous avez trouvé le nombre secret {secret} en {attempts} essai.s')

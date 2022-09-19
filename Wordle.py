import random
import math

def startGame():
    wordlist = open('WordList.txt')
    randomwords = []
    for word in wordlist:
        randomwords.append(word.strip())

    answer = random.choice(randomwords).upper()

    def guessletter():
        position = 0
        working_guess = ''
        for letter in user_guess:
            if letter == answer[position]:
                working_guess += 'G'
            elif letter in answer:
                working_guess += 'Y'
            else:
                working_guess += '-' 
            position += 1
        print(working_guess)

    numofguesses = 0
    gotcorrect = False

    while numofguesses <= 6 and gotcorrect == False:
        user_guess = input('Enter your 5-letter guess: ').upper()
        guessletter()
        numofguesses += 1
        
        
        if answer == user_guess and numofguesses == 1:
            print(f'Congratulations! You guessed correctly in {numofguesses} try!')
            break
        elif answer == user_guess and numofguesses < 6:
            print(f'Congratulations! You guessed correctly in {numofguesses} tries!')
            began()
            break
        elif answer == user_guess and numofguesses == 6:
            gotcorrect == True
            print(f'Congratulations! You guessed correctly in {numofguesses} tries!')
            began()
            break
        
        if numofguesses == 6 and gotcorrect == False:
            print(f'Sorry! You got it wrong. The correct answer was {answer}.')
            began()
            break


def began():
    while True:
        began_game = input('Would you like to play Wordle? ').upper()
        if began_game == 'YES':
            startGame()
        elif began_game == 'NO':
            exit()
        else:
            print('Sorry that does not seem right!')
            began_game = input('Would you like to play Wordle? ').upper()
began()

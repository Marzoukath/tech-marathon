import random

num_digit = 3
max_guesse=10


def main():

    print(''' Welcome !!!  Bagels,a deductive logic game.
        I am thinking of a {}-digit number with no repeated digits.
        Try to guess what it is.  Here are some clues: 
        When I say:     That means: 
        Pico            One digit is correct but in the wrong position.
        Fermi           One digit is correct and in the right position.
        Bagels          No digit is correct.''' .format(num_digit))
    while True: 
        secretNum=getSecretNum()
        print('''I have thought up a number.
            You have {} guesses to get it.'''.format(max_guesse))
        numGuesse=1
        
        while numGuesse <= max_guesse:
            guess=''
            while(len(guess)!=num_digit or  not guess.isdecimal):
                # print('Guesse -{}'.format(numGuesses))
                #print("Please, number you guess must have a -{} digits and be decimal( not a string)".format(num_digit))
                guess=input('Guesse {}: '.format(numGuesse))
            clues=getClues(guess, secretNum)
            print(clues)
            numGuesse+=1

            if(guess==secretNum):
                break
            if(numGuesse>max_guesse):
                print(''' You ran out of guesses.
                    The answer was {}.'''.format(secretNum))
        print("Do you want to play again ? (yes or no)")
        if not input().lower().startswith('y'):
            break
    print('Thanks for playing !!!')

def getSecretNum():
    num=list('0123456789')
    random.shuffle(num)
    secretNum=''
    for i in range(num_digit):
        secretNum+=str(num[i])
    return secretNum


def getClues(guess, secretNum):
    if guess==secretNum:
        print("You got it")
        return 'Congratulations'
    else:
        clues=[]
        for i in range (len(guess)):
            if guess[i]==secretNum[i]:
                clues.append('Fermi')
            elif guess[i] in secretNum:
                clues.append('Pico')
        if len(clues)==0:
            return'Bagels'
        else:
            clues.sort()
            return ' '.join(clues)
    
if __name__ == '__main__':
    main()
    



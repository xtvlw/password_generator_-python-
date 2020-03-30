#_[N_F]_

from random import randrange

alphaA = '0123456789'
alphaB = 'abcdefghijklmnopqrstuvwxyz'
alphaC = alphaB.upper()
alphabet = [alphaA, alphaB, alphaC]
final = ''
Length = int(input('len password : '))

for i in range(Length):
    step1 = randrange(0, len(alphabet))
    step2 = alphabet[step1]
    step3 = randrange(0, len(step2))
    final += step2[step3]

print(final)
    

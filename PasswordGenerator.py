#_[N_F]_
import random

alphaA = '0123456789'
alphaB = 'abcdefghijklmnopqrstuvwxyz'
alphaC = alphaB.upper()
alphabet = [alphaA, alphaB, alphaC]
final = ''
L = int(input('len password : '))

for i in range(L):
    P1 = random.randrange(0, len(alphabet))
    L2 = alphabet[P1]
    P2 = random.randrange(0, len(L2))
    final += L2[P2]

print(final)
    
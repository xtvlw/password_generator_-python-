#_[N_F]_
from random import choice


alphaA = "0123456789"
alphaB = "abcdefghijklmnopqrstuvwxyz"
alphaC = alphaB.upper()

characters = [alphaA + alphaB + alphaC]

length = int(input("\nPassword length: "))

password = ""

for l in range(length):
    for c in characters:
        password += choice(c)

print(password)
    

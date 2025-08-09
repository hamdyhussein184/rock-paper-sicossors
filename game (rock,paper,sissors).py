#try git diff
#ask the user to enter his move (r,p,s)
#pc choose move randomly
#player == pc is a tie
#if user choose ("r") and pc choose ("s") or user choose ("p") and pc choose ("r") or user choose ("s") and pc choose ("P") 
#user win / you win
#else 
#pc won / you lost

import random

user = input ("please insert your choise ? :'r' for rock , 'p' for paper , 's' for sissors\n")
pc = random.choice(['r' , 'p' , 's'])

print("you choose :"+user)
print("pc choose :"+pc)

if user==pc :
    print ("it's tie")
elif (user == 'r' and pc == 's' ) or (user == 'p' and pc == 'r') or (user == 's' and pc == 'p') :
    print("you won !")
else :
    print ("you lost !")
print ("the game end")
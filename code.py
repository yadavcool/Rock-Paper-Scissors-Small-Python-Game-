from random import randint
from typing import Any, Union

player=input('rock(r),paper(p) or scissors(s)?')
print(player,'  VS  ',end=' ')
chosen=randint(1,3)
#print(chosen)
if chosen ==  1:
    computer ='r'

elif chosen ==2:
    computer ='p'

else:
    computer= 's'

print(computer)

if player  == computer:
        print('Draw!')
elif player == 'r' and computer =='s':
        print('Player Wins, ____HURRAY____')
elif player == 'r' and computer =='p':
        print('Computer Wins, ____ALAS____')
elif player =='r' and computer=='s':
        print('Player Wins, ____HURRAY YEHH____')
elif player == 'r'  and computer =='p':
        print('Computer Wins, ____LOL____')
elif player  =='p' and computer =='r':
        print('Player Wins, ____HURRAY FUCKING WOW____')
elif player=='p'  and  computer =='s':
        print('Computer Wins, ____LOOLY POP____')
elif player=='s' and computer =='p':
    print('Player Wins, ____I AM DAMM GOOD____')

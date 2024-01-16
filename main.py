from player_create import check
check()
from gameplay import final_wave
print('This is a generic RPG. You need to go through a series of battles known as "Waves". Each wave will have 4 battles, and there are 6 waves. If you die in any battle, you will be sent back to the first battle. When given a prompt for anything, make sure to type it completely correctly with correct capitalization or else it may be marked incorrect. If you want to challenge yourself, you can try to not use the replay command, good luck!')
x=True
while x==True:
    if bool(final_wave())==True:
        x=False
print('Congratulations! You beat the final boss, the Hydra, and beat the game! Hopefully that was somewhat difficult.')
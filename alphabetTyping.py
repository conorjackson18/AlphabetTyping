import time
from datetime import datetime
import msvcrt

#My top time while testing is 2.928s


highscore = ['',200.0]
alphabet='abcdefghijklmnopqrstuvwxyz' #Define the string to be typed.
# alphabet=''
play=True


while play: #The game loop. 
    start = str(input('Press enter to begin countdown'))
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('GO')
    tstart=datetime.now()
    for x in range(len(alphabet)): #Runs through the string, looking for the next character
        correct=False
        print(alphabet[:x])
        while not correct:
            test=str(msvcrt.getch())
            if test == f"b'{alphabet[x]}'":
                correct=True 
                print('\n'*20)
            else:
                correct=False

    tend = datetime.now() #The timing system
    print(alphabet)
    totaltime = tend-tstart
    totaltime = float(f'{totaltime.seconds}.{totaltime.microseconds//1000}')
    print(f'Congrats! You final time is {totaltime} seconds.')

    
    if highscore[1]==200.0: #Setting the new highscore.
        name=str(input('Enter in your name to set the highscore: '))
        highscore = [name,totaltime]
    elif totaltime < highscore[1]:
        name = str(input(f"Highscore! You beat {highscore[0]}'s time of {highscore[1]}s! Enter your name to store your score: "))
        highscore = [name,totaltime]
    else:
        print(f"The current highscore is {highscore[0]}'s time of {highscore[1]}s!")
    
    answered=False
    while not answered: #Asking if they want to play again
        again=input('Do you want to play again? (y/n) ')
        if again.lower() == 'y':
            answered=True
            play=True
        elif again.lower() == 'n':
            answered=True
            play=False
        else:
            print('Incorrect input!')



print(f"Thanks for playing! The fastest time was {highscore[0]}'s time of {highscore[1]}s!")
time.sleep(5)


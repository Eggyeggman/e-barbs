import time
from timeit import Timer
def countdown_Timer(seconds):
    while seconds>0:
        min = int(seconds/60)
        scc=int(seconds%60)
        timer = f'{min}:{scc}'
        print(timer)
        time.sleep(1)
        seconds-=1
    print("timer")
seconds=input("Enter time in seconds")
countdown_Timer(int(seconds))
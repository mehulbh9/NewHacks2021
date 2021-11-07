# import the time module
import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
  
  
# input time in seconds
m = int(input("Enter the number of minutes : "))
s = int(input("Enter the number of seconds : "))
t = m*60 + s
# t = input("Enter the time in seconds : ")
  
# function call
countdown(int(t))

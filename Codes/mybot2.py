#import RPi.GPIO as GPIO
import time
import curses
from gpiozero import Motor
m1=Motor(21,20) # Create our motor, connected to pins GPIO 20 and 21
m2=Motor(12,16)

def forward():
	m1.forward(0.5) # Move forward at half max speed
	m2.forward(0.5)

def backward():
	m1.backward(0.5) # Move forward at half max speed
	m2.backward(0.5)
def left():
	m1.forward(0.5) # Move forward at half max speed
	m2.backward(0.5)

def right():
	m1.backward(0.5) # Move forward at half max speed
	m2.forward(0.5)
def stop():
	m1.stop() # Move forward at half max speed
	m2.stop()
def main():
	
	
	screen = curses.initscr()
	curses.noecho() 
	curses.cbreak()
	screen.keypad(True)
	z=0

	try:


            while True:   
            	char = screen.getch()
                if char == ord('q'):
                    break
                elif char == curses.KEY_UP:
                    print ("up")
                    forward()
                elif char == curses.KEY_DOWN:
                    print ("down")
                    backward()
                elif char == curses.KEY_RIGHT:
                    print ("right")
                    right()
                elif char == curses.KEY_LEFT:
                    print ("left")
                    left()
                elif char == 10:
                    print ("stop") 
                    stop() 

             
	finally:
    #Close down curses properly, inc turn echo back on!
    	 curses.nocbreak(); screen.keypad(0); curses.echo()
    	 curses.endwin
         #GPIO.cleanup()

if __name__=="__main__": 
    main()  

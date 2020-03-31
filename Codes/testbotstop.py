import RPi.GPIO as GPIO
import time
import curses

def forward():
	GPIO.output(7,True)
	GPIO.output(11,False)
	GPIO.output(13,True)
	GPIO.output(15,False)

def backward():
	GPIO.output(7,False)
	GPIO.output(11,True)
	GPIO.output(13,False)
	GPIO.output(15,True)

def left():
	GPIO.output(7,True)
	GPIO.output(11,False)
	GPIO.output(13,False)
	GPIO.output(15,True)

def right():
	GPIO.output(7,False)
	GPIO.output(11,True)
	GPIO.output(13,True)
	GPIO.output(15,False)

def stop():
	GPIO.output(7,False)
	GPIO.output(11,False)
	GPIO.output(13,False)
	GPIO.output(15,False)

def main():
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7,GPIO.OUT)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)

	screen = curses.initscr()
	curses.noecho() 
	curses.cbreak()
	screen.keypad(True)
	z=0

	try:

			
        	
        	while True:   
            	char = screen.getch()
            	
            	if char == curses.KEY_UP:
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
                	
                elif char == ord('q'):
                	
              		break

             
	finally:
    #Close down curses properly, inc turn echo back on!
    	curses.nocbreak(); screen.keypad(0); curses.echo()
    	curses.endwin
    GPIO.cleanup()

if __name__=="__main__": 
    main()  
# import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(32,False)
                GPIO.output(36,True)
                GPIO.output(38,False)
                GPIO.output(40,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(32,True)
                GPIO.output(36,False)
                GPIO.output(38,True)
                GPIO.output(40,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(32,True)
                GPIO.output(36,False)
                GPIO.output(38,False)
                GPIO.output(40,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(32,False)
                GPIO.output(36,True)
                GPIO.output(38,True)
                GPIO.output(40,False)
            elif char == 10:
                GPIO.output(32,False)
                GPIO.output(36,False)
                GPIO.output(38,False)
                GPIO.output(40,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    

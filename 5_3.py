from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

blue = LED(18)
red = LED(27)
green = LED(10)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helverica', size = 14, weight = "bold")

def blueToggle():
    if blue.is_lit:
        blue.off()
        blueButton["text"] = "Turn LED on"
    else:
        red.off()
        green.off()
        blue.on()
        blueButton["text"] = "Turn LED off"
        
def redToggle():
    if red.is_lit:
        red.off()
        redButton["text"] = "Turn LED on"
    else:
        blue.off()
        green.off()
        red.on()
        redButton["text"] = "Turn LED off"
        
def greenToggle():
    if green.is_lit:
        green.off()
        greenButton["text"] = "Turn LED on"
    else:
        red.off()
        blue.off()
        green.on()
        greenButton["text"] = "Turn LED off"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()

blueButton = Button(win, text = 'Turn LED On', font = myFont, command = blueToggle, bg = 'blue', height = 1,  width = 24)
blueButton.grid(row=0,column=0)

redButton = Button(win, text = 'Turn LED On', font = myFont, command = redToggle, bg = 'red', height = 1,  width = 24)
redButton.grid(row=1,column=0)

greenButton = Button(win, text = 'Turn LED On', font = myFont, command = greenToggle, bg = 'green', height = 1,  width = 24)
greenButton.grid(row=2,column=0)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'bisque2', height = 1, width = 6)
exitButton.grid(row=3, column=0)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
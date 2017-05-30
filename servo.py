from Tkinter import *
import RPi.GPIO as GPIO
import os
import tkFont

win = Tk()

min=2.2
max=12.2
mid=7.2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(5)

pwm.ChangeDutyCycle(min)

def min():
	pwm.ChangeDutyCycle(2.2)

def max():
	pwm.ChangeDutyCycle(12.2)

def mid():
	pwm.ChangeDutyCycle(7.2)

def myinput():
        myinput = input.get()
        pwm.ChangeDutyCycle(float(myinput))
	print(float(myinput))

win.title("Servo Control")
win.geometry("800x480")

Label(win, text="text")
input = Entry(win)
input.grid(row=0, column=1)

inputbutton = Button(win, text="Set", command=myinput, height=10, width=15)
inputbutton.grid(row=1, column=1)

minbutton = Button(win, text="Minimum", command=min, height=10, width=15)
minbutton.grid(row=2, column=1)

maxbutton = Button(win, text="Maximum", command=max, height=10, width=15)
maxbutton.grid(row=3, column=1)

midbutton = Button(win, text="Middle", command=mid, height=10, width=15)
midbutton.grid(row=4, column=1)
mainloop()


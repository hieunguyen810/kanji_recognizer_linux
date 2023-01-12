from email.mime import image
from tkinter import *
import tkinter as tk
import pyautogui 
from PIL import ImageTk
from PIL import Image
import os
import cv2
import recognizer
gui = tk.Tk()
# Set the size of the window
gui.geometry("400x400")
screensize = pyautogui.size()
def take_screenshot():
    canvas = Canvas(width=screensize[0], height=screensize[1])
    # detect monitor resolution
    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()
    geometry = str(screen_width) + "x" + str(screen_height)
    gui.geometry(geometry)
    gui.lift()
    gui.attributes("-alpha", 0.5)
    button.pack_forget()
    a = b = c = d = i = 0
    p = process(a, b, c, d, i)
    canvas.bind("<Button-1>", p.callback)
    canvas.pack()
class process: 
    def __init__(self, a, b, c, d, i):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.i = i
    def callback(self, event):
        if self.i == 0:
            self.a = event.x
            self.b = event.y
            self.i+=1
        elif (self.i == 1):
            self.c = event.x
            self.d = event.y
            self.i+=1
            capture(self.a, self.b, self.c, self.d)
def capture(a, b, c, d):
    left = a
    top = b
    if c-a > 0:
        width = c - a
    else: 
        width = a - c
    if d-b > 0:
        height = d - b
    else:
        height = b - d
    if os.path.isfile('my_screenshot.png'):
        os.remove('my_screenshot.png')
    gui.attributes("-alpha", 1)
    pyautogui.screenshot('my_screenshot.png', region=(left, top, width, height))
    img = cv2.imread("my_screenshot.png")
    text = recognizer.predict(img)
    gui.destroy()
    print(text)
    # cv2.imshow('Image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # l = Label(gui, text = text)
    # l.pack()
button = Button(gui, text='Take ScreenShot', command=take_screenshot)
button.pack(padx=10, pady=10)
gui.mainloop()
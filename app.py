""" https://anapioficeandfire.com/"""

import tkinter as tk
import requests

window = tk()
window.geometry("500x500")
window.title("test")

enteruser = Entry(window, font="Arial, 12")
submit_button = Button(window, text="Submit Data", font="Arial, 12", bg="yellow")
testlabel = Label(window, font="Arial, 12")

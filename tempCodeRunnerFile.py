import tkinter as tk

from tkinter import ttk
from tkinter import *
import tkinter.font as font
import requests , json
from PIL import ImageTk, Image


win = tk.Tk()
win.title("PNR Stutas Checker")
win.iconbitmap('icon.ico')

win.resizable(width = True, height = True)
win.config(bg='DARKSALMON')
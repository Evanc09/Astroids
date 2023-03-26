import tkinter as tk
from tkinter import Button
import sys

try:
   from assets.utils2 import main, TWO_player_Free_play
except ImportError as ie:
    print(f"Could not import(E: {ie})")
    
root = tk.Tk()
def menu4(root):
    def destroy(root):
        root.destroy()

    b1=Button(text="normal", command=lambda:[destroy(root), main()])

    testButton = Button(text="Free Play", command=lambda:[destroy(root),TWO_player_Free_play.Free_play() ])
    testButton.pack()
    b1.pack()
    
    root.mainloop()
menu4(root)

#!/usr/bin/env python3
import tkinter as tk # using tkinter as the GUI platform!
"""
This a basic python script that prints the users input in the terminal.
To do this there are two basic functions needed in order to print the text.
The first will be input, it's a built in function in python that allows someone
to enter text through a basic prompt in the temrinal. The second function will
be print, which will print the basic text from the user input into the terminal.
essentially this is an echo function written in python.

With System Calls a person can utilize basic shell scripting with these different
python modules: os, subprocess, sys, shutil, and socket. These would be imported at
the top of the script and used in context of their library.
"""


prompt = input("type anything!: ") # I used basic input for the prompt to allow the user to type anything, hence "type anything!".
print(f"\n\n{prompt}\n\n") # new lines are needed to help make the presentation of the input fasionable to the screen. I would go in and use tkinter as a way of expressing the user input more artistically. But, that would go beyond the assighnments expectations :)

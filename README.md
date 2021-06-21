# todo-popups

I was supposed to write my thesis, so I wasted valuable time writing this code that is supposed to help me write my thesis:

```
todos = [
  "Write your first todo here (e.g. write thesis section 1)",
  "Write your second todo here (e.g. create figure for section 1)",
  "etc."
]

from tkinter import *
import tkinter.messagebox

def message(msg):
	root=Tk() 
	root.geometry("1x0")
	tkinter.messagebox.showinfo('To do',msg)
	root.destroy()

def iterate_todos(todos):
	for todo in todos:
		root = message(todo)

iterate_todos(todos)

```

So, open a terminal, enter `python3`, copy-paste this piece of code and write a thesis!

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

def message(title, msg):
	try:
		root=Tk() 
		root.geometry("1x0")
		tkinter.messagebox.showinfo(title, msg)
		destroyed = False
		while not destroyed:
			try:
				root.destroy()
			except tkinter.TclError:
				destroyed = True
	except KeyboardInterrupt:
		return 0
	return 1
		

def do(todos):
	todos_left = [todo for todo in todos]
	if len(todos):
		for i, todo in enumerate(todos):
			keep_em_coming = message(f"To do ({i+1}/{len(todos)})", todo)
			if not keep_em_coming:
				break
			todos_left.remove(todo)
	return todos_left

todos = do(todos)

```

So, open a terminal, enter `python3`, copy-paste this piece of code and write a thesis!

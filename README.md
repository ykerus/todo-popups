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
		root = Tk() 
		root.geometry("1x0")
		user_response = tkinter.messagebox.askquestion(title, msg)
		destroyed = False
		while not destroyed:
			try:
				root.destroy()
			except tkinter.TclError:
				destroyed = True
	except KeyboardInterrupt:
		return -1
	if user_response == "no":
		return 0
	return 1

def do(todos):	
	i = 0
	tot_todos = len(todos)
	todos_left = [todo for todo in todos]
	skipped = [False for todo in todos]
	while len(todos_left) > 0:
		user_response = message(f"To do ({i+1}/{tot_todos})", todos[i])
		if user_response == -1:
			break
		elif user_response == 0:
			if len(todos) == 1:
				continue
			j = i+1
			all_skipped = False
			while skipped[j]:
				j += 1
				if j > tot_todos-1:
					all_skipped = True
					break
			todos_copy = [todo for todo in todos]
			if all_skipped:
				append_todo = todos[i]
				todos.remove(append_todo)
				todos.append(append_todo)
				skipped[-1] = True
			else:
				todos[j] = todos[i]
				todos[i] = todos_copy[j]
				skipped[j] = True
		else:
			todos_left.remove(todos[i])
			i += 1
	return todos

todos = do(todos)

```

So, open a terminal, enter `python3`, copy-paste this piece of code and write a thesis!

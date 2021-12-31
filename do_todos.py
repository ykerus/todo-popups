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
		pbar = 30
		space_eq_diff = 2.35
		msg_title = f"To do  ["
		msg_title += "=" * round((i+1)/tot_todos * pbar)
		msg_title += " " * round(space_eq_diff*(pbar-round((i+1)/tot_todos * pbar)))
		user_response = message(msg_title + f"]   {i+1}/{tot_todos}", todos[i])
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

def read_todos(dir="todos.txt"):
	with open(dir) as f:
		temp = f.read()
	todos = temp.split(";;")
	todos = [todo.strip() for todo in todos]
	return todos

def main():
	todos = read_todos()
	todos = do(todos)

if __name__ == "__main__":
	main()

import tkinter.messagebox
import tkinter as tk
from tkinter import *
def print_window():
	window=tk.Tk()
	window.title('test')
	window.geometry('400x400')
	Label(window,text="tip1:*****").grid(row=0,column=0)
	Label(window,text="Your word: ").grid(row=1,column=0)
	e = Entry(window)
	e.grid(row=1,column=1)
	theButton1 = Button(window,text = '确定',command = result)
	theButton2 = Button(window,text = '取消',command = exit)

	theButton1.grid(row = 2,column = 0)
	theButton2.grid(row = 2,column = 1)
	tk.mainloop()
def exit():
	window.destroy()
def result():
	st = e.get()
	if eval(st) == 5:
		tk.messagebox.showinfo(title = 'Correct!',message = 'You are nb')
	else:
		tk.messagebox.showinfo(title = 'Incorrect!',message = 'You are cb')
	window.destroy()
def hit():
    #box系列
    #tk.messagebox.showinfo(title='hi',message='so this is a msgbox')
    #tk.messagebox.showwarning(title='warning', message='so this is a warningbox')
    #tk.messagebox.showerror(title='hi', message='No! the program is about to crash!')
 
    #ask系列
    #tk.messagebox.askquestion(title='hi', message='Are you sure to cancel it?') #返回'yes'或'no'
    #tk.messagebox.askyesno(title='hi', message='Are you sure to cancel it?')  #返回True或者False

    tk.messagebox.askquestion(title='hi', message='Are you sure to cancel it?') 



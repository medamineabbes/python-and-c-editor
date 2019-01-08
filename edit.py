from tkinter import Tk,ttk,Text
import subprocess
import os
window= Tk() # the main window
path_pointer=""
language=""
name=""
path=""
##########  run and save buttons and the text field  #################
run=ttk.Button(window,text="Run")  # run the code
save=ttk.Button(window,text="Save") # save the code
text_to_run=Text(window) #the text field
Home=ttk.Button(window,text="Home")#Go back to the home inteface
Back=ttk.Button(window,text="Back")#Go back to the privious interface
#############################################
c_button=ttk.Button(window,text="C") # chose the language c
python_button=ttk.Button(window,text="Python") #chose the language python
path_capter=ttk.Entry(window)
ok=ttk.Button(window,text="OK")   # creat a new file or open one 
################## functions for the buttons ###################
################################################################
def c_faction():
	c_button.pack_forget()
	python_button.pack_forget()
	path_capter.pack()
	ok.pack()
	Back.pack()
	global language
	language="C"
def python_function():
	c_button.pack_forget()
	python_button.pack_forget()
	path_capter.pack()
	ok.pack()
	Back.pack()
	global language
	langage="Python"
def ok_function():
	if path_capter.get() !="":
		global name
		global path
		global path_pointer
		text_to_run.delete('1.0','end-1c')
		path=""
		name=""
		path_pointer=path_capter.get()
		while os.getcwd()!="/home/amine/Desktop":
			os.chdir("..")
		i=len(path_pointer)-1
		if "/"in path_pointer:
			while(path_pointer[i]!="/"):
				i-=1
		for j in range(0,i):
			path+=path_pointer[j]
		for j in range(i+1,len(path_pointer)):
			name+=path_pointer[j]
		os.chdir(path)
		ok.pack_forget()
		path_capter.pack_forget()
		Back.pack_forget()
		os.system("touch "+ name)
		f=open(name,"r")
		s=""
		for a in f:
			s+=a
		f.close()
		text_to_run.insert('1.0',s)
		text_to_run.pack()
		run.pack()
		save.pack()
		Home.pack()
def save_fanction():
	saving=open(name,"w")
	saving.write(text_to_run.get("1.0",'end-1c'))
	saving.close()
##########python runing bug ################
def run_function():
	save_fanction()
	global name
	global language
	if language=="C":
		try:
			os.system("gcc " + name + " -o " + "abcd")
			os.system("gnome-terminal -- ./abcd")
		except:
			os.system("gcc " + name + " -lgraph -o " + "abcd")
			os.system("gnome-terminal -- ./abcd")
	else:
		os.system("gnome-terminal -- python3 " + name)	
def home():
	run.pack_forget()
	save.pack_forget()
	text_to_run.pack_forget()
	Home.pack_forget()
	c_button.pack()
	python_button.pack()
def go_back():
	path_capter.pack_forget()
	ok.pack_forget()
	Back.pack_forget()
	c_button.pack()
	python_button.pack()
###########################################
ok.config(command=ok_function)
python_button.config(command=python_function)
c_button.config(command=c_faction)
save.config(command=save_fanction)
run.config(command=run_function)
Home.config(command=home)
Back.config(command=go_back)
##########################################
c_button.pack()
python_button.pack()
window.mainloop()
while(1):
   input()
from tkinter import *
from tkinter import filedialog
import subprocess
def Main():
  global Main, Text
  Main = Tk()
  Text = Text(Main, font=("Consolas", 12), fg="black", width=150, height=60)
  Text.pack()
  menuBar=Menu(Main)  
  Main.config(menu=menuBar)
  Main.geometry("800x600")
  Main.title("Notepad")
  try:
    Main.iconbitmap(r'C:\Users\gabec\Downloads\Notepad.ico')
  except:
    print("Image not found")
  fileMenu= Menu(menuBar, tearoff=0)  
  fileMenu.add_command(label="New", command=New)
  fileMenu.add_command(label="New Window", command=New_Win)
  fileMenu.add_command(label="Open...", command=Open)
  fileMenu.add_command(label="Save", command=Save)
  fileMenu.add_command(label="Save As...", command=Save_As)
  fileMenu.add_separator()
  fileMenu.add_command(label="Page Setup")
  fileMenu.add_command(label="Print...")
  fileMenu.add_separator()
  fileMenu.add_command(label="Exit", command=Quit)
  editMenu= Menu(menuBar, tearoff=0)
  editMenu.add_command(label="Undo") 
  editMenu.add_separator()
  editMenu.add_command(label="Cut")
  editMenu.add_command(label="Copy")
  editMenu.add_command(label="Paste")
  editMenu.add_command(label="Delete")
  editMenu.add_separator()
  editMenu.add_command(label="Select All")
  editMenu.add_command(label="Time/Date")
  formatMenu = Menu(menuBar, tearoff=0)  
  formatMenu.add_checkbutton(label="Word Wrap")
  formatMenu.add_command(label="Font...")
  viewMenu = Menu(menuBar, tearoff=0)
  zoomMenu = Menu(menuBar, tearoff=0)
  viewMenu.add_cascade(label="Zoom", menu=zoomMenu)
  viewMenu.add_checkbutton(label="Status Bar")
  menuBar.add_cascade(label="File", menu=fileMenu)
  menuBar.add_cascade(label="Edit", menu=editMenu)
  menuBar.add_cascade(label="Format", menu=formatMenu)
  menuBar.add_cascade(label="View", menu=viewMenu)
  Main.mainloop()
def Quit():
  Main.destroy()
def New():
  Text.delete(1.0,END)
def Write():
  #global file
  # opens file in write mode
  file = open(Main.filename, "w")
  file.write(Box)
  # closes the file
  file.close()
def New_Win():
  subprocess.Popen('python notepad.py', shell=False)
def Save():
  global Box
  Box = Text.get(1.0, "end-1c")
  Box = str(Box)
  Write()
def Save_As():
      Main.filename = filedialog.askopenfilename(initialdir=".", title="Save As", filetypes=(("Text Documents(*.txt)", "*.txt"), ("All Files(*.*)", "*.*")))
      Save()
def Read():
  # reads file back and prints to Result
  try:
    file = open(Main.filename, "r")
  except:
    print("File failed to open")
  New()
  Text.insert(END, file.read())
  file.close()
def Open():
  Main.filename = filedialog.askopenfilename(initialdir=".", title="Open File", filetypes=(("Text Documents(*.txt)", "*.txt"), ("All Files(*.*)", "*.*")))
  Read()
Main()

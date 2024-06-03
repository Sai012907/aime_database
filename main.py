from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
from PIL import *
from tkinter import messagebox

problems = [['AIME1983_1.png'],['AIME1984_1.png'],['AIME1985_1.png'],['AIME1986_1.png'],['AIME1987_1.png'],['AIME1988_1.png'],['AIME1989_1.png'],['AIME1990_1.png'],['AIME1991_1.png'],['AIME1992_1.png'],['AIME1993_1.png'],['AIME1994_1.png'],['AIME1995_1.png'],['AIME1996_1.png'],['AIME1997_1.png'],['AIME1998_1.png'],['AIME1999_1.png']]
answers = [[60,15],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

global tries
tries = 3

global string
string = 0
  
def submit(answer, n, k, tries):
	
    string = answer.get()
    tries = tries - 1
    if (tries != 0):
      if (int(string) == answers[n-1983][k-1]):
        messagebox.showinfo("CORRECT", "CORRECT")
      elif (int(string) != answers[n-1983][k-1]):
        messagebox.showinfo("INCORRECT", "INCORRECT, YOU HAVE " + str(tries) + " TRIES LEFT!")
    else:
      messagebox.showinfo("BAD", "YOU HAVE NO TRIES LEFT!")

def openNewNewWindow(newWindow, n, k):
	
  newNewWindow = Tk()
  newNewWindow.title("AIME {year} Problem {number}".format(year = n, number = k))
  newNewWindow.geometry("1000x800")
  newWindow.destroy()

  canvas = Canvas(newNewWindow, width = 1000, height = 300)      
  canvas.pack()
  img = PhotoImage(file=problems[n-1983][k-1])      
  canvas.create_image(20,20, anchor=NW, image=img)
  
  answer = tk.Entry(newNewWindow)
  answer.pack()

  
  if tries != 0:
    submitbutton = Button(newNewWindow, text='SUBMIT', fg="purple", command=lambda:submit(answer, n, k, tries))
    submitbutton.pack()
  else:
    submit(answer, n, k, 0)
  button_go_back_1 = tk.Button(newNewWindow, text="GO BACK", fg="purple", command=open_root)
  button_go_back_1.pack()
  
  newNewWindow.mainloop()     

def openNewWindow(root, n):

  newWindow = Tk()
  newWindow.title("AIME {year}".format(year = n))
  newWindow.geometry("800x1000")
  root.destroy()

  button_go_back_0 = tk.Button(newWindow, text="GO BACK", fg="purple", command=open_root)
  button_go_back_0.place(x = 360, y = 200)

  button_1 = tk.Button(newWindow, text="Problem 1", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 1))
  button_1.place(x = 90, y = 50)
  
  button_2 = tk.Button(newWindow, text="Problem 2", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 2))
  button_2.place(x = 210, y = 50)

  button_3 = tk.Button(newWindow, text="Problem 3", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 3))
  button_3.place(x = 330, y = 50)

  button_4 = tk.Button(newWindow, text="Problem 4", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 4))
  button_4.place(x = 450, y = 50)

  button_5 = tk.Button(newWindow, text="Problem 5", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 5))
  button_5.place(x = 570, y = 50)

  button_6 = tk.Button(newWindow, text="Problem 6", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 6))
  button_6.place(x = 90, y = 90)

  button_7 = tk.Button(newWindow, text="Problem 7", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 7))
  button_7.place(x = 210, y = 90)

  button_8 = tk.Button(newWindow, text="Problem 8", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 8))
  button_8.place(x = 330, y = 90)

  button_9 = tk.Button(newWindow, text="Problem 9", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 9))
  button_9.place(x = 450, y = 90)

  button_10 = tk.Button(newWindow, text="Problem 10", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 10))
  button_10.place(x = 570, y = 90)

  button_11 = tk.Button(newWindow, text="Problem 11", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 11))
  button_11.place(x = 90, y = 130)

  button_12 = tk.Button(newWindow, text="Problem 12", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 12))
  button_12.place(x = 210, y = 130)

  button_13 = tk.Button(newWindow, text="Problem 13", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 13))
  button_13.place(x = 330, y = 130)

  button_14 = tk.Button(newWindow, text="Problem 14", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 14))
  button_14.place(x = 450, y = 130)

  button_15 = tk.Button(newWindow, text="Problem 15", fg="purple", command=lambda:openNewNewWindow(newWindow, n, 15))
  button_15.place(x = 570, y = 130)


def open_root():
  root = Tk()
  root.title("AIME PROBLEMS")
  root.geometry("800x1000")

  welcome = Text(root)
  welcome.tag_configure("tag_name", justify='center')
  welcome.insert("1.0", "Please pick a year. You have three tries to attempt any given problem.")
  welcome.tag_add("tag_name", "1.0", "end")
  welcome.pack()

  button_1983 = tk.Button(root, text="1983", fg="purple", command=lambda:openNewWindow(root,1983))
  button_1983.place(x = 90, y = 50)
  button_1984 = tk.Button(root, text="1984", fg="purple", command=lambda:openNewWindow(root,1984))
  button_1984.place(x = 160, y = 50)
  button_1985 = tk.Button(root, text="1985", fg="purple", command=lambda:openNewWindow(root,1985))
  button_1985.place(x = 230, y = 50)
  button_1986 = tk.Button(root, text="1986", fg="purple", command=lambda:openNewWindow(root,1986))
  button_1986.place(x = 300, y = 50)
  button_1987 = tk.Button(root, text="1987", fg="purple", command=lambda:openNewWindow(root,1987))
  button_1987.place(x = 370, y = 50)
  button_1988 = tk.Button(root, text="1988", fg="purple", command=lambda:openNewWindow(root,1988))
  button_1988.place(x = 440, y = 50)
  button_1989 = tk.Button(root, text="1989", fg="purple", command=lambda:openNewWindow(root,1989))
  button_1989.place(x = 510, y = 50)
  button_1990 = tk.Button(root, text="1990", fg="purple", command=lambda:openNewWindow(root,1990))
  button_1990.place(x = 580, y = 50)
  button_1991 = tk.Button(root, text="1991", fg="purple", command=lambda:openNewWindow(root,1991))
  button_1991.place(x = 650, y = 50)
  button_1992 = tk.Button(root, text="1992", fg="purple", command=lambda:openNewWindow(root,1992))
  button_1992.place(x = 90, y = 90)
  button_1993 = tk.Button(root, text="1993", fg="purple", command=lambda:openNewWindow(root,1993))
  button_1993.place(x = 160, y = 90)
  button_1994 = tk.Button(root, text="1994", fg="purple", command=lambda:openNewWindow(root,1994))
  button_1994.place(x = 230, y = 90)
  button_1995 = tk.Button(root, text="1995", fg="purple", command=lambda:openNewWindow(root,1995))
  button_1995.place(x = 300, y = 90)
  button_1996 = tk.Button(root, text="1996", fg="purple", command=lambda:openNewWindow(root,1996))
  button_1996.place(x = 370, y = 90)
  button_1997 = tk.Button(root, text="1997", fg="purple", command=lambda:openNewWindow(root,1997))
  button_1997.place(x = 440, y = 90)
  button_1998 = tk.Button(root, text="1998", fg="purple", command=lambda:openNewWindow(root,1998))
  button_1998.place(x = 510, y = 90)
  button_1999 = tk.Button(root, text="1999", fg="purple", command=lambda:openNewWindow(root,1999))
  button_1999.place(x = 580, y = 90)

  root.mainloop()

open_root()

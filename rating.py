from tkinter import *
from tkinter import messagebox


def selection():
    f = open("rating.txt", "a")
    f.write(str(radio.get())+'\n')
    f.close()
    messagebox.showinfo("Thank You", "Thank You For Your Rating")
    top.destroy()
    import feedback


top = Tk()
top.title("Ratings")
top.iconbitmap("star.ico")
top.geometry("300x150")
radio = IntVar()
lbl = Label(text="Rate Our Experience")
lbl.pack()
R1 = Radiobutton(top, text="Very Dissatisfied", variable=radio, value=1,
                 command=selection)
R1.pack(anchor=W)

R2 = Radiobutton(top, text="Dissatisfied", variable=radio, value=2,
                 command=selection)
R2.pack(anchor=W)

R3 = Radiobutton(top, text="Good", variable=radio, value=3,
                 command=selection)
R3.pack(anchor=W)

R4 = Radiobutton(top, text="Very Good", variable=radio, value=4,
                 command=selection)
R4.pack(anchor=W)

R5 = Radiobutton(top, text="Excellent", variable=radio, value=5,
                 command=selection)
R5.pack(anchor=W)


label = Label(top)
label.pack()
top.mainloop()
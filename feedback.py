from tkinter import *
from tkinter import messagebox

root1 = Tk()
root1.geometry("500x280+550+210")
root1.title("Feedback Form")

name_inp = StringVar()
feedback_inp = StringVar()


def destroy():
    root1.destroy()


def sbt():
    f = open("feedback.txt", "a")
    f.write(str(name_inp.get()) + '\n')
    f.write(str(feedback_inp.get()) + '\n' + '\n')
    f.close()
    messagebox.showinfo("Thank You", "Thank You For Your feedback")
    root1.destroy()
    import burger


customer_name = Label(root1, font=('arial', 16, 'bold'), text="Customer's Name", bd=16, anchor='w')
customer_name.place(x=0, y=1)

txt_name = Entry(root1, font=('arial', 16, 'bold'), textvariable=name_inp, bd=10, insertwidth=4, bg="powder blue", justify ='right')
txt_name.place(x=210, y=8)

feedback = Label(root1, font=('arial', 16, 'bold'), text="Feedback", bd=16, anchor='w')
feedback.place(x=0, y=70)

txt_feedback = Entry(root1, font=('arial', 16, 'bold'), textvariable=feedback_inp, bd=10, insertwidth=4, bg="powder blue", justify ='right')
txt_feedback.place(x=210, y=78)

pop = Label(root1, font=('arial', 12, 'bold'), text="*Please provide feedback for improving us.", bd=16, anchor='w')
pop.place(x=60, y=120)

cnf_btn = Button(root1, text="Submit", command=sbt, cursor="hand2", bg="#0b1335", fg="white",
                 font=("default", 28))
cnf_btn.place(x=80, y=180)

cnl_btn = Button(root1, text="Cancel", command=destroy, cursor="hand2", bg="#0b1335", fg="white",
                 font=("default", 28))
cnl_btn.place(x=260, y=180)

root1.mainloop()
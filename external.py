from tkinter import *
from tkinter import messagebox

root1 = Tk()
root1.geometry("620x720+430+40")
root1.title("Payment Interface")


def cash():
    root1.destroy()
    import cashpg


def paytm():
    root1.destroy()
    import ptmpg


def gpay():
    root1.destroy()
    import gpaypg


def card():
    root1.destroy()
    import cardpg


def cancel():
    root1.destroy()
    import burger


label = Label(root1, font=('arial', 50, 'bold'), text="        Payment", fg="steel blue", bd=10, anchor='w')
label.grid(row=1)

label1 = Label(root1, text="Select Your Payment Choice", bg="#d3ede6", font=("cooper black", 22))
label1.place(x=120, y=100)

ptm_btn = Button(root1, text="Paytm", command=paytm, cursor="hand2", bg="#0b1335", fg="white", font=("default", 28))
ptm_btn.place(x=235, y=160)


gpay_btn = Button(root1, text="Google Pay", command=gpay, cursor="hand2", bg="#0b1335", fg="white", font=("default", 28))
gpay_btn.place(x=190, y=270)

card_btn = Button(root1, text="Debit Cards", command=card, cursor="hand2", bg="#0b1335", fg="white", font=("default", 28))
card_btn.place(x=190, y=380)

cash_btn = Button(root1, text="Cash On Delivery", command=cash, cursor="hand2", bg="#0b1335", fg="white", font=("default", 28))
cash_btn.place(x=150, y=490)

cnl_btn = Button(root1, text="Cancel", command=cancel, cursor="hand2", bg="#0b1335", fg="white", font=("default", 28))
cnl_btn.place(x=220, y=600)


root1.mainloop()

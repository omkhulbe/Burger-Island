from tkinter import *
from tkinter import messagebox

root1 = Tk()
root1.geometry("410x720+550+40")
root1.title("Payment Interface")

upiid_inp = StringVar()


def cnf():
    if upiid_inp.get() == "":
        messagebox.showerror("Error", "Please Enter A UPI ID \nOR\nPlease Enter UPI ID For Verification If Paid By Barcode")
    else:
        messagebox.showinfo("Success", "If Delivery: Your Order will be Delivered In Next 30 Minutes\nIf Pickup: You Can Pickup Your Order In Next 30 Minutes")
        messagebox.showinfo("Thank You", "Thank You For Placing Your Order")
        root1.destroy()
        import rating


def destroy():
    root1.destroy()
    import external


root1.mainf1 = Frame(root1, height=312, width=316)
root1.logo = PhotoImage(file="gpay.png")
root1.l = Label(root1.mainf1, image=root1.logo)
root1.l.place(x=40, y=260)
root1.mainf1.pack(fill=BOTH, expand=1)

cnf_btn = Button(root1, text="Confirm", command=cnf, cursor="hand2", bg="#0b1335", fg="white",
                 font=("default", 28))
cnf_btn.place(x=120, y=120)

or_number = Label(root1, font=('arial', 16, 'bold'), text="OR", bd=16, anchor='w')
or_number.place(x=160, y=200)

pop_number = Label(root1, font=('arial', 8, 'bold'), text="*Click On Confirm After Successfully Payment On Google Pay By Barcode", bd=10, anchor='w')
pop_number.place(x=0, y=575)


customer_number = Label(root1, font=('arial', 16, 'bold'), text="UPI ID", bd=16, anchor='w')
customer_number.place(x=150, y=1)

txt_customer = Entry(root1, font=('arial', 16, 'bold'), textvariable=upiid_inp, bd=10, insertwidth=4, bg="powder blue", justify ='right')
txt_customer.place(x=70, y=50)

cnl_btn = Button(root1, text="Cancel", command=destroy, cursor="hand2", bg="#0b1335", fg="white",
                 font=("default", 28))
cnl_btn.place(x=120, y=620)

root1.mainloop()

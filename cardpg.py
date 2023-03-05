from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("920x380+300+200")
root.title("Payment Interface")

cardno_inp = StringVar()
validity_inp = StringVar()
cvv_inp = StringVar()
name_inp = StringVar()


def destroy():
    root.destroy()
    import external


def sbt():
    if card_name == "" and validity_inp == "" and cvv_inp == "":
        messagebox.showerror("Error", "Please Enter Card Details")
    else:
        messagebox.showinfo("Success", "If Delivery: Your Order will be Delivered In Next 30 Minutes\nIf Pickup: You Can Pickup Your Order In Next 30 Minutes")
        messagebox.showinfo("Thank You", "Thank For Your Order")
        root.destroy()
        import rating


card_number = Label(root, font=('arial', 16, 'bold'), text="Card No.", bd=16, anchor='w')
card_number.place(x=0, y=1)

txt_card = Entry(root, font=('arial', 16, 'bold'), textvariable=cardno_inp, bd=10, insertwidth=4, bg="powder blue", justify ='right')
txt_card.place(x=110, y=8)

validity_number = Label(root, font=('arial', 16, 'bold'), text="Valid Through", bd=16, anchor='w')
validity_number.place(x=450, y=1)

txt_validity = Entry(root, font=('arial', 16, 'bold'), textvariable=validity_inp, bd=10, insertwidth=4, bg="powder blue", justify ='right')
txt_validity.place(x=610, y=8)

cvv_number = Label(root, font=('arial', 16, 'bold'), text="CVV", bd=16, anchor='w')
cvv_number.place(x=20, y=100)

txt_cvv = Entry(root, font=('arial', 16, 'bold'), textvariable=cvv_inp, bd=10, insertwidth=4, bg="powder blue", justify ='right')
txt_cvv.place(x=110, y=100)

card_name = Label(root, font=('arial', 16, 'bold'), text="Card Holder's Name", bd=16, anchor='w')
card_name.place(x=390, y=100)

txt_name = Entry(root, font=('arial', 16, 'bold'), textvariable=name_inp, bd=10, insertwidth=4, bg="powder blue", justify ='right')
txt_name.place(x=610, y=100)

cnf_btn = Button(root, text="Submit", command=sbt, cursor="hand2", bg="#0b1335", fg="white",
                 font=("default", 28))
cnf_btn.place(x=260, y=220)

cnl_btn = Button(root, text="Cancel", command=destroy, cursor="hand2", bg="#0b1335", fg="white",
                 font=("default", 28))
cnl_btn.place(x=520, y=220)

powered = Label(root, font=('arial', 16, 'bold'), text="Powered By Visa, Master Card, RuPay, Discover", bd=16, anchor='w')
powered.place(x=200, y=320)

root.mainloop()
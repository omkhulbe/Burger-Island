from tkinter import *
from tkinter import messagebox

root1 = Tk()
root1.geometry("420x320+550+210")
root1.title("Payment Interface")


def cnf():
    messagebox.showinfo("Success", "If Delivery: Your Order will be Delivered In Next 30 Minutes\nIf Pickup: You Can Pickup Your Order In Next 30 Minutes")
    messagebox.showinfo("Thank You", "Thank For Placing Your Order")
    root1.destroy()
    import rating


def destroy():
    root1.destroy()
    import external


cnf_btn = Button(root1, text="Confirm Now", command=cnf, cursor="hand2", bg="#0b1335", fg="white",
                 font=("default", 28))
cnf_btn.place(x=80, y=60)

cnl_btn = Button(root1, text="Cancel", command=destroy, cursor="hand2", bg="#0b1335", fg="white",
                 font=("default", 28))
cnl_btn.place(x=125, y=180)

root1.mainloop()

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x600+300+200')
frame1 = tk.Frame(root, bg='gray', borderwidth=0, height=450, width=500, pady=30, bd=5, relief="solid")
frame1.pack_propagate(False)
label1 = tk.Label(frame1, text='Contact Us', font=('Arial', 15, 'bold'), bg='#464a47', fg='black', width=40)
first_name = tk.Label(frame1, text='First Name', font=('Arial', 10, 'normal'), bg='gray')
entry1 = tk.Entry(frame1)
last_name = tk.Label(frame1, text='Last Name', font=('Arial', 10, 'normal'), bg='gray')
entry2 = tk.Entry(frame1)
email = tk.Label(frame1, text='Email', font=('Arial', 10, 'normal'), bg='gray')
entry3 = tk.Entry(frame1)
website = tk.Label(frame1, text='Website', font=('Arial', 10, 'normal'), bg='gray')
entry4 = tk.Entry(frame1)
password = tk.Label(frame1, text='Password', font=('Arial', 10, 'normal'), bg='gray')
entry5 = tk.Entry(frame1)
password_confirm = tk.Label(frame1, text='Password Confirmation', font=('Arial', 10, 'normal'), bg='gray')
entry6 = tk.Entry(frame1)
button1 = tk.Button(frame1, text='Sing up', font=('Arial', 10, 'normal'))

frame1.pack()
label1.place(x=0, y=0)
first_name.place(x=30, y=50)
entry1.place(x=30, y=70)
last_name.place(x=30, y=90)
entry2.place(x=30, y=110)
email.place(x=30, y=130)
entry3.place(x=30, y=150)
website.place(x=30, y=170)
entry4.place(x=30, y=190)
password.place(x=30, y=210)
entry5.place(x=30, y=230)
password_confirm.place(x=30, y=250)
entry6.place(x=30, y=270)
button1.place(x=30, y=320)

root.mainloop()
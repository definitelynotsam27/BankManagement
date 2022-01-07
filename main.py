from tkinter import *
from tkinter import messagebox
#data
clientName = ['Dhiru Ram', 'Bharadwaj Pranav', 'Samar Pratap', 'Rodri Martinez', 'Kevin de Bruyne', 'Younis Khan', 'Idris Alba']
clientPins = ['0001','0002', '0003','0004','0005','0006','0007']
clientBalances = [7000,9000,10000,20000,150150010,250000,25250020]
clientDeposition = 0
clientWithdrawal = 0
clientBalance=0
#data


root = Tk()
root.geometry='700x700'

#new account window

def clients():

   new2 = Toplevel(root)
   new2.geometry("750x250")
   new2.title("CLient Details")




def account():
   global u
   u = 0
   global disk1
   disk1 = 1
   global disk2
   disk2 = len(clientName)
   new = Toplevel(root)
   new.geometry("750x500")
   new.title("New Account")

   label1 = Label(new, text="New client account", font=('Helvetica 17 bold'))
   label2 = Label(new, text="Please enter the name of client")
   name_entry = Entry(new,  font=('calibre', 10, 'normal'), width = 60)
   #name=name_entry.get()
   label3 = Label(new, text="Please enter a PIN to secure your account")
   pin_entry = Entry(new,  font=('calibre', 10, 'normal'), width = 60)
   #pin=pin_entry.get()
   label4 = Label(new, text="Please enter the amount of Money you wish to Deposit to start an Account")
   amount_entry = Entry(new,  font=('calibre', 10, 'normal'), width = 60)
   amount_entry.insert(0, 0)
   #amount=int(amount_entry.get())
   def value(a, b, c):
      x = a.get()
      y = b.get()
      z = int(c.get())
      clientName.append(x)
      clientPins.append(y)
      clientBalances.append(z)


   def passer():
      n = value(name_entry, pin_entry, amount_entry)
   def msg1():
      messagebox.showinfo("alert", "Your account details have been successfully entered")
   submitbutton= Button(new, text="Submit", command=lambda:[passer(), msg1()])










   label1.pack(padx = 30)
   label2.pack(pady=30)
   name_entry.pack()
   label3.pack(pady=30)
   pin_entry.pack()
   label4.pack(pady=30)
   amount_entry.pack()
   submitbutton.pack()


#withdraw money window

def withdraw():
   new2 = Toplevel(root)
   new2.geometry("750x500")
   new2.title("Withdraw money")

   label1 = Label(new2, text="Withdraw money from your account", font=('Helvetica 17 bold'))
   label1.pack(padx = 30)


   ####################################################

   wlabel1 = Label(new2, text="Please enter the name of client")
   wname_entry = Entry(new2, font=('calibre', 10, 'normal'), width=60)
   wlabel2 = Label(new2, text="Please enter your PIN here")
   wpin_entry = Entry(new2, font=('calibre', 10, 'normal'), width=60)
   def wsubmit(a, b):
      wcounter = 0
      for i in range(len(clientName)):
         if clientName[i]==a and clientPins[i]==b:
            messagebox.showinfo("hey", "howdy")
            wcounter +=1
      if wcounter < 1:
         messagebox.showerror("warning", "the client details don't match! please ensure that both the name and pin are correctly entered")
   wsubmitbutton= Button(new2, text = 'submit', command=lambda:wsubmit(wname_entry.get(), wpin_entry.get()))











   wlabel1.pack(pady = 30)
   wname_entry.pack()
   wlabel2.pack(pady = 30)
   wpin_entry.pack()
   wsubmitbutton.pack(pady= 30)



#deposit money window

def deposit():
   new = Toplevel(root)
   new.geometry("750x250")
   new.title("New Window")

   label1 = Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold'))
   label1.pack(padx = 30)

#check balance window

def balance():
   new = Toplevel(root)
   new.geometry("750x250")
   new.title("New Window")

   label1 = Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold'))
   label1.pack(padx = 30)


#loan window

def loan():
   new = Toplevel(root)
   new.geometry("750x250")
   new.title("New Window")

   label1 = Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold'))
   label1.pack(padx = 30)

#loan status window

def loans():
   new = Toplevel(root)
   new.geometry("750x250")
   new.title("New Window")

   label1 = Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold'))
   label1.pack(padx = 30)




#main buttons here


titlelabel = Label(root, text = "Welcome to PES banking system", font = ("Helvetica 17 bold", 30))
titlelabel.grid(row = 0, column = 1, pady = 20, padx = 10)
#button1
newaccount = Button(root, text = "Open a new client account", font = ("Helvetica 17 bold", 10), height = 5, command = account)
newaccount.grid(row = 1, column = 0,  pady = 20)
#button2
withdraw = Button(root, text = "Withdraw money from your account", font = ("Helvetica 17 bold", 10), height = 5, command = withdraw)
withdraw.grid(row = 1, column = 1,  pady = 20)
#button3
deposit = Button(root, text = "Deposit money in your account", font = ("Helvetica 17 bold", 10), height = 5, command = deposit)
deposit.grid(row = 1, column = 2, pady = 20)
#button4
checkbalance = Button(root, text = "Check your account balance", font = ("Helvetica 17 bold", 10), height = 5, width = 30, command = balance)
checkbalance.grid(row = 2, column = 0, padx = 70, pady = 20)
#button5
loan = Button(root, text = "loan window", font = ("Helvetica 17 bold", 10), height = 5, width = 30, command = loan)
loan.grid(row = 2, column = 1, padx = 70, pady = 20)
#button6
loanstatus = Button(root, text = "Check your loan status", font = ("Helvetica 17 bold", 10), height = 5, width = 30, command = loans)
loanstatus.grid(row = 2, column = 2,  pady = 20)
#button7
quitbank = Button(root, text = "Quit", font = ("Helvetica 17 bold", 10), height = 5, width = 30)
quitbank.grid(row = 3, column = 1, padx = 70, pady = 50)








root.mainloop()


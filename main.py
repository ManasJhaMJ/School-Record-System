import tkinter as tk
from tkinter import *
from tkinter import ttk
from csv import DictWriter
import os
from tkinter import messagebox

#creating the main window

root = Tk()
root.title('School Record System')
root.geometry("700x650")
root.configure(bg="light green")

#creating  labels

label_head = tk.Label(root,text='School Record System\n',bg='light green')
label_head.config(font=("courier",30))
label_head.grid(row=0,column=0)

label_1 = tk.Label(root,text='   ',bg='light green')
label_1.config(font=("courier",30))
label_1.grid(row=8,column=0)

label_2 = tk.Label(root,text='Select User Type :\n',bg='light green')
label_2.config(font=("courier",15))
label_2.grid(row=47,column=0)

label_3 = tk.Label(root,text='\n\nSelect Theme Colour :\n',bg='light green')
label_3.config(font=("courier",15))
label_3.grid(row=49,column=0)

label1 = tk.Label(root,text="Enter Your Name :\n",bg='light green')
label1.config(font=("courier",15))
label1.grid(row=2,column=0,sticky=tk.W)

label2 = tk.Label(root,text="Enter Your Class :\n",bg='light green')
label2.config(font=("courier",15))
label2.grid(row=3,column=0,sticky=tk.W)

label3 = tk.Label(root,text="Enter Your Transport :\n",bg='light green')
label3.config(font=("courier",15))
label3.grid(row=4,column=0,sticky=tk.W)

label4 = tk.Label(root,text="Select Your gender :\n",bg='light green')
label4.config(font=("courier",15))
label4.grid(row=5,column=0,sticky=tk.W)

label5 = tk.Label(root,text="Enter your Addmission No. :\n",bg='light green')
label5.config(font=("courier",15))
label5.grid(row=6,column=0,sticky=tk.W)

label6 = tk.Label(root,text="Select your age :\n",bg='light green')
label6.config(font=("courier",15))
label6.grid(row=7,column=0,sticky=tk.W)

#  Creating Entry box

entrybox_1_var = tk.StringVar()
entrybox_1 = ttk.Entry(root, width = 16, textvariable = entrybox_1_var)
entrybox_1.grid(row=2,column=1,sticky=tk.W)
entrybox_1.focus()

entrybox_2_var = tk.StringVar()
entrybox_2 = ttk.Entry(root, width = 16, textvariable = entrybox_2_var)
entrybox_2.grid(row=3,column=1,sticky=tk.W)

entrybox_3_var = tk.StringVar()
entrybox_3 = ttk.Entry(root, width = 16, textvariable = entrybox_3_var)
entrybox_3.grid(row=4,column=1,sticky=tk.W)

entrybox_4_var = tk.StringVar()
entrybox_4 = ttk.Entry(root, width = 16, textvariable = entrybox_4_var)
entrybox_4.grid(row=6,column=1,sticky=tk.W)

#creating combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root,width=13, textvariable = gender_var, state='readonly')
gender_combobox['values']= ('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=5,column=1)

# creating radio button 

usertype = StringVar() 
radio_btn1 = tk.Radiobutton(root,text='Student',value='Student',variable=usertype)
radio_btn1.grid(row=47,column=1)

radio_btn2 = tk.Radiobutton(root,text='Teacher',value='Teacher',variable=usertype)
radio_btn2.grid(row=47,column=2)

radio_btn1.configure(background='light green')
radio_btn2.configure(background='light green')

#creating check button
checkvar = IntVar()
check_btn = tk.Checkbutton(root,text='check if you want to Subscribe to our newsletter',variable=checkvar)
check_btn.configure(background='light green')
check_btn.grid(row=48, columnspan=3)

#spinbox(number widget)

spin1 = Spinbox(root,from_=0 , to=100 , width=6)
spin1.grid(row=7,column=1)

#functions  

def action():
    user_name = entrybox_1_var.get() 
    user_Class = entrybox_2_var.get()
    user_trans = entrybox_3_var.get()
    gender_vari = gender_var.get()
    user_type = usertype.get()
    add_no = entrybox_4_var.get()
    spin1_var = spin1.get()
    if checkvar.get()==0:
        Subscribed = 'No'
    else:
        Subscribed = 'yes'

    res=messagebox.askyesno('warning','Warning!\nYour data will be saved in a third party database\n'
                                      'Are you sure you want to continue?')
    if res==True:
        messagebox.showinfo('Message','Record added Sucessfully\nThank You')  ###creating message box

### writing to csv file

        with open("st_records.csv",'a', newline='') as f:
            dict_writer = DictWriter(f, fieldnames=['Name','Class','Transport','Gender','Add No','Age','User type',
                                                    'subscribed'])

            if os.stat("st_records.csv").st_size==0: ###checks if file contains the header or not
                DictWriter.writeheader(dict_writer)
    
            dict_writer.writerow({'Name': user_name,'Class': user_Class, 'Transport': user_trans,
                                  'Gender': gender_vari,'Add No': add_no,'Age' : spin1_var,
                                  'User type': user_type,'subscribed':Subscribed })

                    
        
        name =  entrybox_1.delete(0,tk.END)
        age = entrybox_2.delete(0,tk.END)
        Class = entrybox_3.delete(0,tk.END)
       # label1.configure(foreground='light green')

    else:
        print("form not submitted")

def on_enter(e):
   submit_btn.config(background='red', foreground= "black")

def on_leave(e):
   submit_btn.config(background= 'SystemButtonFace', foreground= 'black')

#configuring the theme of other elements

def changeColor(color): 
    root.configure(background =color)
    choice1.configure(background =color)
    check_btn.configure(background=color)
    radio_btn1.configure(background=color)
    radio_btn2.configure(background=color)
    label1.configure(background=color)
    label2.configure(background=color)
    label3.configure(background=color)
    label4.configure(background=color)
    label_1.configure(background=color)
    label_2.configure(background=color)
    label_head.configure(background=color)
    label_3.configure(background=color)
    label5.configure(background=color)
    label6.configure(background=color)
    
    
    choice2.configure(background =color)
    
 
v =StringVar()
v.set("L")

#theme radio-butttons

choice1 =Radiobutton(root, text ="light green", value =1, variable =v, command =lambda: changeColor("light green"))
choice1.grid(row =49, column =2) 
 
choice2 =Radiobutton(root, text ="light blue", value =2, variable =v, command =lambda: changeColor("light blue"))
choice2.grid(row =49, column =1)

choice1.configure(background ='light green')
choice2.configure(background ='light green')


#creating button
submit_btn = tk.Button(root,text='SUBMIT', command= action)
submit_btn.grid(row=50,columnspan=3)
submit_btn.bind('<Enter>', on_enter)
submit_btn.bind('<Leave>', on_leave)


root.mainloop()
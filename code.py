from tkinter import *

from tkinter import ttk

from tkinter import messagebox

import pickle

import os

from datetime import date

 

 

def login_command():

    global login_root

    global username_entry1

    global password_entry1

    global bill_flag

    global emp_flag

    global acc_flag

    global home_flag

   

    login_root=Tk()

    login_root.geometry('200x200')

    login_root.title('Login')

 

    username_label1=Label(login_root,text='USERNAME:')

    username_label1.grid(row=0,column=0)

    passowrd_label1=Label(login_root,text='PASSWORD:')

    passowrd_label1.grid(row=1,column=0)

 

    username_entry1=Entry(login_root)

    username_entry1.grid(row=0,column=1,columnspan=3)

    password_entry1=Entry(login_root,show="*")

    password_entry1.grid(row=1,column=1,columnspan=3)

 

    newuser_label=Label(login_root,text="New to this app?").grid(row=4,column=0)

    login_button=Button(login_root,text='LOGIN',command=ID_check).grid(row=2,column=0)

    create_button=Button(login_root,text='Create',command=ID_create,relief=SUNKEN,bd=0,fg='blue',cursor="hand2").grid(row=4,column=1)   

 

   

    bill_flag=0

    emp_flag=0

    acc_flag=0

    home_flag=0

 

def ID_create():

    global username_entry2

    global password_entry2

    global create_root

    global phone_entry2

    global shopname_entry2

    global emailID_entry2

    global address_entry2

   

    create_root=Tk()

    create_root.geometry("200x200")

    create_root.title('Create Account')

    username_label2=Label(create_root,text='Username:').grid(row=0,column=0)

    passowrd_label2=Label(create_root,text='Password:').grid(row=1,column=0)

    phone_label2=Label(create_root,text='Phone No:').grid(row=2,column=0)

    shopname_label2=Label(create_root,text='Shop Name').grid(row=3,column=0)

    emailID_label2=Label(create_root,text='Email ID:').grid(row=4,column=0)

    address_label2=Label(create_root,text='Address:').grid(row=5,column=0)

   

    username_entry2=Entry(create_root)

    username_entry2.grid(row=0,column=1,columnspan=3)

    password_entry2=Entry(create_root)

    password_entry2.grid(row=1,column=1,columnspan=3)

    phone_entry2=Entry(create_root)

    phone_entry2.grid(row=2,column=1,columnspan=3)

    shopname_entry2=Entry(create_root)

    shopname_entry2.grid(row=3,column=1,columnspan=3)

    emailID_entry2=Entry(create_root)

    emailID_entry2.grid(row=4,column=1,columnspan=3)

    address_entry2=Entry(create_root)

    address_entry2.grid(row=5,column=1,columnspan=3)

    save=Button(create_root,text="Save",command=save1)

    save.grid(row=6,column=0)

 

def save1():

    global save_flag

    f=open("userpass.bin","rb")

    save_flag=0

    while True:

        try:              

            rec = pickle.load(f)

            if rec['username']==username_entry2.get():

                save_flag=1

                messagebox.showinfo("ERROR","Username already in use",icon="warning")

        except EOFError:break

    if save_flag==0:

        f=open("userpass.bin","ab")

        username_info=str(username_entry2.get())

        phone_info=str(phone_entry2.get())

        password_info=str(password_entry2.get())

        shopname_info=str(shopname_entry2.get())

        emailID_info=str(emailID_entry2.get())

        address_info=str(address_entry2.get())

        dictionary={'username':username_info,'password':password_info,'phone':phone_info,'shopname':shopname_info,'emailID':emailID_info,'address':address_info}

        pickle.dump(dictionary,f)

        f.close()

        f=open('username/'+username_info+'.bin',"ab")

        f.close()

        f=open('bill/'+username_info+'.bin','ab')

        f.close()

        create_root.destroy()

 

   

def ID_check():

    global delete_message

    global modify_message

    global button_frame

    global username_info

    global shop_info

    global phone_info

    global email_info

    global mroot

    global login_root

    global shop_heading

    global phone_heading

    global email_heading

    global frame_heading

   

    flag=0

    username_info=str(username_entry1.get())

    f=open("userpass.bin","rb")

    while True:

        try:              

            rec = pickle.load(f)

            if username_entry1.get()==rec['username'] and password_entry1.get()==rec['password']:

                flag=1

                login_root.destroy()

                mroot=Tk()

                mroot.state("zoomed")

                #mroot.geometry("1366x768")

                mroot.title('Shop Manager')

 

                mroot.configure(bg="#E74C3C")

                username_info=rec["username"]

                shop_info=rec['shopname']

                phone_info=rec['phone']

                email_info=rec['emailID']

 

 

                frame_heading=LabelFrame(mroot,relief=SUNKEN,bd=4,bg="#F7DC6F")

                frame_heading.pack(side=TOP,fill="x")

 

                button_frame=LabelFrame(mroot,text="Options",relief=SUNKEN,bd=4,font=("Helvetica","15"),bg="#EDBB99")

                button_frame.pack(side=LEFT,fill="y")

                shop_heading=Label(frame_heading,text=shop_info,font=("Helvetica","50"),fg="#154360",bg="#F7DC6F")

                shop_heading.pack()

                phone_heading=Label(frame_heading,text=phone_info,font=("Helvetica","12"),fg="#154360",bg="#F7DC6F")

                phone_heading.pack()

                email_heading=Label(frame_heading,text=email_info,font=("Helvetica","12"),fg="#154360",bg="#F7DC6F")

                email_heading.pack()

                home=Button(button_frame,text="Home",bd=3,width=15,command=home_command,font=("Times","15"),bg="#AED6F1",fg="#154360")

                home.grid(row=2,column=0,pady=3)

                bill=Button(button_frame,text="Bill",bd=3,width=15,command=bill_command,font=("Times","15"),bg="#AED6F1",fg="#154360")

                bill.grid(row=3,column=0,pady=3)

                emp=Button(button_frame,text="Employee",bd=3,width=15,command=emp_command,font=("Times","15"),bg="#AED6F1",fg="#154360")

                emp.grid(row=4,column=0,pady=3)

                account_button=Button(button_frame,text="Acc Details",command=acc_command,bd=3,width=15,font=("Times","15"),bg="#AED6F1",fg="#154360")

                account_button.grid(row=5,column=0,pady=3)

                quit_button=Button(button_frame,text="Quit",bd=3,width=15,command=quit_command,font=("Times","15"),bg="#AED6F1",fg="#154360")

                quit_button.grid(row=6,column=0,pady=3)

                home_command()

         #dummy labels

                list_box=Label(mroot)

               

 

        except EOFError:break

    f.close()

    if flag==0:

        messagebox.showinfo("ERROR","Username and Password invalid",icon="warning")

login_command()

   

def home_command():

    global emp_flag

    global bill_flag

    global acc_flag

    global home_flag

    global wel_label

    global home_name_label

    global contact_us_label

    global costomer_care_label

 

   

    if home_flag==1:

        wel_label.destroy()

        home_name_label.destroy()

        contact_us_label.destroy()

        costomer_care_label.destroy()

        home_flag=0

       

    home_flag=1  

    if bill_flag==1:

        bill_frame.destroy()

        bill_flag=0

   

    if emp_flag==1:

        mynotebook2.destroy()

        emp_flag=0

    if acc_flag==1:

        acc_frame.destroy()

        acc_flag=0       

 

    wel_label=Label(mroot,text="Welcome,",bg="#E74C3C",font=("Helvetica","80"))

    wel_label.pack(anchor=NW)

    home_name_label=Label(mroot,text=username_info,bg="#E74C3C",font=("Helvetica","80"))

    home_name_label.pack()

    contact_us_label=Label(mroot,text="Contact us: antoherty@gmail.com ",bg="#E74C3C",font=("Helvetica","15"))

    contact_us_label.pack(side=BOTTOM,anchor=SE)

    costomer_care_label=Label(mroot,text="Customer Care: 1800 250 678 ",bg="#E74C3C",font=("Helvetica","15"))

    costomer_care_label.pack(side=BOTTOM,anchor=SE)

   

def bill_command():

    global emp_flag

    global bill_flag

    global acc_flag

    global home_flag

    global bill_frame

    global product_entry

    global cost_entry

    global quantity_entry

    global bill_list_box

    global total_cost

    global cart_x

    global total_flag

    global bill_number_entry

    global cust_name_entry

    global contact_number_entry

    global cust_name_label

    global phone_label

    global billnumber_label

    global date_label

    global bill_list

    global add_cart_button

    global clear1_button

    global total_button

    global generate_button

    global clear2_button

    global remove_button

    global bill_search_button

   

    if bill_flag==1:

        bill_frame.destroy()

        bill_flag=0

    bill_flag=1

   

    if home_flag==1:

        wel_label.destroy()

        home_name_label.destroy()

        contact_us_label.destroy()

        costomer_care_label.destroy()

        home_flag=0

       

    if emp_flag==1:

        mynotebook2.destroy()

        emp_flag=0

    if acc_flag==1:

        acc_frame.destroy()

        acc_flag=0       

    

    bill_frame=Frame(mroot,bd=10,bg="yellow")

    bill_frame.pack(fill="both")

 

    # customer details

    custdetails_frame=LabelFrame(bill_frame,text="Customer Details",bg="yellow",font=("Helvetica","10"))

    custdetails_frame.pack(fill=X,expand=1)

    bill_number_label=Label(custdetails_frame,text="  Bill Number: ",bg="yellow",font=("Times","13"))

    bill_number_label.grid(row=0,column=1,pady=12)

    bill_search_button=Button(custdetails_frame,text="Search",width=10,bg="red",fg="white",font=("Times","10"),command=bill_search_command)

    bill_search_button.grid(row=0,column=3,padx=5)

    bill_number_entry=Entry(custdetails_frame,width=23,justify="center",font=("Times","13"))

    bill_number_entry.grid(row=0,column=2,pady=10)

 

    cust_name_label=Label(custdetails_frame,text="   Customer Name: ",bg="yellow",font=("Times","13"))

    cust_name_label.grid(row=0,column=5,pady=12)

    cust_name_entry=Entry(custdetails_frame,width=25,justify="center",font=("Times","13"))

    cust_name_entry.grid(row=0,column=6,pady=10)

 

 

    contact_number_label=Label(custdetails_frame,text="   Contact Number: ",bg="yellow",font=("Times","13"))

    contact_number_label.grid(row=0,column=7,pady=12)

    contact_number_entry=Entry(custdetails_frame,width=23,justify="center",font=("Times","13"))

    contact_number_entry.grid(row=0,column=8,pady=10)

 

    #product

    product_frame=LabelFrame(bill_frame,text="Product",bg="yellow",font=("Helvetica","10"))

    product_frame.pack(side="left",fill=Y)

 

    Label(product_frame,text=" ",bg="yellow").grid(row=0,column=0,pady=6)

    product_label=Label(product_frame,text="    Product",bg="yellow",font=("Times","13"))

    product_label.grid(row=1,column=0,columnspan=10)

    product_entry=Entry(product_frame,font=("Times","13"),width=45)

    product_entry.grid(row=2,column=0,columnspan=100,padx=16)

 

    Label(product_frame,text=" ",bg="yellow").grid(row=3,column=0,pady=1)

    quantity_label=Label(product_frame,text=" Quantity",bg="yellow",font=("Times","13"))

    quantity_label.grid(row=4,column=0,columnspan=10)

    quantity_entry=Entry(product_frame,font=("Times","13"),width=45)

    quantity_entry.grid(row=5,column=0,columnspan=100)

 

    Label(product_frame,text=" ",bg="yellow").grid(row=6,column=0,pady=1)

    cost_label=Label(product_frame,text="Cost",bg="yellow",font=("Times","13"))

    cost_label.grid(row=7,column=0,columnspan=10)

    cost_entry=Entry(product_frame,font=("Times","13"),width=45)

    cost_entry.grid(row=8,column=0,columnspan=100)

 

    Label(product_frame,text="      ",bg="yellow").grid(row=9,column=0,pady=15)

    Label(product_frame,text="",bg="yellow").grid(row=10,column=0,columnspan=5)

    add_cart_button=Button(product_frame,text="Add To Cart",width=20,bg="red",fg="white",font=("Times","10"),command=add_cart_command)

    add_cart_button.grid(row=10,column=6,columnspan=15)

    #remove_button=Button(product_frame,text="Remove",width=15,bg="red",fg="white",font=("Times","10"),command=remove_command)

    #remove_button.grid(row=10,column=23,columnspan=15)

    Label(product_frame,text="",bg="yellow").grid(row=10,column=25,padx=40)

    clear1_button=Button(product_frame,text="Clear",width=20,bg="red",fg="white",font=("Times","10"),command=product_clear_command)

    clear1_button.grid(row=10,column=40,columnspan=15)

    Label(product_frame,text="",bg="yellow").grid(row=42,column=0,pady=3)

    Label(product_frame,text="",bg="yellow").grid(row=45,column=0)

   

    #bill window

    bill_window_frame=LabelFrame(bill_frame,text="Bill Window",bg="#F39C12",font=("Helvetica","10"))

    bill_window_frame.pack(side=LEFT,fill=Y)

 

    # variables

    total_cost=0

    cart_x=0

    total_flag=0

    bill_list=[]

   

    f=open("userpass.bin","rb")

    while True:

        try:              

            rec = pickle.load(f)

            if rec['username']==username_info:

                bill_shopname=Label(bill_window_frame,text=rec['shopname'],bg="#F39C12",font=("Helvetica","12"))

                bill_shopname.pack()

                bill_address=Label(bill_window_frame,text=rec['address'],bg="#F39C12",font=("Helvetica","12"))

                bill_address.pack()

                bill_phone=Label(bill_window_frame,text="Mobile: "+rec['phone'],bg="#F39C12",font=("Helvetica","12"))

                bill_phone.pack()

                bill_mail=Label(bill_window_frame,text="Mail: "+rec['emailID'],bg="#F39C12",font=("Helvetica","12"))

                bill_mail.pack()

        except EOFError:break

    f.close()

 

    cust_name_label=Label(bill_window_frame,text='Customer Details: ',bg="#F39C12",font=("Helvetica","12"))

    cust_name_label.pack(anchor=W)

    phone_label=Label(bill_window_frame,text='Phone Number:',bg="#F39C12",font=("Helvetica","12"))

    phone_label.pack(anchor=W)

    billnumber_label=Label(bill_window_frame,text='Bill Number:',bg="#F39C12",font=("Helvetica","12"))

    billnumber_label.pack(anchor=W)

    date_label=Label(bill_window_frame,text='Date:',bg="#F39C12",font=("Helvetica","12"))

    date_label.pack(anchor=W)

    Label(bill_window_frame,text="_______________________________________________________________________________________________",bg="#F39C12",font=("Helvetica","12")).pack(anchor=W)

    Label(bill_window_frame,text="Product                                                               Quantity                                                                   Cost",bg="#F39C12",font=("Helvetica","12")).pack(anchor=W)

    bill_listbox_frame=Frame(bill_window_frame,bg="#F39C12",bd=2)

    bill_listbox_frame.pack()

    bill_scrlbary=Scrollbar(bill_listbox_frame,orient="vertical")

    bill_scrlbarx=Scrollbar(bill_listbox_frame,orient="horizontal")

    bill_list_box=Listbox(bill_listbox_frame,width=100,height=25,bg="#F39C12",bd=0,highlightthickness=0,yscrollcommand=bill_scrlbary.set,xscrollcommand=bill_scrlbarx.set,font=("Helvetica","12"))

    bill_scrlbary.config(command=bill_list_box.yview)

    bill_scrlbary.pack(side=RIGHT,fill=Y)

    bill_scrlbarx.config(command=bill_list_box.xview)

    bill_scrlbarx.pack(side=BOTTOM,fill=X)

   

    bill_list_box.pack()

    d=Scrollbar(bill_list_box)

   

    Label(bill_frame,text="Select the item",font=("Helvetica","10"),bg="yellow").pack()

    Label(bill_frame,text="then click on ",font=("Helvetica","10"),bg="yellow").pack()

    Label(bill_frame,text="Delete button",font=("Helvetica","10"),bg="yellow").pack()

 

    delete_button=Button(bill_frame,text="Delete",width=15,bg="red",fg="white",font=("Times","13"))

    delete_button.pack()

   

    

    #bill options

    bill_options_frame=LabelFrame(product_frame,text="Bill Options",bg="yellow",font=("Helvetica","10"))

    bill_options_frame.grid(row=70,column=0,columnspan=1000)

 

    Label(bill_options_frame,text="",bg="yellow").grid(row=0,column=0,padx=10)

    total_button=Button(bill_options_frame,text="Total",width=15,bg="red",fg="white",font=("Times","10"),command=total)

    total_button.grid(row=0,column=6,padx=5)

    generate_button=Button(bill_options_frame,text="Generate",width=15,bg="red",fg="white",font=("Times","10"),command=generate)

    generate_button.grid(row=0,column=23,padx=5)

    clear2_button=Button(bill_options_frame,text="Clear",width=15,bg="red",fg="white",font=("Times","10"),command=bill_command)

    clear2_button.grid(row=0,column=40,padx=5)

    Label(bill_options_frame,text="",bg="yellow").grid(row=0,column=50,padx=10)                     

    remove_button=Button(bill_options_frame,text="Remove",width=15,bg="red",fg="white",font=("Times","10"),command=remove_command)

    remove_button.grid(row=1,column=23,padx=5,pady=3)

 

   

def add_cart_command():

    global total_cost

    global cart_x

    global bill_list

    product_info=str(product_entry.get())

    n_product=len(product_info)

    #print(cart_x)

    try:

        cost_info=int(cost_entry.get())

        quantity_info=int(quantity_entry.get())

        n_quantity=len(quantity_entry.get())

        total_cost=total_cost+(cost_info*quantity_info)

        bill_list_box.insert(cart_x,product_info+" "*(80-(2*n_product))+str(quantity_info)+" "*(80-(2*n_quantity))+str(cost_info))

        cart_x+=1

        l=[product_info,quantity_info,cost_info]

        bill_list.append(l)

    except ValueError:

        messagebox.showinfo("ERROR","Cost and Quantity has to be an integer",icon="warning")

   

def product_clear_command():

    product_entry.delete(0,END)

    cost_entry.delete(0,END)

    quantity_entry.delete(0,END)

 

   

def remove_command():

    global total_cost

    global bill_list

    a=str(bill_list_box.get(ANCHOR))                         

    quantity_delete_info=""

    cost_delete_info=""

    product_delete_info=""

    for x in range(0,35):

        try:

            if a[65+x].isnumeric()==True:

                quantity_delete_info=quantity_delete_info+str(a[65+x])

        except IndexError:break

    cost_delete_info=""

    for x in range(0,70):

        try:

            if a[130+x].isnumeric()==True:

                cost_delete_info=cost_delete_info+str(a[130+x])

        except IndexError:break

    for x in range(0,40):

        try:

            if a[x].isalpha()==True or a[x].isnumeric==True:

                product_delete_info=product_delete_info+str(a[x])

        except IndexError:break

    total_cost=total_cost-(int(quantity_delete_info)*int(cost_delete_info))

    bill_list_box.delete(ANCHOR)

    for list in bill_list:

        print([product_delete_info,quantity_delete_info,cost_delete_info])

        if list[0]==product_delete_info and str(list[1])==quantity_delete_info and str(list[2])==cost_delete_info:

            bill_list.remove(list)

            break

 

def total():

    global total_flag

    total_flag=1

    bill_list_box.insert(END,"                                                                                                                                                        Total: "+str(total_cost))

 

   

def generate():

    global bill_number_entry

    global cust_name_entry

    global contact_number_entry

    global cust_name_label

    global phone_label

    global billnumber_label

    global date_label

    global bill_list

    global total_cost

    today = date.today()

    bill_number_info=str(bill_number_entry.get())

    cust_name_info=str(cust_name_entry.get())   

    contact_number_info=str(contact_number_entry.get())

    cust_name_label.config(text='Customer Details: '+cust_name_info)

    phone_label.config(text='Phone Number:     '+contact_number_info)

    billnumber_label.config(text='Bill Number:    '+bill_number_info)

    date_label.config(text='Date: '+str(today))

    messagebox.showinfo("GENERATED","Bill generated",icon="info")

    f=open('bill/'+username_info+'.bin','ab')

    d={"bil no":bill_number_info,"cust name":cust_name_info,"contact":contact_number_info,'date':str(today),'total':total_cost}

    bill_list.append(d)

    pickle.dump(bill_list,f)

    f.close()

 

def bill_search_command():

    bill_number_info=str(bill_number_entry.get())

    search_flag=0

    f=open('bill/'+username_info+'.bin','rb')

    while True:

        try:

            rec=pickle.load(f)         #[[a,1,10],[a,1,100],{"bil no":1,"cust name":1,"contact":1,'date':1}]

            d=rec[-1]

            if d['bil no']==bill_number_info:

                search_flag=1

                bill_number_info2=str(d['bil no'])

                cust_name_info=str(d['cust name'])   

                contact_number_info=str(d['contact'])

                cust_name_label.config(text='Customer Details: '+cust_name_info)

                phone_label.config(text='Phone Number:     '+contact_number_info)

                billnumber_label.config(text='Bill Number:    '+bill_number_info2)

                date_label.config(text='Date: '+str(d['date']))

                for a in rec:

                    if a==d:

                        break

                    n_product=len(a[0])

                    quan=str(a[1])

                    n_quantity=len(quan)

                    bill_list_box.insert(END,a[0]+" "*(80-(2*n_product))+quan+" "*(80-(2*n_quantity))+str(a[2]))

                bill_list_box.insert(END,"                                                                                                                                                        Total: "+str(d['total']))

 

        except EOFError:break

    if search_flag==0:

        messagebox.showinfo("ERROR","No Bill with bill number "+bill_number_info,icon="warning")

    if search_flag==1:

        bill_search_button.config(text="",command=searched)

        add_cart_button.config(text="",command=searched)

        clear1_button.config(text="",command=searched)

        total_button.config(text="",command=searched)

        generate_button.config(text="",command=searched)

        remove_button.config(text="",command=searched)

    f.close()

   

def searched():

    messagebox.showinfo("ERROR","Bill once genrated cannot be edited",icon="warning")

   

def emp_command():

    global emp_frame

    global emp_flag

    global bill_flag

    global acc_flag

    global home_flag

    global empID_info

    global name_info

    global email_info

    global post_info

    global mobile_info

    global adhaar_info

    global address_info

    global salary_info

    global show_emp_frame

    global add_emp_frame

    global delete_entry

    global modify_entry

    global mynotebook2

    global save

 

   

    if emp_flag==1:

        mynotebook2.destroy()

        emp_flag=0

       

    emp_flag=1

 

    if home_flag==1:

        wel_label.destroy()

        home_name_label.destroy()

        contact_us_label.destroy()

        costomer_care_label.destroy()

        home_flag=0

       

    if bill_flag==1:

        bill_frame.destroy()

        bill_flag=0

    if acc_flag==1:

        acc_frame.destroy()

        acc_flag=0

       

    mynotebook2=ttk.Notebook(mroot)

    add_emp_frame=Frame(mroot,width=500,height=400,bg="#E74C3C")

    mynotebook2.add(add_emp_frame,text='ADD Values')

    show_emp_frame=Frame(mroot,width=500,height=400,bg="#E74C3C")

    mynotebook2.add(show_emp_frame,text='show Values')

    mynotebook2.pack(expand=1,fill="both")

 

 

    #adding labels in add tab

    emp_ID=Label(add_emp_frame,text='1.Employee ID',fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    emp_ID.grid(row=2,column=0,sticky=W)

   

    name_label=Label(add_emp_frame,text="2.Name",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    name_label.grid(row=3,column=0,sticky=W)

 

    post_label=Label(add_emp_frame,text="3.Post",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    post_label.grid(row=4,column=0,sticky=W)

 

    mobile_label=Label(add_emp_frame,text="4.Mobile NO.",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    mobile_label.grid(row=5,column=0,sticky=W)

 

    email_label=Label(add_emp_frame,text="5.Email",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    email_label.grid(row=6,column=0,sticky=W)

 

    adhaar_label=Label(add_emp_frame,text="6.Adhaaar no.",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    adhaar_label.grid(row=7,column=0,sticky=W)

 

    address_label=Label(add_emp_frame,text="7.Address",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    address_label.grid(row=8,column=0,sticky=W)

 

    salary_label=Label(add_emp_frame,text="8.Salary",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    salary_label.grid(row=9,column=0,sticky=W)

 

    empID_info=Entry(add_emp_frame,bd=3)

    empID_info.grid(row=2,column=1,columnspan=1)

   

    name_info=Entry(add_emp_frame,bd=3)

    name_info.grid(row=3,column=1,columnspan=1)

 

    email_info=Entry(add_emp_frame,bd=3)

    email_info.grid(row=6,column=1,columnspan=2)

 

    post_info=Entry(add_emp_frame,bd=3)

    post_info.grid(row=4,column=1,columnspan=2)

 

    mobile_info=Entry(add_emp_frame,bd=3)

    mobile_info.grid(row=5,column=1,columnspan=3)

 

    adhaar_info=Entry(add_emp_frame,bd=3)

    adhaar_info.grid(row=7,column=1,columnspan=2)

 

    address_info=Entry(add_emp_frame,bd=3)

    address_info.grid(row=8,column=1,columnspan=5)

 

    salary_info=Entry(add_emp_frame,bd=3)

    salary_info.grid(row=9,column=1,columnspan=2)

 

    save=Button(add_emp_frame,text="Save",command=saves,width=6,bg="yellow",fg="#154360")

    save.grid(row=10,column=0)

 

    modify_button=Button(add_emp_frame,text="MODIFY",command=modify_command,bg="yellow",fg="#154360")

    modify_button.grid(row=4,column=13,padx=15)

    modify_entry=Entry(add_emp_frame,bd=3)

    modify_entry.grid(row=3,column=13)

    modify_label=Label(add_emp_frame,text="  Enter Emp ID :-  ",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    modify_label.grid(row=3,column=12)

   

    

  # adding info in  show tab

    show_command() 

    delete=Button(show_emp_frame,text="DELETE",command=delete_command,bg="yellow",fg="#154360")

    delete.grid(row=1,column=6,padx=15)

    delete_entry=Entry(show_emp_frame,bd=3)

    delete_entry.grid(row=0,column=6,columnspan=5)

    delete_label=Label(show_emp_frame,text="   Enter Emp ID:-  ",fg="#D5F5E3",bg="#E74C3C",font=("Helvetica","12"))

    delete_label.grid(row=0,column=5,)

   

 

def acc_command():

    global username_entry2

    global password_entry2

    global phone_entry2

    global shopname_entry2

    global emailID_entry2

    global address_entry2

    global change_command

    global emp_flag

    global bill_flag

    global acc_flag

    global home_flag

    global acc_frame

   

    if acc_flag==1:

        acc_frame.destroy()

        acc_flag=0

        

    acc_flag=1

   

    if home_flag==1:

        wel_label.destroy()

        home_name_label.destroy()

        contact_us_label.destroy()

        costomer_care_label.destroy()

        home_flag=0

       

    if emp_flag==1:

        mynotebook2.destroy()

        emp_flag=0

    if bill_flag==1:

        bill_frame.destroy()

        bill_flag=0

   

    acc_frame=Frame(mroot,bg="#E74C3C")

    acc_frame.pack(fill='both', expand=1)

    Label(acc_frame,text="First change the data then click the *To Change* button to save the changes",bg="#E74C3C",font=("Helvetica","12"),fg="#D5F5E3").grid(row=0,column=0,columnspan=50)

   

    username_label2=Label(acc_frame,text='Username:',bg="#E74C3C",font=("Helvetica","12"),fg="#D5F5E3").grid(row=1,column=0)

    passowrd_label2=Label(acc_frame,text='Password:',bg="#E74C3C",font=("Helvetica","12"),fg="#D5F5E3").grid(row=2,column=0)

    phone_label2=Label(acc_frame,text='Phone No:',bg="#E74C3C",font=("Helvetica","12"),fg="#D5F5E3").grid(row=3,column=0)

    shopname_label2=Label(acc_frame,text='Shop Name',bg="#E74C3C",font=("Helvetica","12"),fg="#D5F5E3").grid(row=4,column=0)

    emailID_label2=Label(acc_frame,text='Email ID:',bg="#E74C3C",font=("Helvetica","12"),fg="#D5F5E3").grid(row=5,column=0)

    address_label2=Label(acc_frame,text='Address:',bg="#E74C3C",font=("Helvetica","12"),fg="#D5F5E3").grid(row=6,column=0)

   

    username_entry2=Entry(acc_frame,bd=3,font=("Helvetica","12"))

    username_entry2.grid(row=1,column=1,columnspan=3)

    password_entry2=Entry(acc_frame,bd=3,font=("Helvetica","12"))

    password_entry2.grid(row=2,column=1,columnspan=3)

    phone_entry2=Entry(acc_frame,bd=3,font=("Helvetica","12"))

    phone_entry2.grid(row=3,column=1,columnspan=3)

    shopname_entry2=Entry(acc_frame,bd=3,font=("Helvetica","12"))

    shopname_entry2.grid(row=4,column=1,columnspan=3)

    emailID_entry2=Entry(acc_frame,bd=3,font=("Helvetica","12"))

    emailID_entry2.grid(row=5,column=1,columnspan=3)

    address_entry2=Entry(acc_frame,bd=3,font=("Helvetica","12"))

    address_entry2.grid(row=6,column=1,columnspan=3)

 

   

 

   

    f=open("userpass.bin","rb")

    while True:

        try:              

            rec = pickle.load(f)

            if rec['username']==username_info:

                username_entry2.insert(0,rec["username"])

                password_entry2.insert(0,rec["password"])

                phone_entry2.insert(0,rec["phone"])

                shopname_entry2.insert(0,rec["shopname"])

                emailID_entry2.insert(0,rec["emailID"])

                address_entry2.insert(0,rec["address"])

        except EOFError:break

    f.close()

    change_button=Button(acc_frame,text="CHANGE",command=change_command,width=10,bg="yellow")

    change_button.grid(row=7,column=0,pady=8)

    delete_button=Button(acc_frame,text="DELETE ACC",command=deleteacc_command,width=10,bg="yellow")

    delete_button.grid(row=8,column=0,pady=8)

    logout_button=Button(acc_frame,text="LOG OUT",command=logout_command,width=10,bg="yellow")

    logout_button.grid(row=9,column=0,pady=8)

   

def deleteacc_command():

    deleteacc_label="Are you sure you want to delete account. All data in your account will be be lost "

    MsgBox2=messagebox.askquestion('Delete Account',deleteacc_label,icon="warning")

    if MsgBox2=="yes":

        l=[]

        f=open("userpass.bin","rb")

        while True:

            try:

                rec=pickle.load(f)

                l.append(rec)

            except EOFError:break

        f.close()

 

        f=open('userpass.bin','wb')

        for x in l:

            if x['username']==username_info:

                continue

            pickle.dump(x,f)

        f.close()

        mroot.destroy()

    #f=open(username_info+".bin","wb")

    #f.close()

        os.remove('username/'+username_info+".bin")

        login_command()

   

def logout_command():

    mroot.destroy()

    login_command()

   

def quit_command():

    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')

    if MsgBox == 'yes':

        mroot.destroy()

       

def change_command():

    global create_root

    global shop_heading

    global phone_heading

    global email_heading                               

    global frame_heading

    global username_info

    global save_flag

    save_flag=0

    f=open("userpass.bin","rb")

    while True:

        try:               

            rec = pickle.load(f)

            if rec['username']==username_entry2.get():

                save_flag=1

        except EOFError:break

    f.close()

    if save_flag==0 or username_info==username_entry2.get():

        l=[]

        f=open("userpass.bin","rb")

        while True:

            try:

                rec=pickle.load(f)

                l.append(rec)

            except EOFError:break

        f.close()

 

        f=open('userpass.bin','wb')

        for x in l:

            if x['username']==username_info:

                continue

            pickle.dump(x,f)

        f.close()

        create_root=Label(mroot,text="HI")

        save1()

 

 

        f=open("userpass.bin","rb")

        while True:

            try:              

                rec = pickle.load(f)

                shop_info=rec['shopname']

                phone_info=rec['phone']

                email_info=rec['emailID']

                address_info=rec['address']

                username_info2=rec['username']

            except EOFError:break

        f.close()

        if username_info!=username_info2:

            os.remove('username/'+username_info2+".bin")

            os.remove('bill/'+username_info2+'.bin')

            os.rename('username/'+username_info+'.bin','username/'+username_info2+".bin")

            os.rename('bill/'+username_info+'.bin','bill/'+username_info2+".bin")

            username_info=username_info2

        shop_heading.config(text=shop_info)

        phone_heading.config(text=phone_info)

        email_heading.config(text=email_info)

        messagebox.showinfo("SUCCESFULL","Data succesfully changed",icon="info")

        save_flag=0

       

        

    if save_flag==1:

        f=open("userpass.bin","rb")

        while True:

            try:

                rec=pickle.load(f)

                temp_username=rec['username']

                temp_password=rec['password']

                temp_phone=rec['phone']

                temp_shopname=rec['shopname']

                temp_emailID=rec['emailID']

                temp_address=rec['address']

            except EOFError:break

        f.close()

        username_entry2.delete(0,END)

        password_entry2.delete(0,END)

        phone_entry2.delete(0,END)

        shopname_entry2.delete(0,END)

        emailID_entry2.delete(0,END)

        address_entry2.delete(0,END)

       

        username_entry2.insert(0,temp_username)

        password_entry2.insert(0,temp_password)

        phone_entry2.insert(0,temp_phone)

        shopname_entry2.insert(0,temp_shopname)

        emailID_entry2.insert(0,temp_emailID)

        address_entry2.insert(0,temp_address)

        messagebox.showinfo("ERROR","Username already in use",icon="warning")

       

def saves():

    global f

    save_flag=0

    empID_get =str(empID_info.get())

    name_get =str(name_info.get())

    post_get = str(post_info.get())

    mobile_get =str(mobile_info.get())

    email_get = str(email_info.get())

    adhaar_get = str(adhaar_info.get())

    address_get = str(address_info.get())

    salary_get = str(salary_info.get())

    if len(empID_get)==0 or len(name_get)==0 or len(post_get)==0 or len(salary_get)==0:

        messagebox.showinfo("ERROR","Information cannot be empty!",icon="warning")

    else:

        f=open('username/'+username_info+'.bin',"rb")

        while True:

            try:

                rec=pickle.load(f)

                if empID_get==rec["empID"]:

                    save_flag=1

                    messagebox.showinfo("ERROR","Emp ID already exists",icon="warning")

            except EOFError:break

        f.close()

        if save_flag==0:

            f=open('username/'+username_info+'.bin',"ab")

            d={'empID':empID_get,"name":name_get,"post":post_get,"mobile":mobile_get,"email":email_get,"adhaar":adhaar_get,"address":address_get,"salary":salary_get}

            pickle.dump(d,f)

            empID_info.delete(0,END)

            name_info.delete(0,END)

            post_info.delete(0,END)

            mobile_info.delete(0,END)

            email_info.delete(0,END)

            adhaar_info.delete(0,END)

            address_info.delete(0,END)

            salary_info.delete(0,END)

            f.close()

            show_command()

            save.config(text="Save")

   

def show_command():

    global list_box

    global emp_listbox_frame

    x=0

    emp_listbox_frame=LabelFrame(show_emp_frame,bg="#F39C12",bd=4)

    emp_listbox_frame.grid(row=0,column=0, rowspan=1000)

    emp_scrlbar=Scrollbar(emp_listbox_frame,orient="vertical")

   

    emp_list_box=Listbox(emp_listbox_frame,width=50,height=30,bg="#F39C12",bd=2,yscrollcommand=emp_scrlbar.set)

    emp_scrlbar.config(command=emp_list_box.yview)

    emp_scrlbar.pack(side=RIGHT,fill=Y)

   

    emp_list_box.pack()

   

    

    f=open('username/'+username_info+'.bin','rb')

 

    w=Scrollbar(emp_list_box)

   

    while True:

        try:              

            rec = pickle.load(f)

            emp_list_box.insert(0+x,"            EmpID:      "+rec['empID'])

            emp_list_box.insert(1+x,"            Name:       "+rec['name'])

            emp_list_box.insert(2+x,"            Post:          "+rec['post'])

            emp_list_box.insert(3+x,"            mobile:     "+rec['mobile'])

            emp_list_box.insert(4+x,"            Email:        "+rec['email'])

            emp_list_box.insert(5+x,"            Adhaar:     "+rec['adhaar'])

            emp_list_box.insert(6+x,"            Address:    "+rec['address'])

            emp_list_box.insert(7+x,"            Salary:        "+rec['salary'])

            emp_list_box.insert(8+x,"___________________________________________")

            x=x+9

        except EOFError:break

    f.close()

 

def delete_command():

    global delete_message

    flag=0

    delete_info=str(delete_entry.get())

    f=open('username/'+username_info+'.bin','rb')

    l=[]

    while True:

        try:

            rec=pickle.load(f)

            l.append(rec)

        except EOFError:break

    f.close()

    f=open('username/'+username_info+'.bin','wb')

    for x in l:

        if x['empID']==delete_info:

            flag=1

            continue

        pickle.dump(x,f)

    f.close()

    delete_entry.delete(0,END)

    if flag==0:

        messagebox.showinfo("ERROR","EmpID "+delete_info+" not found",icon="warning")

    if flag==1:

        show_command()

        messagebox.showinfo("Info","Successfully deleted",icon="info")

   

def modify_command():

    global modify_message

    flag=0

    modify_info=str(modify_entry.get())

    name_info.delete(0,END)

    post_info.delete(0,END)

    mobile_info.delete(0,END)

    email_info.delete(0,END)

    adhaar_info.delete(0,END)

    address_info.delete(0,END)

    salary_info.delete(0,END)

    f=open('username/'+username_info+'.bin','rb')

    l=[]

    while True:

        try:

            rec=pickle.load(f)

            l.append(rec)

        except EOFError:break

    f.close()

   

    f=open('username/'+username_info+'.bin','rb')

    for x in l:

        if x['empID']==modify_info:

            flag=1

            empID_info.insert(0,x['empID'])

            name_info.insert(0,x['name'])

            post_info.insert(0,x['post'])

            mobile_info.insert(0,x['mobile'])

            email_info.insert(0,x['email'])

            adhaar_info.insert(0,x['adhaar'])

            address_info.insert(0,x['address'])

            salary_info.insert(0,x['salary'])

    f.close()

    modify_entry.delete(0,END)

    if flag==0:

        messagebox.showinfo("ERROR","EmpID "+modify_info+" not found",icon="warning")

    if flag==1:

        f=open('username/'+username_info+'.bin','wb')

        for x in l:

            if x['empID']==modify_info:

                continue

            pickle.dump(x,f)

        f.close()

        save.config(text="Update")

        messagebox.showinfo("Update","Click on Update to modify",icon="info")

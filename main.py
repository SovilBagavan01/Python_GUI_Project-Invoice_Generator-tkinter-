import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime


#now to clear the items
def clear_item():
    qty_spinbox.delete(0,tkinter.END)# for qty_spinbox delete from 0 to the end 
    qty_spinbox.insert(0,"1")#default value=1
    desc_entry.delete(0,tkinter.END)
    price_spinbox.delete(0,tkinter.END)
    price_spinbox.insert(0,"0.0")
#function for add_item Button
invoice_list=[]
def add_item():
    qty = int(qty_spinbox.get())
    desc= desc_entry.get()
    price = float(price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty,desc,price,line_total]

    tree.insert("",0, values=invoice_item)
    clear_item()

    invoice_list.append(invoice_item)
    
#function for new_invoice 
def new_invoice():
    name_entry.delete(0,tkinter.END)
    email_entry.delete(0,tkinter.END)
    phone_entry.delete(0,tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()

def generate_invoice():
    doc  = DocxTemplate("Relecloud.docx")
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = 1.8
    total = subtotal*(1-salestax)


    doc.render({"name":name,
                "email":email,
                "phone":phone,
                "invoice_list":invoice_list,
                "subtotal":subtotal,
                "salestax":str(salestax*100)+"%",
                "total":total})
    
    doc_name = "new_invoice" + name +datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")+".docx"
    doc.save(doc_name)


#window building
window = tkinter.Tk()
window.title("Invoice Generator Form")
#frame building
frame = tkinter.Frame(window)#use of ".frame " F must be capital
frame.pack()
#label building
name_label = tkinter.Label(frame, text="Name")
name_label.grid(row=0, column=0)
email_label = tkinter.Label(frame, text="Email")
email_label.grid(row=0, column=1)

name_entry = tkinter.Entry(frame)
email_entry = tkinter.Entry(frame)
name_entry.grid(row=1, column=0)
email_entry.grid(row=1, column=1)

phone_label = tkinter.Label(frame, text="Phone")
phone_label.grid(row=0, column=2)
phone_entry = tkinter.Entry(frame)
phone_entry.grid(row=1, column=2)

qty_label = tkinter.Label(frame, text="qty")
qty_label.grid(row=2, column=0)
qty_spinbox = tkinter.Spinbox(frame, from_=1, to=1000, increment=1)
qty_spinbox.grid(row=3,column=0) 

desc_label = tkinter.Label(frame,text="Description")
desc_label.grid(row=2, column=1)
desc_entry = tkinter.Entry(frame)
desc_entry.grid(row=3, column=1)

price_label = tkinter.Label(frame, text="Unit Price")
price_label.grid(row=2, column=2)
price_spinbox= tkinter.Spinbox(frame, from_=0.0, to=500000, increment=100)
price_spinbox.grid(row=3, column=2)

add_item_button = tkinter.Button(frame, text="Add Item", command= add_item)
add_item_button.grid(row=4, column=2, pady=5)

#creating the tree view, i imported ttk to create a tree view
columns=('qty','desc','price','total')
tree = ttk.Treeview(frame,column=columns,show="headings")
tree.heading('qty', text="Qty")
tree.heading('desc', text="Description")
tree.heading('price', text="Unit_Price")
tree.heading('total', text="Total")

tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

save_invoice_button = tkinter.Button(frame, text="Generate Invoice", command=generate_invoice)
#sticky="news" refers to north-east-west-south
save_invoice_button.grid(row=6,column=0,columnspan=3,sticky="news",padx=20,pady=5)
new_invoice_button = tkinter.Button(frame, text="New Invoice", command=new_invoice)
new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)
window.mainloop()
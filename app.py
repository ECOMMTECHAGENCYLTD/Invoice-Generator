from tkinter import *
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import datetime

root = Tk()
root.title("Invoice Generator")
root.geometry("500x650")

Label(root,text="Invoice Generator",font=("Arial",18,"bold")).pack(pady=10)

def field(label):
    Label(root,text=label,font=("Arial",11)).pack()
    e=Entry(root,width=45)
    e.pack(pady=4)
    return e

customer=field("Customer Name")
email=field("Email")
phone=field("Phone")
product=field("Product")
qty=field("Quantity")
price=field("Price per Unit")

def create_invoice():

    try:
        quantity=float(qty.get())
        unit=float(price.get())
    except:
        messagebox.showerror("Error","Quantity and Price must be numeric.")
        return

    total=quantity*unit

    if not os.path.exists("invoices"):
        os.makedirs("invoices")

    filename="invoices/Invoice_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".pdf"

    pdf=canvas.Canvas(filename,pagesize=A4)

    pdf.setFont("Helvetica-Bold",20)
    pdf.drawString(200,800,"INVOICE")

    pdf.setFont("Helvetica",12)

    y=750

    pdf.drawString(50,y,"Customer: "+customer.get())
    y-=25
    pdf.drawString(50,y,"Email: "+email.get())
    y-=25
    pdf.drawString(50,y,"Phone: "+phone.get())

    y-=50

    pdf.drawString(50,y,"Product")
    pdf.drawString(250,y,"Qty")
    pdf.drawString(320,y,"Price")
    pdf.drawString(420,y,"Total")

    y-=20

    pdf.line(50,y,520,y)

    y-=30

    pdf.drawString(50,y,product.get())
    pdf.drawString(250,y,str(quantity))
    pdf.drawString(320,y,f"${unit:.2f}")
    pdf.drawString(420,y,f"${total:.2f}")

    y-=60

    pdf.setFont("Helvetica-Bold",14)
    pdf.drawString(330,y,"Grand Total")
    pdf.drawString(450,y,f"${total:.2f}")

    pdf.save()

    messagebox.showinfo("Success",f"Invoice saved:\n{filename}")

Button(root,text="Generate Invoice",
       bg="green",
       fg="white",
       font=("Arial",12,"bold"),
       command=create_invoice).pack(pady=30)

root.mainloop()

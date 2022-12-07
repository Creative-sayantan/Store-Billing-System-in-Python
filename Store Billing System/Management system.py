from tkinter import *
import random
import datetime
import time
import tkinter.messagebox

root = Tk()
root.geometry("1300x750+0+0")
root.title("Sweets Shop")
root.configure(background = 'cyan')

text_Input = StringVar()
operator = ""

Tops = Frame(root,bg='cyan',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops,font=('pyparus',30),text="Kalpataru Sweets",bd=18,bg='white',fg='cyan',justify=CENTER)
lblTitle.grid(row=0,column=0)

Copyright = Label(root ,bg = 'cyan',fg='white', width = 1200, font=('Arial', 10, 'bold'))
Copyright.pack(side = BOTTOM)

ReceiptCal_F = Frame(root,bg='powder blue',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='powder blue',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='powder blue',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='powder blue',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='cyan',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)

Cost_F=Frame(MenuFrame,bg='white',bd=4)
Cost_F.pack(side=BOTTOM)

Drinks_F=Frame(MenuFrame,bg='cyan',bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame,bg='white',bd=10,width=300,height=400,relief=RIDGE)
Drinks_F.pack(side=LEFT)

Cake_F=Frame(MenuFrame,bg='white',bd=10,relief=RIDGE)
Cake_F.pack(side=RIGHT)

#=====================================================================================================================================#
def iExit():
    iExit = tkinter.messagebox.askyesno("Exit","Confirm you want to exit")
    if iExit>0:
        root.destroy()
        return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    E_Samosa.set("0")
    E_Kachori.set("0")
    E_Lassi.set("0")
    E_G_Halwa.set("0")
    E_KK.set("0")
    E_Ladoo1.set("0")
    E_M_Cake.set("0")
    E_M_Barfi.set("0")

    E_M_Mawa.set("0")
    E_C_Drinks.set("0")
    E_Chips.set("0")
    E_Ladoo2.set("0")
    E_B_Sweets.set("0")
    E_Peda.set("0")
    E_Chach.set("0")
    E_Dhai.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    txtSamosa.configure(state = DISABLED)
    txtKachori.configure(state = DISABLED)
    txtLassi.configure(state = DISABLED)
    txtG_Halwa.configure(state = DISABLED)
    txtKK.configure(state = DISABLED)
    txtLadoo1.configure(state = DISABLED)
    txtM_Cake.configure(state = DISABLED)
    txtM_Barfi.configure(state = DISABLED)
    txtM_Mawa.configure(state = DISABLED)
    txtC_Drinks.configure(state = DISABLED)
    txtChips.configure(state = DISABLED)
    txtLadoo2.configure(state = DISABLED)
    txtB_Sweets.configure(state = DISABLED)
    txtPeda.configure(state = DISABLED)
    txtChach.configure(state = DISABLED)
    txtDhai.configure(state = DISABLED)

def CostofItem():
    Item1=float(E_Samosa.get())
    Item2=float(E_Kachori.get())
    Item3=float(E_Lassi.get())
    Item4=float(E_G_Halwa.get())
    Item5=float(E_KK.get())
    Item6=float(E_Ladoo1.get())
    Item7=float(E_M_Cake.get())
    Item8=float(E_M_Barfi.get())
    Item9=float(E_M_Mawa.get())
    Item10=float(E_C_Drinks.get())
    Item11=float(E_Chips.get())
    Item12=float(E_Ladoo2.get())
    Item13=float(E_B_Sweets.get())
    Item14=float(E_Peda.get())
    Item15=float(E_Chach.get())
    Item16=float(E_Dhai.get())

    PriceofDrinks = (Item1*8) + (Item2*8) + (Item3*20) + (Item4*15) + (Item5*200)+ (Item6*140) + (Item7*50) + (Item8*60)
    PriceofCakes = (Item9*15) + (Item10*20) + (Item11*5) + (Item12*90) + (Item13*180) + (Item14*40) + (Item15*10) + (Item16*10)

    DrinksPrice = "Rs.",str('%.2f'%(PriceofDrinks))
    CakesPrice = "Rs.",str('%.2f'%(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rs.", str('%.2f'%(0))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs.",str('%.2f'%(PriceofDrinks + PriceofCakes + 0))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs.",str('%.2f'%((PriceofDrinks + PriceofCakes + 0)*0))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 0)*0)
    TC = "Rs.",str('%.2f'%(PriceofDrinks + PriceofCakes + 0 + TT))
    TotalCost.set(TC)
def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(100,10000)
    randomRef = str(x)
    Receipt_Ref.set("SS" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Item:\t\t\t'+ "Cost of Items\n")
    txtReceipt.insert(END, 'Samosa:\t\t\t'+E_Samosa.get()+"\n")
    txtReceipt.insert(END, 'Kachori:\t\t\t'+E_Kachori.get()+"\n")
    txtReceipt.insert(END, 'Lassi:\t\t\t'+E_Lassi.get()+"\n")
    txtReceipt.insert(END, 'Halwa(Gajar):\t\t\t'+ E_G_Halwa.get()+"\n")
    txtReceipt.insert(END, 'Kaju Katli:\t\t\t'+E_KK.get()+"\n")
    txtReceipt.insert(END, 'Ladoo(Besan):\t\t\t'+E_Ladoo1.get()+"\n")
    txtReceipt.insert(END, 'Milk Cake:\t\t\t'+ E_M_Cake.get()+"\n")
    txtReceipt.insert(END, 'Mawa Barfi:\t\t\t'+ E_M_Barfi.get()+"\n")
    txtReceipt.insert(END, 'Misri Mawa:\t\t\t'+ E_M_Mawa.get()+"\n")
    txtReceipt.insert(END, 'Cold Drinks:\t\t\t'+E_C_Drinks.get()+"\n")
    txtReceipt.insert(END, 'Chips:\t\t\t'+E_Chips.get()+"\n")
    txtReceipt.insert(END, 'Ladoo(Bundi):\t\t\t'+E_Ladoo2.get()+"\n")
    txtReceipt.insert(END, 'Bengali Sweets:\t\t\t'+E_B_Sweets.get()+"\n")
    txtReceipt.insert(END, 'Peda:\t\t\t'+E_Peda.get()+"\n")
    txtReceipt.insert(END, 'Chach:\t\t\t'+E_Chach.get()+"\n")
    txtReceipt.insert(END, 'Dhai:\t\t\t'+E_Dhai.get()+"\n")

    txtReceipt.insert(END, "Cost of Items:\t\t\t" + (SubTotal.get()) + "\nTax:\t\t\t"+PaidTax.get() + "\n")
    txtReceipt.insert(END, "Sub Total:\t\t\t" + str(SubTotal.get()) + "\n")
    txtReceipt.insert(END, "Service Charge:\t\t\t" + ServiceCharge.get() + "\nTotal:\t\t\t"+str(TotalCost.get()))
#=====================================================================================================================================#
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator=""

E_Samosa=StringVar()
E_Kachori=StringVar()
E_Lassi=StringVar()
E_G_Halwa=StringVar()
E_KK=StringVar()
E_Ladoo1=StringVar()
E_M_Cake=StringVar()
E_M_Barfi=StringVar()

E_M_Mawa=StringVar()
E_C_Drinks=StringVar()
E_Chips=StringVar() 
E_Ladoo2=StringVar()
E_B_Sweets=StringVar()
E_Peda=StringVar()
E_Chach=StringVar()
E_Dhai=StringVar()

E_Samosa.set("0")
E_Kachori.set("0")
E_Lassi.set("0")
E_G_Halwa.set("0")
E_KK.set("0")
E_Ladoo1.set("0")
E_M_Cake.set("0")
E_M_Barfi.set("0")

E_M_Mawa.set("0")
E_C_Drinks.set("0")
E_Chips.set("0")
E_Ladoo2.set("0")
E_B_Sweets.set("0")
E_Peda.set("0")
E_Chach.set("0")
E_Dhai.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))
#======================================================================================================================================#
def chSamosa():
    if (var1.get() == 1):
        txtSamosa.configure(state=NORMAL)
        txtSamosa.focus()
        txtSamosa.delete('0',END)
        E_Samosa.set("")
    elif(var1.get() == 0):
        txtSamosa.configure(state=DISABLED)
        E_Samosa.set("0")
def chKachori():
    if (var2.get() == 1):
        txtKachori.configure(state=NORMAL)
        txtKachori.focus()
        txtKachori.delete('0',END)
        E_Kachori.set("")
    elif(var2.get() == 0):
        txtKachori.configure(state=DISABLED)
        E_Kachori.set("0")
def chLassi():
    if (var3.get() == 1):
        txtLassi.configure(state=NORMAL)
        txtLassi.focus()
        txtLassi.delete('0',END)
        E_Lassi.set("")
    elif(var3.get() == 0):
        txtLassi.configure(state=DISABLED)
        E_Lassi.set("0")
def chM_Cake():
    if (var7.get() == 1):
        txtM_Cake.configure(state=NORMAL)
        txtM_Cake.focus()
        txtM_Cake.delete('0',END)
        E_Samosa.set("")
    elif(var7.get() == 0):
        txtM_Cake.configure(state=DISABLED)
        E_M_Cake.set("0")
def chM_Barfi():
    if (var8.get() == 1):
        txtM_Barfi.configure(state=NORMAL)
        txtM_Barfi.focus()
        txtM_Barfi.delete('0',END)
        E_M_Barfi.set("")
    elif(var8.get() == 0):
        txtM_Barfi.configure(state=DISABLED)
        E_M_Barfi.set("0")
def chG_Halwa():
    if (var4.get() == 1):
        txtG_Halwa.configure(state=NORMAL)
        txtG_Halwa.focus()
        txtG_Halwa.delete('0',END)
        E_G_Halwa.set("")
    elif(var4.get() == 0):
        txtG_Halwa.configure(state=DISABLED)
        E_G_Halwa.set("0")
def chKK():
    if (var5.get() == 1):
        txtKK.configure(state=NORMAL)
        txtKK.focus()
        txtKK.delete('0',END)
        E_KK.set("")
    elif(var5.get() == 0):
        txtKK.configure(state=DISABLED)
        E_KK.set("0")
def chLadoo1():
    if (var6.get() == 1):
        txtLadoo1.configure(state=NORMAL)
        txtLadoo1.focus()
        txtLadoo1.delete('0',END)
        E_Ladoo1.set("")
    elif(var6.get() == 0):
        txtLadoo1.configure(state=DISABLED)
        E_Ladoo1.set("0")
def chDhai():
    if (var16.get() == 1):
        txtDhai.configure(state=NORMAL)
        txtDhai.focus()
        txtDhai.delete('0',END)
        E_Dhai.set("")
    elif(var16.get() == 0):
        txtDhai.configure(state=DISABLED)
        E_Dhai.set("0")
def chChach():
    if (var15.get() == 1):
        txtChach.configure(state=NORMAL)
        txtChach.focus()
        txtChach.delete('0',END)
        E_Chach.set("")
    elif(var15.get() == 0):
        txtChach.configure(state=DISABLED)
        E_Chach.set("0")
def chPeda():
    if (var14.get() == 1):
        txtPeda.configure(state=NORMAL)
        txtPeda.focus()
        txtPeda.delete('0',END)
        E_Peda.set("")
    elif(var14.get() == 0):
        txtPeda.configure(state=DISABLED)
        E_Peda.set("0")
def chLadoo2():
    if (var12.get() == 1):
        txtLadoo2.configure(state=NORMAL)
        txtLadoo2.focus()
        txtLadoo2.delete('0',END)
        E_Ladoo2.set("")
    elif(var12.get() == 0):
        txtLadoo2.configure(state=DISABLED)
        E_Ladoo2.set("0")
def chChips():
    if (var11.get() == 1):
        txtChips.configure(state=NORMAL)
        txtChips.focus()
        txtChips.delete('0',END)
        E_Chips.set("")
    elif(var11.get() == 0):
        txtChips.configure(state=DISABLED)
        E_Chips.set("0")
def chB_Sweets():
    if (var13.get() == 1):
        txtB_Sweets.configure(state=NORMAL)
        txtB_Sweets.focus()
        txtB_Sweets.delete('0',END)
        E_B_Sweets.set("")
    elif(var13.get() == 0):
        txtB_Sweets.configure(state=DISABLED)
        E_B_Sweets.set("0")
def chC_Drinks():
    if (var10.get() == 1):
        txtC_Drinks.configure(state=NORMAL)
        txtC_Drinks.focus()
        txtC_Drinks.delete('0',END)
        E_C_Drinks.set("")
    elif(var10.get() == 0):
        txtC_Drinks.configure(state=DISABLED)
        E_C_Drinks.set("0")
def chM_Mawa():
    if (var9.get() == 1):
        txtM_Mawa.configure(state=NORMAL)
        txtM_Mawa.focus()
        txtM_Mawa.delete('0',END)
        E_M_Mawa.set("")
    elif(var9.get() == 0):
        txtM_Mawa.configure(state=DISABLED)
        E_M_Mawa.set("0")
#=========================================================DRINKS=======================================================================#
Samosa=Checkbutton(Drinks_F,text="Samosa",variable=var1,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chSamosa).grid(row=0,sticky=W)
Kachori=Checkbutton(Drinks_F,text="Kachori",variable=var2,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chKachori).grid(row=1,sticky=W)
Lassi=Checkbutton(Drinks_F,text="Lassi",variable=var3,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chLassi).grid(row=2,sticky=W)
G_Halwa=Checkbutton(Drinks_F,text="Gajar Halwa",variable=var4,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chG_Halwa).grid(row=3,sticky=W)
KK=Checkbutton(Drinks_F,text="Kaju Katli",variable=var5,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chKK).grid(row=4,sticky=W)
Ladoo1=Checkbutton(Drinks_F,text="Ladoo(Besan)",variable=var6,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chLadoo1).grid(row=5,sticky=W)
M_Cake=Checkbutton(Drinks_F,text="Milk Cake",variable=var7,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chM_Cake).grid(row=6,sticky=W)
M_Barfi=Checkbutton(Drinks_F,text="Mawa Barfi",variable=var8,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chM_Barfi).grid(row=7,sticky=W)
#=======================================================ENTRY==BOX==FOR==DRINKS=========================================================#
txtSamosa = Entry(Drinks_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Samosa)
txtSamosa.grid(row=0,column=1)
txtKachori = Entry(Drinks_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Kachori)
txtKachori.grid(row=1,column=1)
txtLassi = Entry(Drinks_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Lassi)
txtLassi.grid(row=2,column=1)
txtG_Halwa = Entry(Drinks_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_G_Halwa)
txtG_Halwa.grid(row=3,column=1)
txtKK = Entry(Drinks_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_KK)
txtKK.grid(row=4,column=1)
txtLadoo1 = Entry(Drinks_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Ladoo1)
txtLadoo1.grid(row=5,column=1)
txtM_Cake = Entry(Drinks_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_M_Cake)
txtM_Cake.grid(row=6,column=1)
txtM_Barfi = Entry(Drinks_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_M_Barfi)
txtM_Barfi.grid(row=7,column=1)
#===============================================================CAKES===================================================================#
M_Mawa=Checkbutton(Cake_F,text="Misri Mawa",variable=var9,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chM_Mawa).grid(row=0,sticky=W)
C_Drinks=Checkbutton(Cake_F,text="Cold Drinks",variable=var10,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chC_Drinks).grid(row=1,sticky=W)
Chips=Checkbutton(Cake_F,text="CHIPS",variable=var11,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chChips).grid(row=2,sticky=W)
Ladoo2=Checkbutton(Cake_F,text="Ladoo(Bundi)",variable=var12,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chLadoo2).grid(row=3,sticky=W)
B_Sweets=Checkbutton(Cake_F,text="Bengali Sweets",variable=var13,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chB_Sweets).grid(row=4,sticky=W)
Peda=Checkbutton(Cake_F,text="Doodh Peda",variable=var14,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chPeda).grid(row=5,sticky=W)
Chach=Checkbutton(Cake_F,text="Chach",variable=var15,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chChach).grid(row=6,sticky=W)
Dhai=Checkbutton(Cake_F,text="Dhai",variable=var16,onvalue=1,offvalue=0, font=('Vrinda',18),bg='white',command = chDhai).grid(row=7,sticky=W)
#=======================================================ENTRY==BOX==FOR==CAKES===========================================================#
txtM_Mawa = Entry(Cake_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_M_Mawa)
txtM_Mawa.grid(row=0,column=1)
txtC_Drinks = Entry(Cake_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_C_Drinks)
txtC_Drinks.grid(row=1,column=1)
txtChips = Entry(Cake_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Chips)
txtChips.grid(row=2,column=1)
txtLadoo2 = Entry(Cake_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Ladoo2)
txtLadoo2.grid(row=3,column=1)
txtB_Sweets = Entry(Cake_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_B_Sweets)
txtB_Sweets.grid(row=4,column=1)
txtPeda = Entry(Cake_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Peda)
txtPeda.grid(row=5,column=1)
txtChach = Entry(Cake_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Chach)
txtChach.grid(row=6,column=1)
txtDhai = Entry(Cake_F,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Dhai)
txtDhai.grid(row=7,column=1)
#============================================================Total Cost==================================================================#
lblCostofDrinks = Label(Cost_F,font=('Vrinda',14),text="Cost Of List1\t ",bg="white",fg="black")
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks = Entry(Cost_F,font=('Vrinda',14),textvariable=CostofDrinks,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtCostofDrinks.grid(row=0,column=1)

lblCostofCakes = Label(Cost_F,font=('Vrinda',14),text="Cost Of List2 ",bg="white",fg="black")
lblCostofCakes.grid(row=1,column=0,sticky=W)
txtCostofCakes = Entry(Cost_F,font=('Vrinda',14),textvariable=CostofCakes,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtCostofCakes.grid(row=1,column=1)

lblServiceCharge = Label(Cost_F,font=('Vrinda',14),text="Service Charge ",bg="white",fg="black")
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge = Entry(Cost_F,font=('Vrinda',14),textvariable=ServiceCharge,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtServiceCharge.grid(row=2,column=1)
#=======================================================Payment Information==============================================================#
lblPaidTax = Label(Cost_F,font=('Vrinda',14),text="Paid Tax",bg="white",fg="black")
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax = Entry(Cost_F,font=('Vrinda',14),textvariable=PaidTax,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtPaidTax.grid(row=0,column=3)

lblSubTotal = Label(Cost_F,font=('Vrinda',14),text="Sub Total",bg="white",fg="black")
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal = Entry(Cost_F,font=('Vrinda',14),textvariable=SubTotal,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtSubTotal.grid(row=1,column=3)

lblTotalCost = Label(Cost_F,font=('Vrinda',14),text="Total Cost",bg="white",fg="black")
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost = Entry(Cost_F,font=('Vrinda',14),textvariable=TotalCost,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtTotalCost.grid(row=2,column=3)
#==============================================================RECEIPT===================================================================#
txtReceipt = Text(Receipt_F, width=46,height=12,bg="white",bd=4,font=('Vrinda',12))
txtReceipt.grid(row=0,column=0)
#==============================================================BUTTONS====================================================================#
btnTotal = Button(Buttons_F,padx=15,pady=1,fg="black",font=('calibri',15),width=4,text="Total",bg="powder blue",command = CostofItem).grid(row=0,column=0)
btnReceipt = Button(Buttons_F,padx=15,pady=1,fg="black",font=('calibri',15),width=4,text="Receipt",bg="powder blue",command = Receipt).grid(row=0,column=1)
btnReset = Button(Buttons_F,padx=15,pady=1,fg="black",font=('calibri',15),width=4,text="Reset",bg="powder blue",command=Reset).grid(row=0,column=2)
btnExit = Button(Buttons_F,padx=15,pady=1,fg="black",font=('calibri',15),width=4,text="Exit",bg="powder blue",command=iExit).grid(row=0,column=3)
#============================================================CALCULATOR DISPLAY===========================================================#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
def btnClear():
    global operator
    operator=""
    text_Input.set("")
def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    
txtDisplay = Entry(Cal_F, width=45,bg="white",bd=4,font=('Vrinda',12,'bold'),textvariable=text_Input,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
#========================================================================Calculator Buttons=========================================================================#
btn7=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="7", bg="white",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="8", bg="white",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="9", bg="white",command=lambda:btnClick(9)).grid(row=2,column=2)
btnAddition=Button(Cal_F,padx=16, pady=1,fg="white", font=('calibri',19,'bold'),width=4,text="+", bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
btn4=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="4", bg="white",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="5", bg="white",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="6", bg="white",command=lambda:btnClick(6)).grid(row=3,column=2)
btnSubstraction=Button(Cal_F,padx=16, pady=1,fg="white", font=('calibri',19,'bold'),width=4,text="-", bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
btn1=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="1", bg="white",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="2", bg="white",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16, pady=1,fg="powder blue", font=('calibri',19,'bold'),width=4,text="3", bg="white",command=lambda:btnClick(3)).grid(row=4,column=2)
btnMultiply=Button(Cal_F,padx=16, pady=1,fg="white", font=('calibri',19,'bold'),width=4,text="x", bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
btn0=Button(Cal_F,padx=16, pady=1,fg="white", font=('calibri',19,'bold'),width=4,text="0", bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16, pady=1,fg="white", font=('calibri',19,'bold'),width=4,text="C", bg="powder blue",command=btnClear).grid(row=5,column=1)
btnEquals=Button(Cal_F,padx=16, pady=1,fg="white", font=('calibri',19,'bold'),width=4,text="=", bg="powder blue",command=btnEquals).grid(row=5,column=2)
btnDivision=Button(Cal_F,padx=16, pady=1,fg="white", font=('calibri',19,'bold'),width=4,text="/", bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)
#=============================================================================================================================================================================#
root.mainloop()


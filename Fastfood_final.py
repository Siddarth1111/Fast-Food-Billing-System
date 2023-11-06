from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
import mysql.connector as sql
import random
import os

os.environ['LANG'] = 'en_US.UTF-8'


a=sql.connect(host='localhost',user='root',password='root',auth_plugin='mysql_native_password')
b=a.cursor()
b.execute('create database if not exists fastfood')
b.execute("use fastfood")

window=Tk()
window.geometry("1920x1080+0+0")
window.title("Pick n Pay")
window.config(bg='#F7F1E5')

top = Frame(window,bg='#E7B10A',width=1920,height=100,bd=12)
top.pack(side=TOP)
lbltitle = Label(top,bg='#F7F1E5',fg='#E7B10A',font=('arial',50,'bold'), text="                                Pick 'n Pay                             ")
lbltitle.grid(row=0,column=0)

bottom = Frame(window,bg='#F7F1E5',width=1920,height=650,bd=60)
bottom.pack(side=BOTTOM)

f1 = Frame(bottom,bg='#F7F1E5',width=480,height=50,bd=12)
f1.pack(side=LEFT)

f2 = Frame(bottom,bg='#F7F1E5',width=480,height=650,bd=12)
f2.pack(side=LEFT)

f2top = Frame(f2,bg='#F7F1E5',width=480,height=325,bd=12)
f2top.pack(side=TOP)

f2bottom = Frame(f2,bg='#F7F1E5',width=480,height=325,bd=12)
f2bottom.pack(side=BOTTOM)

f3 = Frame(bottom,bg='#F7F1E5',width=480,height=650,bd=12)
f3.pack(side=RIGHT)

all_food = {}
selected_food = {}

var1=BooleanVar()
var2=BooleanVar()
var3=BooleanVar()
var4=BooleanVar()
var5=BooleanVar()
var6=BooleanVar()
var7=BooleanVar()
var8=BooleanVar()
var9=BooleanVar()
var10=BooleanVar()
var11=BooleanVar()
var12=BooleanVar()
var13=BooleanVar()
var14=BooleanVar()
var15=BooleanVar()
var16=BooleanVar()
var19=BooleanVar()
var20=BooleanVar()
var21=BooleanVar()
var22=BooleanVar()
var23=BooleanVar()
var24=BooleanVar()
var25=BooleanVar()
var26=BooleanVar()
var27=BooleanVar()
var28=BooleanVar()
var29=BooleanVar()
var30=BooleanVar()
var31=BooleanVar()
var32=BooleanVar()
var33=BooleanVar()
var34=BooleanVar()
var35=BooleanVar()
var36=BooleanVar()
vartax=StringVar()
varsub=StringVar()
vartotal=StringVar()

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
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)
var24.set(0)
var25.set(0)
var26.set(0)
var27.set(0)
var28.set(0)
var29.set(0)
var30.set(0)
var31.set(0)
var32.set(0)
var33.set(0)
var34.set(0)
var35.set(0)
var36.set(0)

s1='Chicken Soup'
s2='Hot n Sour Soup'
s3='Sweet Corn Soup'
s4='French Onion Soup'
s5='Blue Cheese Fritters'
s6='Chicken Canapés'
s7='Stuffed Crab'
s8='Shrimp Canapés'
s9='Dukkah'
s10='Cordon Bleu'
s11='Lentil Salad'
dr1='Absinthe'
dr2='Pastis'
dr3='Calvados'
dr4='Chinon '
dr5='Muscadet'
ds1='Calisson'
ds2='Crème Brûlée'
ds3='Charlotte'
ds4='Clafoutis'
sh1='Salted Caramel'
sh2='Frozen Mudslide'
sh3='Chocolate'
sh4='French Vanilla'

varcsoup = StringVar()
varhsoup = StringVar()
varssoup = StringVar()
varfsoup = StringVar()
varbc = StringVar()
varcc = StringVar()
varcs = StringVar()
varsc = StringVar()
vard = StringVar()
varcb = StringVar()
varls = StringVar()
varab = StringVar()
varpa = StringVar()
varcv = StringVar()
varcn = StringVar()
varmu = StringVar()
varci = StringVar()
varbl = StringVar()
varco = StringVar()
varcf = StringVar()
varfv = StringVar()
varfm = StringVar()
varce = StringVar()
varfa = StringVar()

varcsoup.set('0')
varhsoup.set('0')
varssoup.set('0')
varfsoup.set('0')
varbc.set('0')
varcc.set('0')
varcs.set('0')
varsc.set('0')
vard.set('0')
varcb.set('0')
varls.set('0')
varab.set('0')
varpa.set('0')
varcv.set('0')
varcn.set('0')
varmu.set('0')
varci.set('0')
varbl.set('0')
varco.set('0')
varcf.set('0')
varfv.set('0')
varfm.set('0')
varce.set('0')
varfa.set('0')
vartax.set('0')
varsub.set('0')
vartotal.set('0')

def reset():
    varcsoup.set(0)
    varhsoup.set('0')
    varssoup.set('0')
    varfsoup.set('0')
    varbc.set('0')
    varcc.set('0')
    varcs.set('0')
    varsc.set('0')
    vard.set('0')
    varcb.set('0')
    varls.set('0')
    varab.set('0')
    varpa.set('0')
    varcv.set('0')
    varcn.set('0')
    varmu.set('0')
    varci.set('0')
    varbl.set('0')
    varco.set('0')
    varcf.set('0')
    varfv.set('0')
    varfm.set('0')
    varce.set('0')
    varfa.set('0')
    vartax.set('0')
    varsub.set('0')
    vartotal.set('0')

    txtcsoup.configure(state=DISABLED)
    txthsoup.configure(state=DISABLED)
    txtssoup.configure(state=DISABLED)
    txtfsoup.configure(state=DISABLED)
    txtbc.configure(state=DISABLED)
    txtcc.configure(state=DISABLED)
    txtcs.configure(state=DISABLED)
    txtsc.configure(state=DISABLED)
    txtd.configure(state=DISABLED)
    txtcb.configure(state=DISABLED)
    txtls.configure(state=DISABLED)
    txtab.configure(state=DISABLED)
    txtpa.configure(state=DISABLED)
    txtcv.configure(state=DISABLED)
    txtcn.configure(state=DISABLED)
    txtmu.configure(state=DISABLED)
    txtci.configure(state=DISABLED)
    txtbl.configure(state=DISABLED)
    txtco.configure(state=DISABLED)
    txtcf.configure(state=DISABLED)
    txtfv.configure(state=DISABLED)
    txtfm.configure(state=DISABLED)
    txtce.configure(state=DISABLED)
    txtfa.configure(state=DISABLED)
    txttax.configure(state=DISABLED)
    txtsub.configure(state=DISABLED)
    txttotal.configure(state=DISABLED)

    pay.set('Cash')
    
def cost():
    d1=float(varcsoup.get())
    d2=float(varhsoup.get())
    d3=float(varssoup.get())
    d4=float(varfsoup.get())
    d5=float(varbc.get())
    d6=float(varcc.get())
    d7=float(varcs.get())
    d8=float(varsc.get())
    d9=float(vard.get())
    d10=float(varcb.get())
    d11=float(varls.get())
    d12=float(varab.get())
    d13=float(varpa.get())
    d14=float(varcv.get())
    d15=float(varcn.get())
    d16=float(varmu.get())
    d17=float(varci.get())
    d18=float(varbl.get())
    d19=float(varco.get())
    d20=float(varcf.get())
    d21=float(varfv.get())
    d22=float(varfm.get())
    d23=float(varce.get())
    d24=float(varfa.get())

    t1=(d1*450.00 + d2*400.00 + d3*300.00 + d4*350.00 + d5*600.00 + d6*450.00 + d7*500.00 + d8*550.00)
    t2=(d9*200.00 + d10*500.00 + d11*400.00 + d12*250.00 + d13*250.00 + d14*300.00 + d15*300.00 + d16*250.00)
    t3=(d17*400.00 + d18*400.00+ d19*400.00 + d20*400.00 + d21*300.00 + d22*250.00 + d23*200.00 + d24*350.00)

    cost1 = t1+t2+t3
    tax1 = (cost1 * 5)/100
    vartax.set(tax1)
    varsub.set(cost1)
    tot = cost1 + tax1
    vartotal.set(tot)


lblsoup = Label(f1,bg='#F7F1E5',fg='#E7B10A',font=('arial',18,'bold'), text='                      Soups            ')
lblsoup.grid(row=0,column=0)

def csoup():
    if (var1.get() == 1):
        txtcsoup.configure(state=NORMAL)
        varcsoup.set('1')
    elif (var1.get() == 0):
        txtcsoup.configure(state=DISABLED)
        varcsoup.set('0')

csoup = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s1,variable=var1,onvalue=1,offvalue=0,
                   font=('arial',18),command=csoup).grid(row=1,column=0,sticky=W)
lbl1 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='450',font=('arial',18)).grid(row=1,column=1)
txtcsoup = Entry(f1,font=('arial',18,'bold'),textvariable=varcsoup,width=3,justify='left',state=DISABLED)
txtcsoup.grid(row=1,column=2)

def hsoup():
    if (var2.get() == 1):
        txthsoup.configure(state=NORMAL)
        varhsoup.set('1')
    elif (var2.get() == 0):
        txthsoup.configure(state=DISABLED)
        varhsoup.set('0')
        
hsoup = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s2,variable=var2,onvalue=1,offvalue=0,
                   font=('arial',18),command=hsoup).grid(row=2,column=0,sticky=W)
lbl2 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='400',font=('arial',18)).grid(row=2,column=1)
txthsoup = Entry(f1,font=('arial',18,'bold'),textvariable=varhsoup,width=3,justify='left',state=DISABLED)
txthsoup.grid(row=2,column=2)

def ssoup():
    if (var3.get() == 1):
        txtssoup.configure(state=NORMAL)
        varssoup.set('1')
    elif (var3.get() == 0):
        txtssoup.configure(state=DISABLED)
        varssoup.set('0')
        
ssoup = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s3,variable=var3,onvalue=1,offvalue=0,
                   font=('arial',18),command=ssoup).grid(row=3,column=0,sticky=W)
lbl3 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='300',font=('arial',18)).grid(row=3,column=1)
txtssoup = Entry(f1,font=('arial',18,'bold'),textvariable=varssoup,width=3,justify='left',state=DISABLED)
txtssoup.grid(row=3,column=2)

def fsoup():
    if (var4.get() == 1):
        txtfsoup.configure(state=NORMAL)
        varfsoup.set('1')
    elif (var4.get() == 0):
        txtfsoup.configure(state=DISABLED)
        varfsoup.set('0')
        
fsoup = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s4,variable=var4,onvalue=1,offvalue=0,
                   font=('arial',18),command=fsoup).grid(row=4,column=0,sticky=W)
lbl4 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='350',font=('arial',18)).grid(row=4,column=1)
txtfsoup = Entry(f1,font=('arial',18,'bold'),textvariable=varfsoup,width=3,justify='left',state=DISABLED)
txtfsoup.grid(row=4,column=2)

lblstart = Label(f1,bg='#F7F1E5',fg='#E7B10A',font=('arial',18,'bold'), text='                     Starters            ')
lblstart.grid(row=6,column=0)

def bc():
    if (var5.get() == 1):
        txtbc.configure(state=NORMAL)
        varbc.set('1')
    elif (var5.get() == 0):
        txtbc.configure(state=DISABLED)
        varbc.set('0')
        
bc = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s5,variable=var5,onvalue=1,offvalue=0,
                   font=('arial',18),command=bc).grid(row=7,column=0,sticky=W)
lbl5 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='600',font=('arial',18)).grid(row=7,column=1)
txtbc = Entry(f1,font=('arial',18,'bold'),textvariable=varbc,width=3,justify='left',state=DISABLED)
txtbc.grid(row=7,column=2)

def cc():
    if (var6.get() == 1):
        txtcc.configure(state=NORMAL)
        varcc.set('1')

    elif (var6.get() == 0):
        txtcc.configure(state=DISABLED)
        varcc.set('0')
        
cc = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s6,variable=var6,onvalue=1,offvalue=0,
                   font=('arial',18),command=cc).grid(row=8,column=0,sticky=W)
lbl6 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='450',font=('arial',18)).grid(row=8,column=1)
txtcc = Entry(f1,font=('arial',18,'bold'),textvariable=varcc,width=3,justify='left',state=DISABLED)
txtcc.grid(row=8,column=2)

def cs():
    if (var7.get() == 1):
        txtcs.configure(state=NORMAL)
        varcs.set('1')
    elif (var7.get() == 0):
        txtcs.configure(state=DISABLED)
        varcs.set('0')
        
cs = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s7,variable=var7,onvalue=1,offvalue=0,
                   font=('arial',18),command=cs).grid(row=9,column=0,sticky=W)
lbl7 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='500',font=('arial',18)).grid(row=9,column=1)
txtcs = Entry(f1,font=('arial',18,'bold'),textvariable=varcs,width=3,justify='left',state=DISABLED)
txtcs.grid(row=9,column=2)

def sc():
    if (var8.get() == 1):
        txtsc.configure(state=NORMAL)
        varsc.set('1')
    elif (var8.get() == 0):
        txtsc.configure(state=DISABLED)
        varsc.set('0')
        
sc = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s8,variable=var8,onvalue=1,offvalue=0,
                   font=('arial',18),command=sc).grid(row=10,column=0,sticky=W)
lbl8 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='550',font=('arial',18)).grid(row=10,column=1)
txtsc = Entry(f1,font=('arial',18,'bold'),textvariable=varsc,width=3,justify='left',state=DISABLED)
txtsc.grid(row=10,column=2)

def d():
    if (var9.get() == 1):
        txtd.configure(state=NORMAL)
        vard.set('1')
    elif (var9.get() == 0):
        txtd.configure(state=DISABLED)
        vard.set('0')
        
d = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s9,variable=var9,onvalue=1,offvalue=0,
                   font=('arial',18),command=d).grid(row=11,column=0,sticky=W)
lbl9 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='200',font=('arial',18)).grid(row=11,column=1)
txtd = Entry(f1,font=('arial',18,'bold'),textvariable=vard,width=3,justify='left',state=DISABLED)
txtd.grid(row=11,column=2)

def cb():
    if (var10.get() == 1):
        txtcb.configure(state=NORMAL)
        varcb.set('1')
    elif (var10.get() == 0):
        txtcb.configure(state=DISABLED)
        varcb.set('0')
        
cb = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s10,variable=var10,onvalue=1,offvalue=0,
                   font=('arial',18),command=cb).grid(row=12,column=0,sticky=W)
lbl10 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='500',font=('arial',18)).grid(row=12,column=1)
txtcb = Entry(f1,font=('arial',18,'bold'),textvariable=varcb,width=3,justify='left',state=DISABLED)
txtcb.grid(row=12,column=2)

def ls():
    if (var11.get() == 1):
        txtls.configure(state=NORMAL)
        varls.set('1')
    elif (var11.get() == 0):
        txtls.configure(state=DISABLED)
        varls.set('0')
        
ls = Checkbutton(f1,bg='#F7F1E5',fg='#E7B10A',text=s11,variable=var11,onvalue=1,offvalue=0,
                   font=('arial',18),command=ls).grid(row=13,column=0,sticky=W)
lbl11 = Label(f1,bg='#F7F1E5',fg='#E7B10A',text='400',font=('arial',18)).grid(row=13,column=1)
txtls = Entry(f1,font=('arial',18,'bold'),textvariable=varls,width=3,justify='left',state=DISABLED)
txtls.grid(row=13,column=2)

lblspace = Label(f1,bg='#F7F1E5',text="\n")
lblspace.grid(row=14,column=0)

lbldrinks = Label(f2top,bg='#F7F1E5',fg='#E7B10A',font=('arial',18,'bold'), text='                          Drinks            ')
lbldrinks.grid(row=0,column=0)

def ab():
    if (var12.get() == 1):
        txtab.configure(state=NORMAL)
        varab.set('1')
    elif (var12.get() == 0):
        txtab.configure(state=DISABLED)
        varab.set('0')
        
ab = Checkbutton(f2top,bg='#F7F1E5',fg='#E7B10A',text=dr1,variable=var12,onvalue=1,offvalue=0,
                   font=('arial',18),command=ab).grid(row=1,column=0,sticky=W)
lbl12 = Label(f2top,bg='#F7F1E5',fg='#E7B10A',text='250',font=('arial',18)).grid(row=1,column=1)
txtab = Entry(f2top,font=('arial',18,'bold'),textvariable=varab,width=3,justify='left',state=DISABLED)
txtab.grid(row=1,column=2)

def pa():
    if (var13.get() == 1):
        txtpa.configure(state=NORMAL)
        varpa.set('1')
    elif (var13.get() == 0):
        txtpa.configure(state=DISABLED)
        varpa.set('0')

pa = Checkbutton(f2top,bg='#F7F1E5',fg='#E7B10A',text=dr2,variable=var13,onvalue=1,offvalue=0,
                   font=('arial',18),command=pa).grid(row=2,column=0,sticky=W)
lbl13 = Label(f2top,bg='#F7F1E5',fg='#E7B10A',text='250',font=('arial',18)).grid(row=2,column=1)
txtpa = Entry(f2top,font=('arial',18,'bold'),textvariable=varpa,width=3,justify='left',state=DISABLED)
txtpa.grid(row=2,column=2)

def cv():
    if (var14.get() == 1):
        txtcv.configure(state=NORMAL)
        varcv.set('1')
    elif (var14.get() == 0):
        txtcv.configure(state=DISABLED)
        varcv.set('0')
        
cv = Checkbutton(f2top,bg='#F7F1E5',fg='#E7B10A',text=dr3,variable=var14,onvalue=1,offvalue=0,
                   font=('arial',18),command=cv).grid(row=3,column=0,sticky=W)
lbl13 = Label(f2top,bg='#F7F1E5',fg='#E7B10A',text='300',font=('arial',18)).grid(row=3,column=1)
txtcv = Entry(f2top,font=('arial',18,'bold'),textvariable=varcv,width=3,justify='left',state=DISABLED)
txtcv.grid(row=3,column=2)

def cn():
    if (var15.get() == 1):
        txtcn.configure(state=NORMAL)
        varcn.set('1')
    elif (var15.get() == 0):
        txtcn.configure(state=DISABLED)
        varcn.set('0')
        
cn = Checkbutton(f2top,bg='#F7F1E5',fg='#E7B10A',text=dr4,variable=var15,onvalue=1,offvalue=0,
                   font=('arial',18),command=cn).grid(row=4,column=0,sticky=W)
lbl14 = Label(f2top,bg='#F7F1E5',fg='#E7B10A',text='300',font=('arial',18)).grid(row=4,column=1)
txtcn = Entry(f2top,font=('arial',18,'bold'),textvariable=varcn,width=3,justify='left',state=DISABLED)
txtcn.grid(row=4,column=2)

def mu():
    if (var16.get() == 1):
        txtmu.configure(state=NORMAL)
        varmu.set('1')
    elif (var16.get() == 0):
        txtmu.configure(state=DISABLED)
        varmu.set('0')
        
mu = Checkbutton(f2top,bg='#F7F1E5',fg='#E7B10A',text=dr5,variable=var16,onvalue=1,offvalue=0,
                   font=('arial',18),command=mu).grid(row=5,column=0,sticky=W)
lbl15 = Label(f2top,bg='#F7F1E5',fg='#E7B10A',text='250',font=('arial',18)).grid(row=5,column=1)
txtmu = Entry(f2top,font=('arial',18,'bold'),textvariable=varmu,width=3,justify='left',state=DISABLED)
txtmu.grid(row=5,column=2)


lbldessert = Label(f3,bg='#F7F1E5',fg='#E7B10A',font=('arial',18,'bold'), text='                          Desserts            ')
lbldessert.grid(row=0,column=0)

def ci():
    if (var19.get() == 1):
        txtci.configure(state=NORMAL)
        varci.set('1')    
    elif (var19.get() == 0):
        txtci.configure(state=DISABLED)
        varci.set('0')
        
ci = Checkbutton(f3,bg='#F7F1E5',fg='#E7B10A',text=ds1,variable=var19,onvalue=1,offvalue=0,
                   font=('arial',18),command=ci).grid(row=1,column=0,sticky=W)
lbl16 = Label(f3,bg='#F7F1E5',fg='#E7B10A',text='400',font=('arial',18)).grid(row=1,column=1)
txtci = Entry(f3,font=('arial',18,'bold'),textvariable=varci,width=3,justify='left',state=DISABLED)
txtci.grid(row=1,column=2)

def bl():
    if (var20.get() == 1):
        txtbl.configure(state=NORMAL)
        varbl.set('1')
    elif (var20.get() == 0):
        txtbl.configure(state=DISABLED)
        varbl.set('0')
        
bl = Checkbutton(f3,bg='#F7F1E5',fg='#E7B10A',text=ds2,variable=var20,onvalue=1,offvalue=0,
                   font=('arial',18),comman=bl).grid(row=2,column=0,sticky=W)
lbl17 = Label(f3,bg='#F7F1E5',fg='#E7B10A',text='400',font=('arial',18)).grid(row=2,column=1)
txtbl = Entry(f3,font=('arial',18,'bold'),textvariable=varbl,width=3,justify='left',state=DISABLED)
txtbl.grid(row=2,column=2)

def co():
    if (var21.get() == 1):
        txtco.configure(state=NORMAL)
        varco.set('1')
    elif (var21.get() == 0):
        txtco.configure(state=DISABLED)
        varco.set('0')
        
co = Checkbutton(f3,bg='#F7F1E5',fg='#E7B10A',text=ds3,variable=var21,onvalue=1,offvalue=0,
                   font=('arial',18),command=co).grid(row=3,column=0,sticky=W)
lbl17 = Label(f3,bg='#F7F1E5',fg='#E7B10A',text='400',font=('arial',18)).grid(row=3,column=1)
txtco = Entry(f3,font=('arial',18,'bold'),textvariable=varco,width=3,justify='left',state=DISABLED)
txtco.grid(row=3,column=2)

def cf():
    if (var22.get() == 1):
        txtcf.configure(state=NORMAL)
        varcf.set('1')
    elif (var22.get() == 0):
        txtcf.configure(state=DISABLED)
        varcf.set('0')
        
cf = Checkbutton(f3,bg='#F7F1E5',fg='#E7B10A',text=ds4,variable=var22,onvalue=1,offvalue=0,
                   font=('arial',18),command=cf).grid(row=4,column=0,sticky=W)
lbl18 = Label(f3,bg='#F7F1E5',fg='#E7B10A',text='400',font=('arial',18)).grid(row=4,column=1)
txtcf = Entry(f3,font=('arial',18,'bold'),textvariable=varcf,width=3,justify='left',state=DISABLED)
txtcf.grid(row=4,column=2)

lblshakes = Label(f3,bg='#F7F1E5',fg='#E7B10A',font=('arial',18,'bold'), text='                           Shakes            ')
lblshakes.grid(row=6,column=0)

def fv():
    if (var23.get() == 1):
        txtfv.configure(state=NORMAL)
        varfv.set('1')
    elif (var23.get() == 0):
        txtfv.configure(state=DISABLED)
        varfv.set('0')

fv = Checkbutton(f3,bg='#F7F1E5',fg='#E7B10A',text=sh1,variable=var23,onvalue=1,offvalue=0,
                   font=('arial',18),command=fv).grid(row=7,column=0,sticky=W)
lbl19 = Label(f3,bg='#F7F1E5',fg='#E7B10A',text='300',font=('arial',18)).grid(row=7,column=1)
txtfv = Entry(f3,font=('arial',18,'bold'),textvariable=varfv,width=3,justify='left',state=DISABLED)
txtfv.grid(row=7,column=2)

def fm():
    if (var24.get() == 1):
        txtfm.configure(state=NORMAL)
        varfm.set('1')
    elif (var24.get() == 0):
        txtfm.configure(state=DISABLED)
        varfm.set('0')
        
fm = Checkbutton(f3,bg='#F7F1E5',fg='#E7B10A',text=sh2,variable=var24,onvalue=1,offvalue=0,
                   font=('arial',18),command=fm).grid(row=8,column=0,sticky=W)
lbl20 = Label(f3,bg='#F7F1E5',fg='#E7B10A',text='250',font=('arial',18)).grid(row=8,column=1)
txtfm = Entry(f3,font=('arial',18,'bold'),textvariable=varfm,width=3,justify='left',state=DISABLED)
txtfm.grid(row=8,column=2)

def ce():
    if (var25.get() == 1):
        txtce.configure(state=NORMAL)
        varce.set('1')
    elif (var25.get() == 0):
        txtce.configure(state=DISABLED)
        varce.set('0')
        
ce = Checkbutton(f3,bg='#F7F1E5',fg='#E7B10A',text=sh3,variable=var25,onvalue=1,offvalue=0,
                   font=('arial',18),command=ce).grid(row=9,column=0,sticky=W)
lbl21 = Label(f3,bg='#F7F1E5',fg='#E7B10A',text='200',font=('arial',18)).grid(row=9,column=1)
txtce = Entry(f3,font=('arial',18,'bold'),textvariable=varce,width=3,justify='left',state=DISABLED)
txtce.grid(row=9,column=2)

def fa():
    if (var26.get() == 1):
        txtfa.configure(state=NORMAL)
        varfa.set('1')
    elif (var26.get() == 0):
        txtfa.configure(state=DISABLED)
        varfa.set('0')
        
fa = Checkbutton(f3,bg='#F7F1E5',fg='#E7B10A',text=sh4,variable=var26,onvalue=1,offvalue=0,
                   font=('arial',18),command=fa).grid(row=10,column=0,sticky=W)
lbl16 = Label(f3,bg='#F7F1E5',fg='#E7B10A',text='350',font=('arial',18)).grid(row=10,column=1)
txtfa = Entry(f3,font=('arial',18,'bold'),textvariable=varfa,width=3,justify='left',state=DISABLED)
txtfa.grid(row=10,column=2)

lblspace = Label(f3,bg='#F7F1E5',fg='#E7B10A',text="\n\n\n\n\n")
lblspace.grid(row=17,column=0)

lblspace = Label(f2bottom,bg='#F7F1E5',fg='#E7B10A',text="\n\n\n\n")
lblspace.grid(row=4,column=0)

lblpay = Label(f2bottom,bg='#F7F1E5',fg='#E7B10A',font=('arial',14,'bold'),text="Payment Method",bd=10,width=16,anchor='w')
lblpay.grid(row=0,column=0)

pay = ttk.Combobox(f2bottom,textvariable=var27,state='readonly',font=('arial',10,'bold'),width=20)
pay['value'] = ('Cash','Credit card','Debit card','UPI')
pay.set('Cash')
pay.grid(row=1,column=0)

lbltax = Label(f2bottom,bg='#F7F1E5',fg='#E7B10A',font=('arial',14,'bold'),text='Tax',bd=10,anchor='w')
lbltax.grid(row=1,column=1)
txttax = Entry(f2bottom,font=('arial',18,'bold'),textvariable=vartax,width=10,justify='left',state=DISABLED)
txttax.grid(row=1,column=2)

lblsub = Label(f2bottom,bg='#F7F1E5',fg='#E7B10A',font=('arial',14,'bold'),text='Sub Total',bd=10,anchor='w')
lblsub.grid(row=2,column=1)
txtsub = Entry(f2bottom,font=('arial',18,'bold'),textvariable=varsub,width=10,justify='left',state=DISABLED)
txtsub.grid(row=2,column=2)

lbltotal = Label(f2bottom,bg='#F7F1E5',fg='#E7B10A',font=('arial',14,'bold'),text='Total',bd=10,anchor='w')
lbltotal.grid(row=3,column=1)
txttotal = Entry(f2bottom,font=('arial',18,'bold'),textvariable=vartotal,width=10,justify='left',state=DISABLED)
txttotal.grid(row=3,column=2)

btotal = Button(f2bottom,padx=16,pady=1,bd=4,bg='#E7B10A',fg='#F7F1E5',font=('arial',16,'bold'),width=5,
                text='Total',command=cost).place(x=50,y=200)
breset = Button(f2bottom,padx=16,pady=1,bd=4,bg='#E7B10A',fg='#F7F1E5',font=('arial',16,'bold'),width=5,
                text='Reset',command=reset).place(x=190,y=200)

def exit1():
    e=messagebox.askyesno("Pick n Pay","Do you want to exit ?")
    if e>0:
        window.destroy()
        return

bexit = Button(f2bottom,padx=16,pady=1,bd=4,bg='#E7B10A',fg='#F7F1E5',font=('arial',16,'bold'),width=5,
                text='Exit',command=exit1).place(x=330,y=200)

def conf():
    try:
        all_food[s1]=varcsoup.get()
        all_food[s2]=varhsoup.get()
        all_food[s3]=varssoup.get()
        all_food[s4]=varfsoup.get()
        all_food[s5]=varbc.get()
        all_food[s6]=varcc.get()
        all_food[s7]=varcs.get()
        all_food[s8]=varsc.get()
        all_food[s9]=vard.get()
        all_food[s10]=varcb.get()
        all_food[s11]=varls.get()
        all_food[dr1]=varab.get()
        all_food[dr2]=varpa.get()
        all_food[dr3]=varcv.get()
        all_food[dr4]=varcn.get()
        all_food[dr5]=varmu.get()
        all_food[ds1]=varci.get()
        all_food[ds2]=varbl.get()
        all_food[ds3]=varco.get()
        all_food[ds4]=varcf.get()
        all_food[sh1]=varfv.get()
        all_food[sh2]=varfm.get()
        all_food[sh3]=varce.get()
        all_food[sh4]=varfa.get()
        for key, value in all_food.items():
            if value != '0':
                selected_food[key]=value
            else:
                pass
        rand = random.randint(100,999)
        table_name = "ord_" + str(rand)
        q1 = "create table if not exists {} (food_name varchar(255), quantity int)".format(table_name)
        b.execute(q1)
        for food,quant in selected_food.items():
            b.execute(f"insert into {table_name} (food_name,quantity) values ('{food}',{quant})", {"food_name":food, "quantity":quant})
        conf=messagebox.showinfo("Pick n Pay","Your order number is {}.\nYou will receive your order soon !".format(rand))
        a.commit();
        reset()
    except:
        conf=messagebox.showerror("Pick n Pay","Database error !\nRetry ordering !")

def view():
    l=[]
    b.execute("use fastfood")
    b.execute("show tables")
    data = b.fetchall()
    for i in data:
        l.append(i[0])
    curr = Tk()
    curr.title("Current orders")
    curr.config(bg='#F7F1E5')
    buttons=[IntVar(curr) for i in range(len(l))]
    for i in range(len(l)):
        chk_btn = Checkbutton(curr,bg='#F7F1E5',fg='#E7B10A',onvalue=1,offvalue=0,font=('arial',12), variable=buttons[i])
        chk_btn.grid(row=i,column=0)
        chk_btn.config(text=l[i])   

    def deltab():
        widgets = curr.winfo_children()
        for i in range(len(l)):
            if buttons[i].get()==1:
                query=f"drop table if exists {l[i]}"
                b.execute(query)
                a.commit()
        curr.destroy()

    bok = Button(curr, bg='#E7B10A',fg='#F7F1E5', text="Ok", command=deltab)
    bok.grid(row=len(l), column=0)
        
bconf = Button(f3,padx=16,pady=1,bd=4,bg='#E7B10A',fg='#F7F1E5',font=('arial',16,'bold'),width=5,
                text='Confirm',command=conf).place(x=180,y=400)

bcurr = Button(f3,padx=16,pady=1,bd=4,bg='#E7B10A',fg='#F7F1E5',font=('arial',8,'bold'),width=10,
                text='View Orders',command=view).place(x=178,y=470)


window.mainloop()
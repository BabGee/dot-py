from tkinter import *
from tkinter import messagebox

from math import sqrt

root = Tk()
root.title("Mean")
root.geometry("1000x600+0+0")
root.config(bg="black")

#***************************************VARIABLES************************************
var1 = IntVar()
var1.set(0)
var2 = IntVar()
var2.set(0)
var3 = IntVar()
var3.set(0)
var4 = IntVar()
var4.set(0)
var5 = IntVar()
var5.set(0)
var6 = IntVar()
var6.set(0)
var7 = IntVar()
var7.set(0)
var8 = IntVar()
var8.set(0)
var9 = IntVar()
var9.set(0)
var10 = IntVar()
var10.set(0)

ed1 = StringVar()
ed1.set("0")
ed2 = StringVar()
ed2.set("0")
ed3 = StringVar()
ed3.set("0")
ed4 = StringVar()
ed4.set("0")
ed5 = StringVar()
ed5.set("0")
ed6 = StringVar()
ed6.set("0")
ed7 = StringVar()
ed7.set("0")
ed8 = StringVar()
ed8.set("0")
ed9 = StringVar()
ed9.set("0")
ed10 = StringVar()
ed10.set("0")

ef1 = StringVar()
ef1.set("0")
ef2 = StringVar()
ef2.set("0")
ef3 = StringVar()
ef3.set("0")
ef4 = StringVar()
ef4.set("0")
ef5 = StringVar()
ef5.set("0")
ef6 = StringVar()
ef6.set("0")
ef7 = StringVar()
ef7.set("0")
ef8 = StringVar()
ef8.set("0")
ef9 = StringVar()
ef9.set("0")
ef10 = StringVar()
ef10.set("0")

exf1 = StringVar()
exf1.set("0")
exf2 = StringVar()
exf2.set("0")
exf3 = StringVar()
exf3.set("0")
exf4 = StringVar()
exf4.set("0")
exf5 = StringVar()
exf5.set("0")
exf6 = StringVar()
exf6.set("0")
exf7 = StringVar()
exf7.set("0")
exf8 = StringVar()
exf8.set("0")
exf9 = StringVar()
exf9.set("0")
exf10 = StringVar()
exf10.set("0")

edvsqf1 = StringVar()
edvsqf1.set("0")
edvsqf2 = StringVar()
edvsqf2.set("0")
edvsqf3 = StringVar()
edvsqf3.set("0")
edvsqf4 = StringVar()
edvsqf4.set("0")
edvsqf5 = StringVar()
edvsqf5.set("0")
edvsqf6 = StringVar()
edvsqf6.set("0")
edvsqf7 = StringVar()
edvsqf7.set("0")
edvsqf8 = StringVar()
edvsqf8.set("0")
edvsqf9 = StringVar()
edvsqf9.set("0")
edvsqf10 = StringVar()
edvsqf10.set("0")

eu = StringVar()
eu.set("0")

er = StringVar()
er.set("0")

ev = StringVar()
ev.set("0")

em = StringVar()
em.set("0")

#***************************************FUNCTIONS************************************

def checkBtn():
	if var1.get() > 0:
		d1.config(state=NORMAL)
		f1.config(state=NORMAL)
		xf1.config(state=NORMAL)
		dvsqf1.config(state=NORMAL)
	else:
		d1.config(state=DISABLED)
		ed1.set("0")
		f1.config(state=DISABLED)
		ef1.set("0")
		xf1.config(state=DISABLED)
		exf1.set("0")
		dvsqf1.config(state=DISABLED)
		edvsqf1.set("0")
		
	if var2.get() > 0:
		d2.config(state=NORMAL)
		f2.config(state=NORMAL)
		xf2.config(state=NORMAL)
		dvsqf2.config(state=NORMAL)
	else:
		d2.config(state=DISABLED)
		ed2.set("0")
		f2.config(state=DISABLED)
		ef2.set("0")
		xf2.config(state=DISABLED)
		exf2.set("0")
		dvsqf2.config(state=DISABLED)
		edvsqf2.set("0")	
	
	if var3.get() > 0:
		d3.config(state=NORMAL)
		f3.config(state=NORMAL)
		xf3.config(state=NORMAL)
		dvsqf3.config(state=NORMAL)
	else:
		d3.config(state=DISABLED)
		ed3.set("0")
		f3.config(state=DISABLED)
		ef3.set("0")
		xf3.config(state=DISABLED)
		exf3.set("0")
		dvsqf3.config(state=DISABLED)
		edvsqf3.set("0")

	if var4.get() > 0:
		d4.config(state=NORMAL)
		f4.config(state=NORMAL)
		xf4.config(state=NORMAL)
		dvsqf4.config(state=NORMAL)
	else:
		d4.config(state=DISABLED)
		ed4.set("0")
		f4.config(state=DISABLED)
		ef4.set("0")
		xf4.config(state=DISABLED)
		exf4.set("0")
		dvsqf4.config(state=DISABLED)
		edvsqf4.set("0")
		
	if var5.get() > 0:
		d5.config(state=NORMAL)
		f5.config(state=NORMAL)
		xf5.config(state=NORMAL)
		dvsqf5.config(state=NORMAL)
	else:
		d5.config(state=DISABLED)
		ed5.set("0")
		f5.config(state=DISABLED)
		ef5.set("0")
		xf5.config(state=DISABLED)
		exf5.set("0")
		dvsqf5.config(state=DISABLED)
		edvsqf5.set("0")

	if var6.get() > 0:
		d6.config(state=NORMAL)
		f6.config(state=NORMAL)
		xf6.config(state=NORMAL)
		dvsqf6.config(state=NORMAL)
	else:
		d6.config(state=DISABLED)
		ed6.set("0")
		f6.config(state=DISABLED)
		ef6.set("0")
		xf6.config(state=DISABLED)
		exf6.set("0")
		dvsqf6.config(state=DISABLED)
		edvsqf6.set("0")		

	if var7.get() > 0:
		d7.config(state=NORMAL)
		f7.config(state=NORMAL)
		xf7.config(state=NORMAL)
		dvsqf7.config(state=NORMAL)
	else:
		d7.config(state=DISABLED)
		ed7.set("0")
		f7.config(state=DISABLED)
		ef7.set("0")
		xf7.config(state=DISABLED)
		exf7.set("0")
		dvsqf7.config(state=DISABLED)
		edvsqf7.set("0")

	if var8.get() > 0:
		d8.config(state=NORMAL)
		f8.config(state=NORMAL)
		xf8.config(state=NORMAL)
		dvsqf8.config(state=NORMAL)
	else:
		d8.config(state=DISABLED)
		ed8.set("0")
		f8.config(state=DISABLED)
		ef8.set("0")
		xf8.config(state=DISABLED)
		exf8.set("0")
		dvsqf8.config(state=DISABLED)
		edvsqf8.set("0")

	if var9.get() > 0:
		d9.config(state=NORMAL)
		f9.config(state=NORMAL)
		xf9.config(state=NORMAL)
		dvsqf9.config(state=NORMAL)
	else:
		d9.config(state=DISABLED)
		ed9.set("0")
		f9.config(state=DISABLED)
		ef9.set("0")
		xf9.config(state=DISABLED)
		exf9.set("0")
		dvsqf9.config(state=DISABLED)
		edvsqf9.set("0")
	
	if var10.get() > 0:
		d10.config(state=NORMAL)
		f10.config(state=NORMAL)
		xf10.config(state=NORMAL)
		dvsqf10.config(state=NORMAL)
	else:
		d10.config(state=DISABLED)
		ed10.set("0")
		f10.config(state=DISABLED)
		ef10.set("0")
		xf10.config(state=DISABLED)
		exf10.set("0")
		dvsqf10.config(state=DISABLED)
		edvsqf10.set("0")
		
		
def quit():
	Quit = messagebox.askyesno("Quit System", "Do You Want to quit?")
	if Quit > 0:
		root.destroy()
		return

def reset():
	var1.set("0")
	var2.set("0")
	var3.set("0")
	var4.set("0")
	var5.set("0")
	var6.set("0")
	var7.set("0")
	var8.set("0")
	var9.set("0")
	var10.set("0")
	
	d1.config(state=DISABLED)
	ed1.set("0")
	f1.config(state=DISABLED)
	ef1.set("0")
	xf1.config(state=DISABLED)
	exf1.set("0")
	dvsqf1.config(state=DISABLED)
	edvsqf1.set("0")

	d2.config(state=DISABLED)
	ed2.set("0")
	f2.config(state=DISABLED)
	ef2.set("0")
	xf2.config(state=DISABLED)
	exf2.set("0")
	dvsqf2.config(state=DISABLED)
	edvsqf2.set("0")

	d3.config(state=DISABLED)
	ed3.set("0")
	f3.config(state=DISABLED)
	ef3.set("0")
	xf3.config(state=DISABLED)
	exf3.set("0")
	dvsqf3.config(state=DISABLED)
	edvsqf3.set("0")
	
	d4.config(state=DISABLED)
	ed4.set("0")
	f4.config(state=DISABLED)
	ef4.set("0")
	xf4.config(state=DISABLED)
	exf4.set("0")
	dvsqf4.config(state=DISABLED)
	edvsqf4.set("0")
	
	d5.config(state=DISABLED)
	ed5.set("0")
	f5.config(state=DISABLED)
	ef5.set("0")
	xf5.config(state=DISABLED)
	exf5.set("0")
	dvsqf5.config(state=DISABLED)
	edvsqf5.set("0")
	
	d6.config(state=DISABLED)
	ed6.set("0")
	f6.config(state=DISABLED)
	ef6.set("0")
	xf6.config(state=DISABLED)
	exf6.set("0")
	dvsqf6.config(state=DISABLED)
	edvsqf6.set("0")
	
	d7.config(state=DISABLED)
	ed7.set("0")
	f7.config(state=DISABLED)
	ef7.set("0")
	xf7.config(state=DISABLED)
	exf7.set("0")
	dvsqf7.config(state=DISABLED)
	edvsqf7.set("0")
	
	d8.config(state=DISABLED)
	ed8.set("0")
	f8.config(state=DISABLED)
	ef8.set("0")
	xf8.config(state=DISABLED)
	exf8.set("0")
	dvsqf8.config(state=DISABLED)
	edvsqf8.set("0")
	
	d9.config(state=DISABLED)
	ed9.set("0")
	f9.config(state=DISABLED)
	ef9.set("0")
	xf9.config(state=DISABLED)
	exf9.set("0")
	dvsqf9.config(state=DISABLED)
	edvsqf9.set("0")
	
	d10.config(state=DISABLED)
	ed10.set("0")
	f10.config(state=DISABLED)
	ef10.set("0")
	xf10.config(state=DISABLED)
	exf10.set("0")
	dvsqf10.config(state=DISABLED)
	edvsqf10.set("0")
	
	u.config(state=DISABLED)
	eu.set("0")
	r.config(state=DISABLED)
	er.set("0")
	v.config(state=DISABLED)
	ev.set("0")
	
	m.config(state=DISABLED)
	em.set("0")


def calculate():	
	u.config(state=NORMAL)
	r.config(state=NORMAL)
	v.config(state=NORMAL)
	m.config(state=NORMAL)
		
	try:	
		data1 = float(d1.get())	
		data2 = float(d2.get())
		data3 = float(d3.get())
		data4 = float(d4.get())	
		data5 = float(d5.get())
		data6 = float(d6.get())
		data7 = float(d7.get())
		data8 = float(d8.get())	
		data9 = float(d9.get())
		data10 = float(d10.get())
		dataList=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
		
		freq1 = int(f1.get())
		freq2 = int(f2.get())
		freq3 = int(f3.get())
		freq4 = int(f4.get())
		freq5 = int(f5.get())
		freq6 = int(f6.get())
		freq7 = int(f7.get())
		freq8 = int(f8.get())
		freq9 = int(f9.get())
		freq10 = int(f10.get())
		freqList=[freq1,freq2,freq3,freq4,freq5,freq6,freq7,freq8,freq9,freq10]	
	
		freqList.sort(reverse=True)
		
		if freqList[0] == freq1:
			em.set(int(data1))
		elif freqList[0] == freq2:
			em.set(int(data2))
		elif freqList[0] == freq3:
			em.set(int(data3))
		elif freqList[0] == freq4:
			em.set(int(data4))		
		elif freqList[0] == freq5:
			em.set(int(data5))
		elif freqList[0] == freq6:
			em.set(int(data6))
		elif freqList[0] == freq7:
			em.set(int(data7))
		elif freqList[0] == freq8:
			em.set(int(data8))
		elif freqList[0] == freq9:
			em.set(int(data9))
		elif freqList[0] == freq10:
			em.set(int(data10))
			
		pxf1 = data1 * freq1
		exf1.set(pxf1)
		pxf2 = data2 * freq2
		exf2.set(pxf2)
		pxf3 = data3 * freq3
		exf3.set(pxf3)
		pxf4 = data4 * freq4
		exf4.set(pxf4)
		pxf5 = data5 * freq5
		exf5.set(pxf5)
		pxf6 = data6 * freq6
		exf6.set(pxf6)
		pxf7 = data7 * freq7
		exf7.set(pxf7)
		pxf8 = data8 * freq8
		exf8.set(pxf8)
		pxf9 = data9 * freq9
		exf9.set(pxf9)
		pxf10 = data10 * freq10
		exf10.set(pxf10)
		
		sumxf = pxf1+pxf2+pxf3+pxf4+pxf5+pxf6+pxf7+pxf8+pxf9+pxf10
		sumf = float(freq1+freq2+freq3+freq4+freq5+freq6+freq7+freq8+freq9+freq10)
		
		mean = sumxf/sumf
		eu.set(mean)
		
		dev1 = data1 - mean
		devsq1 = dev1 * dev1
		devsqf1 = devsq1 * freq1
		edvsqf1.set(devsqf1)
		
		dev2 = data2 - mean
		devsq2 = dev2 * dev2
		devsqf2 = devsq2 * freq2
		edvsqf2.set(devsqf2)
		
		dev3 = data3 - mean
		devsq3 = dev3 * dev3
		devsqf3 = devsq3 * freq3
		edvsqf3.set(devsqf3)
		
		dev4 = data4 - mean
		devsq4 = dev4 * dev4
		devsqf4 = devsq4 * freq4
		edvsqf4.set(devsqf4)
		
		dev4 = data4 - mean
		devsq4 = dev4 * dev4
		devsqf4 = devsq4 * freq4
		edvsqf4.set(devsqf4)
		
		dev5 = data5 - mean
		devsq5 = dev5 * dev5
		devsqf5 = devsq5 * freq5
		edvsqf5.set(devsqf5)
		
		dev6 = data6 - mean
		devsq6 = dev6 * dev6
		devsqf6 = devsq6 * freq6
		edvsqf6.set(devsqf6)
		
		dev7 = data7 - mean
		devsq7 = dev7 * dev7
		devsqf7 = devsq7 * freq7
		edvsqf7.set(devsqf7)
		
		dev8 = data8 - mean
		devsq8 = dev8 * dev8
		devsqf8 = devsq8 * freq8
		edvsqf8.set(devsqf8)
		
		dev9 = data9 - mean
		devsq9 = dev9 * dev9
		devsqf9 = devsq9 * freq9
		edvsqf9.set(devsqf9)
		
		dev10 = data10 - mean
		devsq10 = dev10 * dev10
		devsqf10 = devsq10 * freq10
		edvsqf10.set(devsqf10)
		
		sumDevsqf = devsqf1+devsqf2+devsqf3+devsqf4+devsqf5+devsqf6+devsqf7+devsqf8+devsqf9+devsqf10
		standardDev = sumDevsqf/sumf
		er.set(standardDev)
		
		variance = sqrt(standardDev)
		ev.set(variance)
	except Exception as error:
		ed1.set("0")
		ed2.set("0")
		ed3.set("0")
		ed4.set("0")
		ed5.set("0")
		ed6.set("0")
		ef7.set("0")
		ed8.set("0")
		ed9.set("0")
		ed10.set("0")
		
		ef1.set("0")
		ef2.set("0")
		ef3.set("0")
		ef4.set("0")
		ef5.set("0")
		ef6.set("0")
		ef7.set("0")
		ef8.set("0")
		ef9.set("0")
		ef10.set("0")
		
	
#***************************************LABELS************************************

Label(root, text="  DATA(x)  ", font=("arial black", 13, "bold"), fg="cadet blue", bd=12).grid(row=0, column=1)
Label(root, text="  Frequency(f)  ", font=("arial black", 13, "bold"), fg="cadet blue", bd=12).grid(row=0, column=2)
Label(root, text="  xf  ", font=("arial black", 13, "bold"), fg="cadet blue", bd=12).grid(row=0, column=3)
Label(root, text="  dvsqf  ", font=("arial black", 13, "bold"), fg="cadet blue", bd=12).grid(row=0, column=4)
Label(root, text="  Mean(u)  ", font=("arial black", 13, "bold"), fg="cadet blue", bd=12).grid(row=11, column=1)
Label(root, text="  Standard deviation(r)  ", font=("arial black", 13, "bold"), fg="cadet blue", bd=12).grid(row=11, column=2)
Label(root, text="  Variance(v)  ", font=("arial black", 13, "bold"), fg="cadet blue", bd=12).grid(row=11, column=3)
Label(root, text="  Mode  ", font=("arial black", 13, "bold"), fg="cadet blue", bd=12).grid(row=11, column=4)

#***************************************CHECKBUTTONS************************************

checkd1 = Checkbutton(root, text=" 1 ", variable=var1, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=1,column=0)

checkd1 = Checkbutton(root, text=" 2 ", variable=var2, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=2,column=0)

checkd1 = Checkbutton(root, text=" 3 ", variable=var3, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=3,column=0)

checkd1 = Checkbutton(root, text=" 4 ", variable=var4, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=4,column=0)

checkd1 = Checkbutton(root, text=" 5 ", variable=var5, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=5,column=0)

checkd1 = Checkbutton(root, text=" 6 ", variable=var6, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=6,column=0)

checkd1 = Checkbutton(root, text=" 7 ", variable=var7, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=7,column=0)

checkd1 = Checkbutton(root, text=" 8 ", variable=var8, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=8,column=0)

checkd1 = Checkbutton(root, text=" 9 ", variable=var9, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=9,column=0)

checkd1 = Checkbutton(root, text=" 10 ", variable=var10, onvalue=1, offvalue=0, command=checkBtn,font=("COURIER", 13, "bold"), bd=8)
checkd1.grid(row=10,column=0)


#***************************************ENTRY************************************

d1 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed1, state=DISABLED)
d1.grid(row=1, column=1)

d2 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed2, state=DISABLED)
d2.grid(row=2, column=1)

d3 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed3, state=DISABLED)
d3.grid(row=3, column=1)

d4 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed4, state=DISABLED)
d4.grid(row=4, column=1)

d5 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed5, state=DISABLED)
d5.grid(row=5, column=1)

d6 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed6, state=DISABLED)
d6.grid(row=6, column=1)

d7 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed7, state=DISABLED)
d7.grid(row=7, column=1)

d8 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed8, state=DISABLED)
d8.grid(row=8, column=1)

d9 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed9, state=DISABLED)
d9.grid(row=9, column=1)

d10 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ed10, state=DISABLED)
d10.grid(row=10, column=1)


f1 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef1, state=DISABLED)
f1.grid(row=1, column=2)

f2 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef2, state=DISABLED)
f2.grid(row=2, column=2)

f3 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef3, state=DISABLED)
f3.grid(row=3, column=2)

f4 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef4, state=DISABLED)
f4.grid(row=4, column=2)

f5 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef5, state=DISABLED)
f5.grid(row=5, column=2)

f6 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef6, state=DISABLED)
f6.grid(row=6, column=2)

f7 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef7, state=DISABLED)
f7.grid(row=7, column=2)

f8 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef8, state=DISABLED)
f8.grid(row=8, column=2)

f9 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef9, state=DISABLED)
f9.grid(row=9, column=2)

f10 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ef10, state=DISABLED)
f10.grid(row=10, column=2)

xf1 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf1, state=DISABLED)
xf1.grid(row=1, column=3)

xf2 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf2, state=DISABLED)
xf2.grid(row=2, column=3)

xf3 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf3, state=DISABLED)
xf3.grid(row=3, column=3)

xf4 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf4, state=DISABLED)
xf4.grid(row=4, column=3)

xf5 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf5, state=DISABLED)
xf5.grid(row=5, column=3)

xf6 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf6, state=DISABLED)
xf6.grid(row=6, column=3)

xf7 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf7, state=DISABLED)
xf7.grid(row=7, column=3)

xf8 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf8, state=DISABLED)
xf8.grid(row=8, column=3)

xf9 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf9, state=DISABLED)
xf9.grid(row=9, column=3)

xf10 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=exf10, state=DISABLED)
xf10.grid(row=10, column=3)


dvsqf1 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf1, state=DISABLED)
dvsqf1.grid(row=1, column=4)

dvsqf2 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf2, state=DISABLED)
dvsqf2.grid(row=2, column=4)

dvsqf3 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf3, state=DISABLED)
dvsqf3.grid(row=3, column=4)

dvsqf4 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf4, state=DISABLED)
dvsqf4.grid(row=4, column=4)

dvsqf5 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf5, state=DISABLED)
dvsqf5.grid(row=5, column=4)

dvsqf6 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf6, state=DISABLED)
dvsqf6.grid(row=6, column=4)

dvsqf7 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf7, state=DISABLED)
dvsqf7.grid(row=7, column=4)

dvsqf8 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf8, state=DISABLED)
dvsqf8.grid(row=8, column=4)

dvsqf9 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf9, state=DISABLED)
dvsqf9.grid(row=9, column=4)

dvsqf10 = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=edvsqf10, state=DISABLED)
dvsqf10.grid(row=10, column=4)


u = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=eu, state=DISABLED)
u.grid(row=12, column=1)

r = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=er, state=DISABLED)
r.grid(row=12, column=2)

v = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=ev, state=DISABLED)
v.grid(row=12, column=3)

m = Entry(root, width=8, bd=6, font=("arial black", 13, "bold"), fg="cadet blue", textvariable=em, state=DISABLED)
m.grid(row=12, column=4)

#***************************************BUTTONS************************************

Button(root, text="Calculate", command=calculate, bd=8, font=("arial black", 13, "bold"), fg="cadet blue", padx=2, pady=2).grid(row=11,column=0)

Button(root, text=" Reset ", command=reset, bd=8, font=("arial black", 13, "bold"), fg="cadet blue", padx=2, pady=2).grid(row=12,column=0)

#Button(root, text=" Reset ", command=reset, bd=8, font=("arial black", 13, "bold"), fg="cadet blue", padx=2, pady=2).grid(row=13,column=0)
Button(root, text=" Exit ", command=quit, bd=8, font=("arial black", 13, "bold"), fg="red", padx=2, pady=2).grid(row=0,column=0)












root.mainloop()
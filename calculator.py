from tkinter import *

root=Tk()
root.title('Calculator')
root.geometry('1500x850+0+0')
root.config(bg='sky blue')

textInput=StringVar()
operator=''

def click(number):
	global operator
	operator+=str(number)
	textInput.set(operator)
	
def Clear():
	global operator
	operator=''
	textInput.set(operator)
	
def Equals():
	global operator
	sumup=str(eval(operator))
	textInput.set(sumup)
	operator=''
	
#======textEntry====

txtDisplay=Entry(root,justify=RIGHT,textvariable=textInput,font=('courier',12,'bold'))
txtDisplay.grid(columnspan=4)

#=====1st row buttons====

btn7=Button(root,text='7',command=lambda:click(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text='8',command=lambda:click(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text='9',command=lambda:click(9))
btn9.grid(row=1,column=2)
addition=Button(root,text='+',command=lambda:click('+'))
addition.grid(row=1,column=3)

#=====2nd row buttons====

btn4=Button(root,text='4',command=lambda:click(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text='5',command=lambda:click(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text='6',command=lambda:click(6))
btn6.grid(row=2,column=2)
subtraction=Button(root,text='-',command=lambda:click('-'))
subtraction.grid(row=2,column=3)

#=====3rd row buttons===

btn1=Button(root,text='1',command=lambda:click(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text='2',command=lambda:click(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text='3',command=lambda:click(3))
btn3.grid(row=3,column=2)
division=Button(root,text='/',command=lambda:click('/'))
division.grid(row=3,column=3)

#=====4th row buttons===

btnClear=Button(root,text='C',command=Clear)
btnClear.grid(row=4,column=0)
btn0=Button(root,text='0',command=lambda:click(0))
btn0.grid(row=4,column=1)
btnEquals=Button(root,text='=',command=Equals)
btnEquals.grid(row=4,column=2)
multiplication=Button(root,text='*',command=lambda:click('*'))
multiplication.grid(row=4,column=3)

root.mainloop()
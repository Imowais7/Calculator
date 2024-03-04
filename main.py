from tkinter import *
from tkinter.messagebox import *

font=('',14,'bold ')

#function
def clear():
    ex=textfield.get()
    ex=ex[0:len(ex)-3]
    textfield.delete(0,END)
    textfield.insert(0,ex)
def all_clear():
    textfield.delete(0,END)
def click_btn_function(event):
    print("button clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text=='X':
        textfield.insert(END,"*")
        return


    if text=='=':
        try:
            ex=textfield.get()
            answer=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,answer)
        except Exception as e:
            print('error...',e)
            showerror("Error",e)
            return

    textfield.insert(END, text)





window=Tk()
window.title('My Calculator')
window.geometry('450x350')
pic = PhotoImage(file='')

#heading
headinglabel=Label(window, text='CALCULATOR',font=font)
headinglabel.pack(side=TOP,pady=10)

#textfiled
textfield =Entry(window, font=font,justify=CENTER)
textfield.pack(side=TOP,pady=5,fill=X, padx=9)


#button
buttonFrame= Frame(window)
buttonFrame.pack(side=TOP, pady=10)

temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),font=font, width=7,activebackground='green', activeforeground='light green')
        btn.grid(row=i, column=j ,padx=5,pady=5)
        temp= temp+1
        btn.bind('<Button-1>',click_btn_function)

zeroBtn=Button(buttonFrame,text=0,font=font, width=7,activebackground='green', activeforeground='light green')
zeroBtn.grid(row=3, column=0 ,padx=5,pady=5)

dotBtn=Button(buttonFrame,text='.',font=font, width=7,activebackground='green', activeforeground='light green')
dotBtn.grid(row=3, column=1 ,padx=5,pady=5)

equalBtn=Button(buttonFrame,text='=',font=font, width=7,activebackground='green', activeforeground='light green')
equalBtn.grid(row=3, column=2 ,padx=5,pady=5)

plusBtn=Button(buttonFrame,text='+',font=font, width=7,activebackground='green', activeforeground='light green')
plusBtn.grid(row=0, column=3 ,padx=5,pady=5)

minusBtn=Button(buttonFrame,text='-',font=font, width=7,activebackground='green', activeforeground='light green')
minusBtn.grid(row=1, column=3 ,padx=5,pady=5)

multiplyBtn=Button(buttonFrame,text='X',font=font, width=7,activebackground='green', activeforeground='light green')
multiplyBtn.grid(row=2, column=3 ,padx=5,pady=5)

divideBtn=Button(buttonFrame,text='/',font=font, width=7,activebackground='green', activeforeground='light green')
divideBtn.grid(row=3, column=3 ,padx=5,pady=5)

clearBtn=Button(buttonFrame,text='<-',font=font, width=16,activebackground='green', activeforeground='light green',command=clear)
clearBtn.grid(row=4, column=0 ,padx=5,pady=5,columnspan=2)

allclearBtn=Button(buttonFrame,text='AC',font=font, width=16,activebackground='green', activeforeground='light green',command=all_clear)
allclearBtn.grid(row=4, column=2 ,padx=5,pady=5,columnspan=2)


#binding buttons
zeroBtn.bind('<Button-1>',click_btn_function)
minusBtn.bind('<Button-1>',click_btn_function)
plusBtn.bind('<Button-1>',click_btn_function)
dotBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)
multiplyBtn.bind('<Button-1>',click_btn_function)
divideBtn.bind('<Button-1>',click_btn_function)
clearBtn.bind('<Button-1>',click_btn_function)
allclearBtn.bind('<Button-1>',click_btn_function)




window.mainloop()

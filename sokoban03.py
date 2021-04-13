
from tkinter import *  
  
  
def clicked():  
    lbl.configure(text="Я же просил...")  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
lbl = Label(window, text="Привет", font=("Arial Bold", 30))  
lbl.grid(column=0, row=0)  
btn = Button(window, text="Не нажимать!", command=clicked)  
btn.grid(column=1, row=0)

vcol =[]
vrow =[]

for col01 in range(5):
    #print(number)
    for row01 in range(5):
        vrow.append(row01)
        #print ( vrow[row01] )
        vrow[row01] = Label(window, text=str(col01), font=("Arial Bold", 10))
        vrow[row01].grid(column=col01, row=row01+1)

'''
d1 = []
for j in range(5):
    d2 = []
    for i in range(5):
        d2.append(0)
    d1.append(d2)
'''      

window.mainloop()

'''

'''


from tkinter import *

Window = Tk()
Gen = StringVar(None)
hei = IntVar(None)
wei = IntVar(None)
Res = IntVar(None)


#0 - Enter
def enter():
    try:
        gen = Gen.get()
        result = float(Weight.get())/(float(Height.get())*float(Height.get()))
        if gen not in ['M', 'm', 'F', 'f']:
            result = 0
        Res.set(result)
    except ZeroDivisionError:
        hei.set()
        wei.set()
        Res.set()

    if gen in 'Mm':
        if result < 20:
            resText.set('Underweight')

        elif 20 <= result < 25:
            resText.set('Normal Weight')

        elif 25 <= result < 30:
            resText.set('Overweight')

        elif 30 <= result < 40:
            resText.set('Obesity')

        else:
            resText.set('Morbid Obesity')
            return
    
    elif gen in 'Ff':
        if result < 19:
            resText.set('Underweight')

        elif 19 <= result < 24:
            resText.set('Normal Weight')

        elif 24 <= result < 29:
            resText.set('Overweight')

        elif 29 <= result < 39:
            resText.set('Obesity')

        else:
            resText.set('Morbid Obesity')
        return
    
    else:
        resText.set('Invalid!')
    
#1 - Structure
Window.title('BMI Calculator --- Concept By Dorgival Filho')

#2 - Widgets

InfoText = StringVar()
InfoText.set('Info Men\n<= 19.9: Underweight\n20 - 24.9: Normal Weight\n25 - 29.9: Overweight\n30 - 39.9: Obesity\nAbove 40: Morbid Obesity\n')
InfoLabel = Label(Window, textvariable=InfoText)
InfoLabel.pack()

InfoText = StringVar()
InfoText.set('Info Women\n<= 18.9: Underweight\n19 - 23.9: Normal Weight\n24 - 28.9: Overweight\n29 - 38.9: Obesity\nAbove 39: Morbid Obesity')
InfoLabel = Label(Window, textvariable=InfoText)
InfoLabel.pack()

GenText = StringVar()
GenText.set('Genre')
GenDir = Label(Window, textvariable=GenText)
GenDir.pack()

Genre = Entry(Window, textvariable=Gen)
Genre.pack()

HeiText = StringVar()
HeiText.set('Height (m)')
HeiDir = Label(Window, textvariable=HeiText)
HeiDir.pack()

Height = Entry(Window, textvariable=hei)
Height.pack()

WeiText = StringVar()
WeiText.set('Weight (Kg)')
WeiDir = Label(Window, textvariable=WeiText)
WeiDir.pack()

Weight = Entry(Window, textvariable=wei)
Weight.pack()

Button(Window, text='Calculate Your BMI', font=('Kalimati', '12'), command=enter).pack(padx=10, pady=10)
Label(Window, text='\nStatus:', font=('Kalimati', '12')).pack()
LabelText = Entry(Window, textvariable=Res)
LabelText.pack()
resText = StringVar()
resText.set('Your Status is: ')
ResLab = Label(Window, textvariable=resText)
ResLab.pack()

Window.mainloop()

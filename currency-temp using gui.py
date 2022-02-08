from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from functools import partial


root=Tk()
root.title("Unit Converter")
root.geometry("500x500")

#create Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)



#Create Three Frames
main_frame= Frame(my_notebook,width = 480,height = 480)
currency_frame= Frame(my_notebook,width = 480,height = 480)
temperature_frame= Frame(my_notebook,width = 480,height = 480)

main_frame.pack(fill='both',expand=1)
currency_frame.pack(fill='both',expand=1)
temperature_frame.pack(fill='both',expand=1)

my_notebook.add(main_frame,text ='Main window')
my_notebook.add(currency_frame,text='Currency Conversion')
my_notebook.add(temperature_frame,text='Temperature Conversion')



#  Welcome Label
#welcome_label=Label(root,text="Welcme to Currency and Temperature Converter")
#welcome_label.pack(padx=10,pady=10)

# Disable 2nd Tab
my_notebook.tab(1,state='disabled')
my_notebook.tab(2,state='disabled')

def Temp():
     my_notebook.tab(2,state='normal')
     my_notebook.tab(1,state='disabled')
def Currency():
    my_notebook.tab(2,state='disabled')
    my_notebook.tab(1,state='normal')  

Temp_button = Button(main_frame,text="Currency Conversion",command=Currency)
Temp_button.pack(pady=10,padx=10)
Currency_button = Button(main_frame,text="Temperature Conversion",command=Temp)
Currency_button.pack(pady=10,padx=10)

home = Label(main_frame,text="Welcome to Unit Converter\n Select any of the above to start your Conversion")
home.pack(pady=20)

#Currency Variables
variable1 = StringVar(currency_frame)
variable2 = StringVar(currency_frame)
#Temperature Variables
numberInput = StringVar()
var = StringVar()


#Currency Stuff and Program
variable1.set("currency")
variable2.set("currency")


def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))


def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)

CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR","IDR","BGN","ILS","GBP","JPY","AUD","HUF","RON","MYR","SGD","HKD","CHF","KRW","CNY","TRY","MXN","BRL"]




label1 = Label(currency_frame, font=('Helvetica', 8), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = Label(currency_frame, font=('Helvetica', 8), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = Label(currency_frame, font=('Helvetica', 8), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = Label(currency_frame, font=('Helvetica', 8), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(currency_frame, font=('Helvetica', 7), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(currency_frame, font=('Helvetica', 7), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)


FromCurrency_option = OptionMenu(currency_frame, variable1, *CurrenyCode_list)
ToCurrency_option = OptionMenu(currency_frame, variable2, *CurrenyCode_list)

FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

Amount1_field = Entry(currency_frame)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Amount2_field = Entry(currency_frame)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

Label_9 = Button(currency_frame, font=('arial', 15), text="   Convert  ", padx=2, pady=2, bg="black", fg="white",command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)

Label_1 = Label(currency_frame, font=('Helvetica', 7), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(currency_frame, font=('arial', 15), text="   Clear All  ", padx=2, pady=2, bg="black", fg="white",command=clear_all)
Label_9.grid(row=10, column=0)
#------------------------------------------------------------------------------------------------------------------------------------------------

#Temperature Program
input_label = Label(temperature_frame, text="Enter temperature" )
input_entry = Entry(temperature_frame, textvariable=numberInput)
input_label.pack(padx=200)
input_entry.pack()

# getting drop down value
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp

# drop down initalization and setup
dropDownList = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = OptionMenu(temperature_frame, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.pack(padx=10,pady=10)
dropdown.config(foreground="black")
dropdown["menu"].config( foreground="black")

# the main conversion
def call_convert(rlabel1, rlabe12, inputn):
    tem = inputn.get()
    if tempVal == 'Celsius':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        rlabel1.config(text="%f Fahrenheit" % f)
        rlabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Fahrenheit':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Kelvin':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Fahrenheit" % f)
    return
#button frame
button_frame = Frame(temperature_frame)
button_frame.pack(pady=20)


# result label's for showing the other two temperatures
result_label1 = Label(temperature_frame)
result_label1.pack(padx=10,pady=10)
result_label2 = Label(temperature_frame)
result_label2.pack(padx=10,pady=10)

call_convert = partial(call_convert, result_label1, result_label2, numberInput)
result_button = Button(temperature_frame, text="Convert", command=call_convert)
result_button.pack(padx=20, pady=40)





root.mainloop()

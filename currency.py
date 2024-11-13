from tkinter import ttk
from tkinter import *
import json
import requests
col1="#FFFFFF"
col2="#333333"
col3="#E85051"

window=Tk()
window.geometry("300x320")
window.title("Currency Converter")
window.configure(bg=col1)
window.resizable(height=FALSE,width=FALSE)


top=Frame(window,width=300,height=60,bg=col3)
top.grid(row=0,column=0)

main=Frame(window,width=300,height=260,bg=col1)
main.grid(row=1,column=0)



def convert():
    import requests

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency1=box1.get()
    currency2=box2.get()
    amount=value.get()

    querystring = {"from":currency1,"to":currency2,"amount":amount}
    if currency2=="USD":
        symbol="$"
    elif currency2=="INR":
        symbol="₹"
    elif currency2=="EUR":
        symbol="Є"
    elif currency2=="CAD":
        symbol="CA$"
    elif currency2=="JPY":
        symbol="¥"

    headers = {
    "x-rapidapi-host": "currency-converter18.p.rapidapi.com",
    "x-rapidapi-key": "5c33565547msh83e120ea3a45d4ep10ef35jsndb46a2b63215"
  }

    response = requests.request("GET",url, headers=headers, params=querystring)
    data=json.loads(response.text)
    converted_amount=data["result"]["convertedAmount"]
    formated= symbol +"{:,.2f}".format(converted_amount)
    result["text"]=formated


    print(converted_amount,formated)




result=Label(main,text=" ",width=16,height=2,pady=7,relief="solid",anchor=CENTER,font=("Ivy 15 bold"),bg=col1,fg=col2)
result.place(x=50,y=10)

currency=["INR","CAD","USD","EUR","JPY"]

from_label=Label(main,text="From",width=8,height=1,pady=0,padx=0,relief="flat",anchor=NW,font=("Ivy 10 bold"),bg=col1,fg=col2)
from_label.place(x=40,y=90)
box1=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
box1["values"]=(currency)
box1.place(x=50,y=115)

to_label=Label(main,text="To",width=8,height=1,pady=0,padx=0,relief="flat",anchor=NW,font=("Ivy 10 bold"),bg=col1,fg=col2)
to_label.place(x=140,y=90)
box2=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
box2["values"]=(currency)
box2.place(x=150,y=115)

value=Entry(main,width=22,justify=CENTER,font=("Ivy 12 bold"),relief=SOLID)
value.place(x=50,y=155)

button=Button(main,text="CONVERTER",width=19,padx=5,height=1,bg=col3,fg=col2,font=("Ivy 12 bold"),command=convert)
button.place(x=50,y=205)

window.mainloop()

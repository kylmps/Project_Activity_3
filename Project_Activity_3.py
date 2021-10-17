#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import json
from requests import get

sample = tk.Tk()
sample.title('IP Getter')
sample.geometry("250x100")


def getIP():
    ip = get('https://api.ipify.org').text
    res = get('http://api.ipstack.com/'+ip+'?access_key=8c0be74b9a0147fc10472f75d56d5e90&format=1').text
    res = json.loads(res)
#     print(res)
    return res['ip'],res['type']

ip,uri = getIP()


textExample = tk.Entry(sample)
textExample.pack()

textExample2 = tk.Entry(sample)
textExample2.pack()

button = tk.Button(sample, text='Get IP and Version', width=20, command = lambda:setTextInput(ip, uri))
button.place(x= 45, y = 40)

def setTextInput(text, text2):
    textExample.delete(0,"end")
    textExample.insert(0, text)
    
    textExample2.delete(0,"end")
    textExample2.insert(0, text2)


sample.mainloop()



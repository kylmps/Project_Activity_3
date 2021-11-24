#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# Using Jupyter Lab


import tkinter as tk
import json
from requests import get

sample = tk.Tk()
sample.title('IP Getter')
sample.geometry("350x200")


def getIP():
    ip = get('https://api.ipify.org').text
    res = get('http://api.ipstack.com/'+ip+'?access_key=8c0be74b9a0147fc10472f75d56d5e90&format=1').text
    res = json.loads(res)
    print(res)
    return res['ip'],res['type'],res['country_name'],res['latitude'],res['longitude']

ip,uri,code,lat,long = getIP()


textExample = tk.Entry(sample)
textExample.pack()

textExample2 = tk.Entry(sample)
textExample2.pack()

textExample3 = tk.Entry(sample)
textExample3.pack()

textExample4 = tk.Entry(sample)
textExample4.pack()

textExample5 = tk.Entry(sample)
textExample5.pack()

button = tk.Button(sample, text='Get IP and location (latitude and longitude)', width=40, command = lambda:setTextInput(ip, uri, code, lat, long))
button.place(x= 45, y = 120)

def setTextInput(text, text2, text3, text4, text5):
    textExample.delete(0,"end")
    textExample.insert(0, text)
    
    textExample2.delete(0,"end")
    textExample2.insert(0, text2)
    
    textExample3.delete(0,"end")
    textExample3.insert(0, text3)
    
    textExample4.delete(0,"end")
    textExample4.insert(0, text4)
    
    textExample5.delete(0,"end")
    textExample5.insert(0, text5)


sample.mainloop()


# In[8]:


getIP()


# In[ ]:





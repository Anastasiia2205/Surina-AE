import requests
import json
import tkinter as tk 
def TK():
    visual = name.get()
    sait_json = requests.get('https://api.github.com/users/spark')
    key = json.loads(sait_json.text)
    slovar = dict({'company': key['company'],'created_at': key['created_at'],'id': key['id'],'name': key['name'],'url': key['url']})
    if visual == 'spark':
        with open('C:\\Users\\ЕвГений\\Desktop\\spark_vivod.json', 'w') as file:
            json.dump(slovar,file)        
    else:
        print('Not found')
window = tk.Tk()
window.geometry('580x400')
window.title(":)") 
name = tk.Entry(window)
name.grid(padx=160, pady=15)
btn = tk.Button(window, text="кнопка", command=TK)
btn.grid(padx=100, pady=15)
window.mainloop()
TK()
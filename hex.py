from uuid import uuid4,UUID
from requests import get
def make_hex(title):
    s=uuid4()
    print(s)
    print(f"bytes: {s.bytes}")
    print(f"hex: {s.hex}")
    print(f"version: {s.version}")
    print(f'Ints %d'%s.int)
    print(len(s.bytes))
    return s.hex

def download_url(name,url):
    local_fname=url.split("/")[-1]
    rq=get(url)
    with open(name,'wb') as file:
        for chunk in rq.iter_content(chunk_size=512*1024):
            print('goo')
            if chunk:
                file.write(chunk)
    return

url_img='http://192.168.43.66:8000/media/a580741a-1c26-4c16-aaa4-8d7ca6d1989f_Screenshot_20210516-082441_YouTube.jpg'
pipenv='https://gist.githubusercontent.com/jlusk/855d611bbcfa2b159839db73d07f6ce9/raw/7f5743401809f7e630ee8ff458faa980e19924a0/pipenv.gif'
download_url('pipenvtuturial.gif',pipenv)
import tkinter as tk
from tkinter import ttk 

root=tk.Tk()
bar=ttk.Progressbar(master=root, value=29)
bar.pack()

p=ttk.Button(master=root,text='Click me' ,command=lambda :download_url(url_img))
p.pack()
root.mainloop() 


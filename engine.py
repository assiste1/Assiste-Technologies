from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import *
import re
import webbrowser
import openpyxl

root = tk.Tk()
root.geometry("900x700")
result=''
links = []
india_links=[]
result=''
results=''
labels=[]
labelslink=[]
labellink=''
text_list=[]
wrkbk = openpyxl.load_workbook("fo_mktlots.xlsx")
sh = wrkbk["fo_mktlots"]
sheet_obj = wrkbk.active 
resultset=[]      
resjkn=[]*35
textlink=[]
keyset=[]*35
    
def res():
       for c in sh['B']:
         txt=c.value
         if txt not in resultset:
          resultset.append(txt)
          url = str(txt)
          r = requests.get(url)
          soup = BeautifulSoup(r.content, 'lxml')
          
          keywords=['property','india']
          
          for s in sh['A']:
           keywords=s.value
           if keywords not in keyset:
            keyset.append(keywords)
            ks=str(keywords).lower()
            india_links = lambda tag: (getattr(tag, 'name', None) == 'a' and
                           'href' in tag.attrs and
                           ks in tag.get_text().lower())
            results = soup.find_all(india_links)
            for link in results:
             jk = link.get('href')
             if jk.find("http") >= 0:
              jkn = jk   
              if jkn not in resjkn: 
                m=jkn
                resjkn.append(jkn)
                k=link.text.strip(' ')
                link_label = Label(root, text=k, cursor="hand2")
                link_label.pack(side=TOP,anchor=NW)
                link_label.bind("<Button-1>", lambda event: callback(event.widget.cget("text")))
                text_list.append(m)
                textlink.append(k)

def callback(urltxt):
   indtxt=textlink.index(urltxt)
   a=int(indtxt)
   url=text_list[a]
   webbrowser.open_new_tab(url)

res()

root.mainloop()
from tkinter import *
import re
import csv
import subprocess
t_str=r".*\n"

def nstrip(el):
    return el.strip()
def generateQ():
    global text_in
    full_list=[]
    
    full_text=text_in.get()
    tlist=re.findall(t_str,full_text)
    
    
    for element in tlist:
        if (element=="\n" or element.isspace()):
            tlist.remove(element)
    #print(tlist)
    telist=list(map(nstrip,tlist))
    
    for e in telist:
        if (e=="" or len(e)==2 or len(e)==1):
            telist.remove(e)
    for i in range(0,len(tlist),5):
        full_list.append(telist[i:i+5])
    print(telist)    
    with open("questions.csv",'w+',newline="") as file:
        write=csv.writer(file)
        write.writerows(full_list)
    subprocess.call(["C:/Program Files/Microsoft Office/Office15/EXCEL.exe",'questions.csv'])

root=Tk()
text_in=Entry(root,width="50")
text_in.pack(ipady="10")
text_in.focus_set()
cb=Button(root,text="Generate",command=generateQ)
cb.pack()
root.mainloop()

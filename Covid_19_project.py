import tkinter as tk
from tkinter import ttk
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import datetime
import plyer
import threading
import time

font = font =("Bodoni MT Black", 15)

def get_notify():
    
    lst = ["0","1","2","3","4","5","6","7","8","9"]
    current = []
    ctx = ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE
    html = urllib.request.urlopen("https://www.mohfw.gov.in/",context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup.find("li",attrs={"class":"bg-blue"}).get_text()
    temp = ""
    for i in tags:
        if(i in lst):
            temp+=i
        if(i == "("):
            break
    current.append(temp)
    
    tags = soup.find("li",attrs={"class":"bg-green"}).get_text()
    temp = ""
    for i in tags:
        if(i in lst):
            temp+=i
        if(i == "("):
            break
    current.append(temp)
    
    tags = soup.find("li",attrs={"class":"bg-red"}).get_text()
    temp = ""
    for i in tags:
        if(i in lst):
            temp+=i
        if(i == "("):
            break
    current.append(temp)
    
    details = ""+"Active: "+current[0]+"\n"+"Discharged: "+current[1]+"\n"+"Deaths: "+current[2]
    return(details)    
    
def notify():
    while(1):
        plyer.notification.notify(
        title="COVID-19",
        message=get_notify(),
        timeout=10,
        app_icon=r"C:\Users\DELL\.spyder-py3\scripts\Industrial_Training_Project\Covid_Project\covid-19.ico"
        )
        time.sleep(3600)

def add_data(state,r_label):
    text = state.get()
    ctx = ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE
    html = urllib.request.urlopen("https://covidindia.org/",context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup.find("tbody",attrs={"class":"row-hover"}).findAllNext("tr")
    
    for tag in tags:


        try:
            temp = []
            if(tag.find("td",attrs={"class":"column-1"}).get_text()==text):
                temp.append(tag.find("td",attrs={"class":"column-1"}).get_text())
                temp.append(tag.find("td",attrs={"class":"column-2"}).get_text())
                temp.append(tag.find("td",attrs={"class":"column-3"}).get_text())
                temp.append(tag.find("td",attrs={"class":"column-4"}).get_text())
                break
            
        except:
            pass
        
    result = ""
    for i in temp:
        result=result+i+"\n"
    r_label.config(text=result[:len(result)-1])
    return


def  refresh():
    
    data = get_data()
    
    a1.config(text=data[0][0])
    a2.config(text=data[0][1])
    a3.config(text=data[0][2])
    a4.config(text=data[0][3])
    
    d1.config(text=data[1][0])
    d2.config(text=data[1][1])
    d3.config(text=data[1][2])
    d4.config(text=data[1][3])
    
    de1.config(text=data[2][0])
    de2.config(text=data[2][1])
    de3.config(text=data[2][2])
    de4.config(text=data[2][3])    
    
    
    ti = datetime.now()
    
    t="as on : "
    t+=str(ti.day)+"/"
    t+=str(ti.month)+"/"
    t+=str(ti.year)+" , "
    t+=str(ti.hour)+":"
    t+=str(ti.minute)+":"
    t+=str(ti.second)+"\n (GMT+5:30)"
    
    time_label.config(text=t)
    
    add_data(state, r_label)

def get_state():
    
    text = state.get()
    
    ctx = ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE
    html = urllib.request.urlopen("https://covidindia.org/",context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup.find("tbody",attrs={"class":"row-hover"}).findAllNext("tr")
    
    for tag in tags:
        try:
            temp = []
            if(tag.find("td",attrs={"class":"column-1"}).get_text()==text):
                temp.append(tag.find("td",attrs={"class":"column-1"}).get_text())
                temp.append(tag.find("td",attrs={"class":"column-2"}).get_text())
                temp.append(tag.find("td",attrs={"class":"column-3"}).get_text())
                temp.append(tag.find("td",attrs={"class":"column-4"}).get_text())
                break
            
        except:
            pass
        
    result = ""
    for i in temp:
        result=result+i+"\n"
    r_label.config(text=result[:len(result)-1])
    return

def get_data():
    
    ctx = ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE
    html = urllib.request.urlopen("https://www.mohfw.gov.in/",context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup.find("div",attrs={"class":"col-xs-8 site-stats-count"}).findAllNext("li")
    cases = []
    for tag in tags:
        try:
            temp = str(tag.find("strong",attrs={"class":"mob-hide"}).get_text())
            cases.append(temp)
        except:
            pass
        
    
    lst = ["0","1","2","3","4","5","6","7","8","9"]
    current = []
    change = []
    ctx = ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE
    html = urllib.request.urlopen("https://www.mohfw.gov.in/",context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup.find("li",attrs={"class":"bg-blue"}).get_text()
    temp = ""
    for i in tags:
        if(i in lst):
            temp+=i
        if(i == "("):
            break
    current.append(int(temp))



    ind1 = tags.index("(")
    ind2 = tags.index(")")
    change.append(tags[ind1+1:ind2])
    
    tags = soup.find("li",attrs={"class":"bg-green"}).get_text()
    temp = ""
    for i in tags:
        if(i in lst):
            temp+=i
        if(i == "("):
            break
    current.append(int(temp))
    ind1 = tags.index("(")
    ind2 = tags.index(")")
    change.append(tags[ind1+1:ind2])
    
    tags = soup.find("li",attrs={"class":"bg-red"}).get_text()
    temp = ""
    for i in tags:
        if(i in lst):
            temp+=i
        if(i == "("):
            break
    current.append(int(temp))
    ind1=tags.index("(")
    ind2=tags.index(")")
    change.append(tags[ind1+1:ind2])
    
    s=sum(current)
    percent = []
    for i in current:
        percent.append(str((i/s)*100)[:5]+"%")
        
    for i in range(3):
        ind=cases[i].index(" ")
        cases[i]=cases[i][:ind]
        
    all_details = []
    for i in range(3):
        all_details.append([cases[i],percent[i],current[i],change[i]])
    
    return(all_details)

root = tk.Tk()
    
root.title("Covid-19 Tracker")
root.config(bg="#ffff00")
    
root.iconbitmap(r"C:\Users\DELL\.spyder-py3\scripts\Industrial_Training_Project\Covid_Project\covid-19.ico")
    
img_frame = tk.Frame(root)
img_frame.pack(side="top",pady=2)
    
img = tk.PhotoImage(file=r"C:\Users\DELL\.spyder-py3\scripts\Industrial_Training_Project\Covid_Project\Covid-19.png")
l = tk.Label(img_frame,image=img)
l.pack(side="top")
    
lable1 = tk.Label(root,text="INDIA's Covid-19 Situation",font=font,background="#b0b0b0",foreground="#800000")
lable1.pack(side="top",padx=10,pady=2,fill="x")
    
date_frame = tk.Frame(root)
date_frame.pack(side="top",padx=10,pady=2,fill="x")
    
ti = datetime.now()
    
t = "as on : "
t+=str(ti.day)+"/"
t+=str(ti.month)+"/"
t+=str(ti.year)+" , "
t+=str(ti.hour)+":"
t+=str(ti.minute)+":"
t+=str(ti.second)+"\n (GMT+5:30)"
    
time_label = tk.Label(date_frame,text=t,font=font,background="#00ff00",foreground="#0000ff")
time_label.pack(side="top",fill="x")
    
total_frame = tk.Frame(root)
total_frame.pack(side="top",padx=10,pady=2,fill="x")
total_frame.config(bg="#ff5e5e")
    
l1_1 = tk.Label(total_frame,text="Situation",width=22,font=font,background="#ff5e5e",foreground="#0000ff")
l1_1.grid(row=0,column=0,padx=5,pady=2)
    
l1_2 = tk.Label(total_frame,text="%Change+",width=22,font=font,background="#ff5e5e",foreground="#0000ff")
l1_2.grid(row=0,column=1,padx=5,pady=2)
    
l1_3 = tk.Label(total_frame,text="Current",width=22,font=font,background="#ff5e5e",foreground="#0000ff")
l1_3.grid(row=0,column=2,padx=5,pady=2)
    
l1_4 = tk.Label(total_frame,text="Change",width=22,font=font,background="#ff5e5e",foreground="#0000ff")
l1_4.grid(row=0,column=3,padx=5,pady=2)
    
data = get_data()
    
a1 = tk.Label(total_frame,text=data[0][0],font=font,background="#ff5e5e",foreground="#0000ff")
a1.grid(row=1,column=0,padx=5,pady=2)
    
a2 = tk.Label(total_frame,text=data[0][1],font=font,background="#ff5e5e",foreground="#0000ff")
a2.grid(row=1,column=1,padx=5,pady=2)
    
a3 = tk.Label(total_frame,text=data[0][2],font=font,background="#ff5e5e",foreground="#0000ff")
a3.grid(row=1,column=2,padx=5,pady=2)
    
a4 = tk.Label(total_frame,text=data[0][3],font=font,background="#ff5e5e",foreground="#0000ff")
a4.grid(row=1,column=3,padx=5,pady=2)
    
d1 = tk.Label(total_frame,text=data[1][0],font=font,background="#ff5e5e",foreground="#0000ff")
d1.grid(row=2,column=0,padx=5,pady=2)
    
d2 = tk.Label(total_frame,text=data[1][1],font=font,background="#ff5e5e",foreground="#0000ff")
d2.grid(row=2,column=1,padx=5,pady=2)
    
d3 = tk.Label(total_frame,text=data[1][2],font=font,background="#ff5e5e",foreground="#0000ff")
d3.grid(row=2,column=2,padx=5,pady=2)
    
d4 = tk.Label(total_frame,text=data[1][3],font=font,background="#ff5e5e",foreground="#0000ff")
d4.grid(row=2,column=3,padx=5,pady=2)
    
de1 = tk.Label(total_frame,text=data[2][0],font=font,background="#ff5e5e",foreground="#0000ff")
de1.grid(row=3,column=0,padx=5,pady=2)
    
de2 = tk.Label(total_frame,text=data[2][1],font=font,background="#ff5e5e",foreground="#0000ff")
de2.grid(row=3,column=1,padx=5,pady=2)
    
de3 = tk.Label(total_frame,text=data[2][2],font=font,background="#ff5e5e",foreground="#0000ff")
de3.grid(row=3,column=2,padx=5,pady=2)
    
de4 = tk.Label(total_frame,text=data[2][3],font=font,background="#ff5e5e",foreground="#0000ff")
de4.grid(row=3,column=3,padx=5,pady=2)
    
refresh_btn = tk.Button(root,text="Refresh",font=("Bodoni MT Black", 12),relief="raise",fg="#920323",command=refresh)
refresh_btn.pack(side="top",pady=2)
    
state = ttk.Combobox(root,state="readonly")
state["values"]=("Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadar & Nagar Haveli; Daman & Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal")
state.current(33)
state.pack(side="top",pady=2)
    
find_btn = tk.Button(root,text="Find",font=("Bodoni MT Black", 12),relief="raise",fg="#920323",command=get_state)
find_btn.pack(side="top",pady=2)
    
state_frame = tk.Frame(root)
state_frame.pack(side="top")
state_frame.config(bg="#d2d2d2")
    
s="""
Name of Sate/UT
Confirmed Cases
Recoveries
Deaths
"""
    
l_label = tk.Label(state_frame,text=s,font=font,foreground="#00e1e1")
l_label.pack(side="left")
    
r_label = tk.Label(state_frame,text="Cases",font=font,foreground="#000000")
r_label.pack(side="right")
get_state()
    
thread = threading.Thread(target=notify)
thread.setDaemon(True)
thread.start()
    
root.mainloop()
    
    

from tkinter import *
window=Tk()

def action():
    ip="127.0.0.1 "
    host=open("C:\WINDOWS\System32\drivers\etc\hosts","r+")
    # host=open("C:\\Users\\Y.KARTHICK REDDY\\Desktop\\sample.txt","r+")
    # with open ("C:\WINDOWS\System32\drivers\etc\hosts","r+") as host:
    file_data=host.read()
    website_name=name.get()
    multi=list(website_name.split(","))
    # host.write(ip)
    for x in multi:
        if x in file_data:
            val=x
            text.insert(INSERT,str(x))
            print("Already Blocked") 
            Label(text="Website already blocked").pack()
        else:
            print(x)
            Label(text="Website blocked succesfully").pack()
            text.insert(INSERT,str(x))
            host.write(ip+" "+x+"\n")
    # print(website_name)
    # print(multi
def remove1():
    # host=open("C:\\Users\\Y.KARTHICK REDDY\\Desktop\\sample.txt","r+")
    host=open("C:\WINDOWS\System32\drivers\etc\hosts","r+")
    text1=str(text.get(1.0,END))
    new=text1.split()
    re=host.read()
    new_text=""
    for c in new:
         if c==str(name.get()):
             new.remove(c)
             new_text=re.replace(c,'')
            #  print(name.get())
    text2=' '.join(new)
    host.truncate(0)
    host.write(new_text)
    # print(text2)
    text.delete(1.0,END)
    text.insert(INSERT,text2)
window.title("WEBSITE BLOCKER")
window.geometry("500x500")
label=Label(text="WEBSITE BLOCKER",fg="green",font="bold,25,bold")
label.place(x=160,y=25)
label1=Label(text="Enter the website:",font="bold,20,bold")
label1.place(x=25,y=100)
name=Entry(font="italic,15",width=20)
name.place(x=195,y=100)
submit=Button(text="BLOCK",height=2,width=10,command=action)
submit1=Button(text="UNBLOCK",height=2,width=10,command=remove1)
text=Text(height=20,width=60)
text.insert(INSERT,"Blocked websites are ")
submit.place(x=150,y=150)
submit1.place(x=260,y=150)
text.place(x=10,y=200)
window.mainloop()

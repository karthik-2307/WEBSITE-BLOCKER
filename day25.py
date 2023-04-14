from tkinter import *
window=Tk()
def action():
    ip="127.0.0.1 "
    # host=open("C:\WINDOWS\System32\drivers\etc\hosts","r+")
    with open ("C:\WINDOWS\System32\drivers\etc\hosts","r+") as host:
     file_data=host.read()
    website_name=name.get()
    multi=list(website_name.split(","))
    for x in multi:
        if x in file_data:
            print("Already Blocked") 
        else:
            file_data.write(ip+" "+x+"\n")
    print(website_name)
    print(multi)
window.title("WEBSITE BLOCKER")
window.geometry("500x500")
label=Label(text="WEBSITE BLOCKER",fg="green",font="bold,25,bold")
label.place(x=100,y=25)
label1=Label(text="Enter the website:",font="bold,20,bold")
label1.place(x=25,y=100)
name=Entry(font="italic,15",width=20)
name.place(x=195,y=100)
submit=Button(text="SUBMIT",height=2,width=10,command=action)
submit.place(x=195,y=150)
window.mainloop()
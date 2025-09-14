from tkinter import *
import guienumerator
from tkinter import ttk

def main():

    screen=Tk()
    screen.title("GUI Enumerator")
    screen.geometry("1500x1500")
    screen.config(bg="lightblue")   


    #frames
    fram1=Frame(screen,bg="lightblue",width=300,height=1500)
    fram1.pack(side=LEFT,fill=BOTH,expand=True)
    fram2=Frame(screen,bg="white",width=1400,height=1500)
    fram2.pack(side=RIGHT)
    butframe=Frame(fram1,bg="lightblue",width=300)
    butframe.place(x=0,y=100)

    #entry
    Label(fram1,text="Enter Target",font=("Arial",14),bg="lightblue").place(x=20,y=0)
    targ=Entry(fram1,width=20,font=("Arial",18),bg="lightgrey")
    targ.place(x=20,y=25)

    #functions

    def clear_results():
        for item in tree.get_children():
            tree.delete(item)

    def ipv4():
        clear_results()
        target=targ.get()
        result=guienumerator.a(target)
        for res in result:
            tree.insert("",END,values=(res,"","","","","",""))

    def ipv6():
        clear_results()
        target=targ.get()
        result=guienumerator.aaaa(target)
        for res in result:
            tree.insert("",END,values=("",res,"","","",""))
    

    def cnamerec():
        clear_results()
        target=targ.get()
        result=guienumerator.cname(target)
        for res in result:
            tree.insert("",END,values=("","",res,"","","",""))
        
    def mxrec():
        clear_results()
        target=targ.get()
        result=guienumerator.mx(target)
        for res in result:
            tree.insert("",END,values=("","","",res,"","",""))

    def nsrec():
        clear_results()
        target=targ.get()
        result=guienumerator.ns(target)
        for res in result:
            tree.insert("",END,values=("","","","",res,"",""))

    def txtrec():
        clear_results()
        target=targ.get()
        result=guienumerator.txt(target)
        for res in result:
            tree.insert("",END,values=("","","","","",res,""))
        
    def soarec():
        clear_results()
        target=targ.get()
        result=guienumerator.soa(target)
        for res in result:
            tree.insert("",END,values=("","","","","","",res))
        
    def allrec():
        clear_results()
        target=targ.get()
        result=guienumerator.all_records(target)
        max_len = max(len(v) for v in result.values())
        for i in range(max_len):
            row = []
            for rec_type in ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"]:
                values = result.get(rec_type, [])
                row.append(values[i] if i < len(values) else "")
            tree.insert("", END, values=tuple(row))

    #buttons
    abut=Button(butframe,text="ipv4",command=ipv4,bg="lightgreen")
    aaaabut=Button(butframe,text="ipv6",command=ipv6,bg="red")
    cnamebut=Button(butframe,text="CNAME",command=cnamerec,bg="yellow")
    mxbut=Button(butframe,text="MX",command=mxrec,bg="pink")
    nsbut=Button(butframe,text="NS",command=nsrec,bg="lightgrey")
    txtbut=Button(butframe,text="TXT",command=txtrec,bg="orange")
    soabut=Button(butframe,text="SOA",command=soarec,bg="violet")
    allbut=Button(butframe,text="ALL",command=allrec,bg="lightblue")
    clearbut=Button(butframe,text="Clear",command=clear_results,bg="white")

    abut.grid(row=0,column=0,padx=10,pady=10)
    aaaabut.grid(row=0,column=1,padx=10,pady=10)
    cnamebut.grid(row=1,column=0,padx=10,pady=10)
    mxbut.grid(row=1,column=1,padx=10,pady=10)
    nsbut.grid(row=2,column=0,padx=10,pady=10)
    txtbut.grid(row=2,column=1,padx=10,pady=10)
    soabut.grid(row=3,column=0,padx=10,pady=10)
    allbut.grid(row=3,column=1,padx=10,pady=10)
    clearbut.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky="we")



    #treeview
    tree=ttk.Treeview(fram2,columns=("A","AAAA","CNAME","MX","NS","TXT","SOA"),show="headings",height=1500)
    tree.heading("A",text="A Record")
    tree.heading("AAAA",text="AAAA Record")
    tree.heading("CNAME",text="CNAME Record")
    tree.heading("MX",text="MX Record")
    tree.heading("NS",text="NS Record")
    tree.heading("TXT",text="TXT Record")
    tree.heading("SOA",text="SOA Record")
    tree.column("A",width=230)
    tree.column("AAAA",width=230)
    tree.column("CNAME",width=230)
    tree.column("MX",width=230)
    tree.column("NS",width=230)     
    tree.column("TXT",width=230)
    tree.column("SOA",width=230)
    tree.pack(fill=BOTH,expand=True)



    screen.mainloop()




if __name__ == "__main__":
    main()
from tkinter import *
import enumerator
from tkinter import ttk
import whoiscan

def main():

    screen=Tk()
    screen.title("DNS Lookup")
    screen.geometry("1500x1600")
    screen.config(bg="lightblue")   


    #frames
    fram1=Frame(screen,bg="lightblue",width=300,height=1500)
    fram1.pack(side=LEFT,fill=BOTH,expand=True)
    fram2=Frame(screen,bg="white",width=1400,height=1500)
    fram2.pack(side=RIGHT,expand=True,fill=BOTH)
    butframe=Frame(fram1,bg="lightblue",width=300)
    butframe.place(x=0,y=100)

    # Configure grid for fram2
    fram2.grid_rowconfigure(0, weight=1)
    fram2.grid_rowconfigure(1, weight=1)
    fram2.grid_columnconfigure(0, weight=1)

    #recordsframe
    rec_frame=Frame(fram2,height=750,width=1400,bg="lightgrey",border=5)
    rec_frame.grid(row=0, column=0, sticky="nsew")

    #whoisframe
    whoisframe=Frame(fram2,height=750,width=1400,border=5)
    whoisframe.grid(row=1, column=0, sticky="nsew")
    
    
    #entry
    Label(fram1,text="Enter Target",font=("Arial",14),bg="lightblue").place(x=20,y=0)
    targ=Entry(fram1,width=20,font=("Arial",18),bg="lightgrey")
    targ.place(x=20,y=25)

    #functions

    def clear_results():
        for item in tree.get_children():
            tree.delete(item)
        clear_whois()   
        
    def clear_whois():
        for item in whoistree.get_children():
            whoistree.delete(item)

    def ipv4():
        clear_results()
        target=targ.get()
        result=enumerator.a(target)
        # result may be a list of IPs or a single string; normalize to list
        if not result:
            return
        if isinstance(result, str):
            result = [result]
        for res in result:
            tree.insert("",END,values=(res,"","","","","",""))

    def ipv6():
        clear_results()
        target=targ.get()
        result=enumerator.ipv6(target)
        if not result:
            return
        if isinstance(result, str):
            result = [result]
        for res in result:
            # Ensure 7 columns: (A, AAAA, CNAME, MX, NS, TXT, SOA)
            tree.insert("",END,values=("",res,"","","","",""))
    

    def cnamerec():
        clear_results()
        target=targ.get()
        result=enumerator.cname(target)
        if not result:
            return
        if isinstance(result, str):
            result = [result]
        for res in result:
            tree.insert("",END,values=("","",res,"","","",""))
        
    def mxrec():
        clear_results()
        target=targ.get()
        result=enumerator.mx(target)
        if not result:
            return
        if isinstance(result, str):
            result = [result]
        for res in result:
            tree.insert("",END,values=("","","",res,"","",""))

    def nsrec():
        clear_results()
        target=targ.get()
        result=enumerator.ns(target)
        if not result:
            return
        if isinstance(result, str):
            result = [result]
        for res in result:
            tree.insert("",END,values=("","","","",res,"",""))

    def txtrec():
        clear_results()
        target=targ.get()
        result=enumerator.txt(target)
        if not result:
            return
        if isinstance(result, str):
            result = [result]
        for res in result:
            tree.insert("",END,values=("","","","","",res,""))
        
    def soarec():
        clear_results()
        target=targ.get()
        result=enumerator.soa(target)
        if not result:
            return
        if isinstance(result, str):
            result = [result]
        for res in result:
            tree.insert("",END,values=("","","","","","",res))

    def whoisrec():
        clear_whois()
        target = targ.get()
        result = whoiscan.whois_scan(target)
        for key, value in result.items():
            whoistree.insert("", END, values=(f"{key}: {value}",))

    def allrec():
        clear_results()
        target=targ.get()
        rec1=enumerator.a(target)
        rec2=enumerator.ipv6(target)
        rec3=enumerator.cname(target)
        rec4=enumerator.mx(target)
        rec5=enumerator.ns(target)
        rec6=enumerator.txt(target)
        rec7=enumerator.soa(target)
        # Normalize non-list returns to lists
        recs = []
        for r in (rec1, rec2, rec3, rec4, rec5, rec6, rec7):
            if not r:
                recs.append([])
            elif isinstance(r, list):
                recs.append(r)
            else:
                recs.append([str(r)])

        max_len = max((len(r) for r in recs), default=0)
        # Insert rows aligning records by index across columns
        for i in range(max_len):
            row = tuple((recs[col][i] if i < len(recs[col]) else "") for col in range(7))
            tree.insert("", END, values=row)
        whoisrec()
    
    #buttons
    abut=Button(butframe,text="ipv4",command=ipv4,bg="lightgreen",width=10)
    aaaabut=Button(butframe,text="ipv6",command=ipv6,bg="red",width=10)
    cnamebut=Button(butframe,text="CNAME",command=cnamerec,bg="yellow",width=10)
    mxbut=Button(butframe,text="MX",command=mxrec,bg="pink",width=10)
    nsbut=Button(butframe,text="NS",command=nsrec,bg="lightgrey",width=10)
    txtbut=Button(butframe,text="TXT",command=txtrec,bg="orange",width=10)
    soabut=Button(butframe,text="SOA",command=soarec,bg="violet",width=10)
    allbut=Button(butframe,text="ALL",command=allrec,bg="lightblue",width=10)
    whoisbut=Button(butframe,text="WHOIS",command=whoisrec,bg="cyan",width=10)
    clearbut=Button(butframe,text="Clear",command=clear_results,bg="white",width=10)

    abut.grid(row=0,column=0,padx=10,pady=10)
    aaaabut.grid(row=0,column=1,padx=10,pady=10)
    cnamebut.grid(row=1,column=0,padx=10,pady=10)
    mxbut.grid(row=1,column=1,padx=10,pady=10)
    nsbut.grid(row=2,column=0,padx=10,pady=10)
    txtbut.grid(row=2,column=1,padx=10,pady=10)
    soabut.grid(row=3,column=0,padx=10,pady=10)
    allbut.grid(row=3,column=1,padx=10,pady=10)
    whoisbut.grid(row=4,column=0,padx=10,pady=10)
    clearbut.grid(row=4,column=1,padx=10,pady=10)

    #whoistree
    whoistree=ttk.Treeview(whoisframe,columns=("whoisinfo"),show="headings",height=30)
    whoistree.heading("whoisinfo",text="WHOIS Information")
    whoistree.column("whoisinfo",width=1370)

    #whoisscrollbar
    whoisscrollbar=Scrollbar(whoisframe,orient=VERTICAL,command=whoistree.yview)
    whoistree.configure(yscrollcommand=whoisscrollbar.set)

    whoisscrollbar.pack(side=RIGHT,fill=Y)
    whoistree.pack(fill=BOTH,expand=True)


    #treeview
    tree=ttk.Treeview(rec_frame,columns=("A","AAAA","CNAME","MX","NS","TXT","SOA"),show="headings",height=10)
    tree.heading("A",text="A Record")
    tree.heading("AAAA",text="AAAA Record")
    tree.heading("CNAME",text="CNAME Record")
    tree.heading("MX",text="MX Record")
    tree.heading("NS",text="NS Record")
    tree.heading("TXT",text="TXT Record")
    tree.heading("SOA",text="SOA Record")
    tree.column("A",width=100)
    tree.column("AAAA",width=210)
    tree.column("CNAME",width=230)
    tree.column("MX",width=230)
    tree.column("NS",width=200)
    tree.column("TXT",width=230)
    tree.column("SOA",width=230)
    tree.pack(fill=BOTH,expand=True)



    screen.mainloop()




if __name__ == "__main__":
    main()

import enumerator
from colorama import Fore




def arec(target):
    
    print(Fore.GREEN+"\n|--------------------A RECORD--------------------|\n")
    result=enumerator.a(target)
    print(result)

def aaaarec(target):    
    print(Fore.GREEN+"\n|--------------------AAAA RECORD--------------------|\n")
    result=enumerator.ipv6(target)
    print(result)
    
def cnamerec(target):
    print(Fore.GREEN+"\n|--------------------CNAME RECORD--------------------|\n")
    result=enumerator.cname(target)
    print(result)
        

def mxrec(target):    
    print(Fore.GREEN+"\n|--------------------MX RECORD--------------------|\n")
    result=enumerator.mx(target)
    print(result)
        

def nsrec(target):    
    print(Fore.GREEN+"\n|--------------------NS RECORD--------------------|\n")
    result=enumerator.ns(target)
    print(result)
        

def txtrec(target):    
    print(Fore.GREEN+"\n|--------------------TXT RECORD--------------------|\n")
    result=enumerator.txt(target)
    print(result)
        

def soarec(target):    
    print(Fore.GREEN+"\n|--------------------SOA RECORD--------------------|\n")
    result=enumerator.soa(target)
    print(result)
        
def allrec(target):
    print(Fore.GREEN+"\n|--------------------all RECORD--------------------|\n")
    arec(target)
    aaaarec(target)
    cnamerec(target)
    mxrec(target)
    nsrec(target)
    txtrec(target)
    soarec(target)
    
    
    
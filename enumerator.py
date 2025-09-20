import dns.resolver
import whoiscan
from colorama import *



def a(target):
    try:
        info=dns.resolver.resolve(target,'A')
    
        for ip in info:
            return [str(ip)]
    except dns.resolver.NoAnswer:
        return(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        return(Fore.RED+"Domain does not exist")
    except Exception as e:
        return(Fore.RED+f"error occured :{e}"+Fore.RESET)
        

def ipv6(target):
    
    try:
        info=dns.resolver.resolve(target,'AAAA')
    
        for ip in info:
            return [str(ip)]
            
    except dns.resolver.NoAnswer:
        return(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        return(Fore.RED+"Domain does not exist")
    except Exception as e:
        return(Fore.RED+f"error occured :{e}"+Fore.RESET)
        
def cname(target):
        
    try:
        cname_info=dns.resolver.resolve(target,'CNAME')
    
        for cn in cname_info:
            return cn
            
    except dns.resolver.NoAnswer:
        return(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        return(Fore.RED+"Domain does not exist")
    except Exception as e:
        return(Fore.RED+f"error occured :{e}"+Fore.RESET)
        

def mx(target):
    
    try:
        mail_info=dns.resolver.resolve(target,'MX')
    
        for mailinfo in mail_info:
            return [str(mailinfo)]
        
    except dns.resolver.NoAnswer:
        return(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        return(Fore.RED+"Domain does not exist")
    except Exception as e:
        return(Fore.RED+f"error occured :{e}"+Fore.RESET)
         
def ns(target):
    
    
    try:
        ns_info=dns.resolver.resolve(target,'NS')
    
        for nameserver in ns_info:
            return [str(nameserver)]
            
    except dns.resolver.NoAnswer:
        return(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        return(Fore.RED+"Domain does not exist")
    except Exception as e:
        return(Fore.RED+f"error occured :{e}"+Fore.RESET)
        
def txt(target):
    
    
    try:
        
        txt_rec=dns.resolver.resolve(target,'TXT')
    
        for rec in txt_rec:
            return [str(rec)]
            
    except dns.resolver.NoAnswer:
        return(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        return(Fore.RED+"Domain does not exist")
    except Exception as e:
        return(Fore.RED+f"error occured :{e}"+Fore.RESET)
        

               
def soa(target):
    
    
    try:
        soa_rec=dns.resolver.resolve(target,'SOA')
        for rec in soa_rec:
            return [str(rec)]
    except dns.resolver.NoAnswer:
        return(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        return(Fore.RED+"Domain does not exist")
    except Exception as e:
        return(Fore.RED+f"error occured :{e}"+Fore.RESET)
  

       
def all_records(target):
    
    results = {
        "A": a(target),
        "AAAA": ipv6(target),
        "CNAME": cname(target),
        "MX": mx(target),
        "NS": ns(target),
        "TXT": txt(target),
        "SOA": soa(target),
    }
    return results

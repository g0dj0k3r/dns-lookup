import dns.resolver
import whoiscan
from colorama import *



def a(target):
    try:
        info=dns.resolver.resolve(target,'A')
        return [ip.to_text() for ip in info]
            
    except dns.resolver.NoAnswer:
        return [Fore.RED+"Query does not exist :"+Fore.RESET]
    except dns.resolver.NXDOMAIN:
        return [Fore.RED+"Domain does not exist"+Fore.RESET]
    except Exception as e:
        return [Fore.RED+f"error occured :{e}"+Fore.RESET]
        

def ipv6(target):
    
    try:
        info=dns.resolver.resolve(target,'AAAA')
        return [ip.to_text() for ip in info]

            
    except dns.resolver.NoAnswer:
        return [Fore.RED+"Query does not exist :"+Fore.RESET]
    except dns.resolver.NXDOMAIN:
        return [Fore.RED+"Domain does not exist"+Fore.RESET]
    except Exception as e:
        return [Fore.RED+f"error occured :{e}"+Fore.RESET]
        
def cname(target):
        
    try:
        cname_info=dns.resolver.resolve(target,'CNAME')
    
        return [data.to_text() for data in cname_info]
            
    except dns.resolver.NoAnswer:
        return [Fore.RED+"Query does not exist :"+Fore.RESET]
    except dns.resolver.NXDOMAIN:
        return [Fore.RED+"Domain does not exist"+Fore.RESET]
    except Exception as e:
        return [Fore.RED+f"error occured :{e}"+Fore.RESET]
        

def mx(target):
    
    try:
        mail_info=dns.resolver.resolve(target,'MX')
    
        return [data.to_text() for data in mail_info]

        
    except dns.resolver.NoAnswer:
        return [Fore.RED+"Query does not exist :"+Fore.RESET]
    except dns.resolver.NXDOMAIN:
        return [Fore.RED+"Domain does not exist"+Fore.RESET]
    except Exception as e:
        return [Fore.RED+f"error occured :{e}"+Fore.RESET]
         
def ns(target):
    
    
    try:
        ns_info=dns.resolver.resolve(target,'NS')

        return [data.to_text() for data in ns_info]
            
    except dns.resolver.NoAnswer:
        return [Fore.RED+"Query does not exist :"+Fore.RESET]
    except dns.resolver.NXDOMAIN:
        return [Fore.RED+"Domain does not exist"+Fore.RESET]
    except Exception as e:
        return [Fore.RED+f"error occured :{e}"+Fore.RESET]
        
def txt(target):
    
    
    try:
        
        txt_rec=dns.resolver.resolve(target,'TXT')
    
        return [data.to_text() for data in txt_rec]

            
    except dns.resolver.NoAnswer:
        return [Fore.RED+"Query does not exist :"+Fore.RESET]
    except dns.resolver.NXDOMAIN:
        return [Fore.RED+"Domain does not exist"+Fore.RESET]
    except Exception as e:
        return [Fore.RED+f"error occured :{e}"+Fore.RESET]
        

               
def soa(target):
    
    
    try:
        soa_rec=dns.resolver.resolve(target,'SOA')
        return [data.to_text() for data in soa_rec]

    except dns.resolver.NoAnswer:
        return[Fore.RED+"Query does not exist :"]
    except dns.resolver.NXDOMAIN:
        return[Fore.RED+"Domain does not exist"]
    except Exception as e:
        return[Fore.RED+f"error occured :{e}"+Fore.RESET]
  

       
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

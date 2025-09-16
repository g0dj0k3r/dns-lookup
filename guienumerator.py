import dns.resolver

def a(target):
    try:
        info=dns.resolver.resolve(target,'A')
        return [str(rdata) for rdata in info.rrset]
    
    except dns.resolver.NoAnswer:
        return ["Query does not exist"]
    
    except Exception as e:
        return [f"Error: {e}"]
      
def aaaa(target):

    try:
        info=dns.resolver.resolve(target,'AAAA')
        return [str(rdata) for rdata in info.rrset]

    except dns.resolver.NoAnswer:
        return ["Query does not exist"]
    
    except Exception as e:
        return [f"Error: {e}"]
    
            
 
def cname(target):

    try:
        info=dns.resolver.resolve(target,'CNAME')
        return [str(rdata) for rdata in info.rrset]
    
    except dns.resolver.NoAnswer:
        return ["Query does not exist"]
    except Exception as e:
        return [f"Error: {e}"]
    

def mx(target):
    try:
    
        info=dns.resolver.resolve(target,'MX')
        return [str(rdata) for rdata in info.rrset]
    
    except dns.resolver.NoAnswer:
        return ["Query does not exist"]
    except Exception as e:
        return [f"Error: {e}"]
   
def ns(target):
    
    try:
        info=dns.resolver.resolve(target,'NS')
        return [str(rdata) for rdata in info.rrset]
    
    except dns.resolver.NoAnswer:
        return ["Query does not exist"]
    except Exception as e:
        return [f"Error: {e}"]
   
        
def txt(target):
    
    try:
        info=dns.resolver.resolve(target,'TXT')
        return [str(rdata) for rdata in info.rrset]
    
    except dns.resolver.NoAnswer:
        return ["Query does not exist"]
    except Exception as e:
        return [f"Error: {e}"]
   

               
def soa(target):
    
    try:
        info=dns.resolver.resolve(target,'SOA')
        return [str(rdata) for rdata in info.rrset]
    
    except dns.resolver.NoAnswer:
        return ["Query does not exist"]
    except Exception as e:
        return [f"Error: {e}"]
    
  
        
def all_records(target):
    
    results = {
        "A": a(target),
        "AAAA": aaaa(target),
        "CNAME": cname(target),
        "MX": mx(target),
        "NS": ns(target),
        "TXT": txt(target),
        "SOA": soa(target),
    }
    return results

import dns.resolver

def a(target):

    info=dns.resolver.resolve(target,'A')

    return [str(rdata) for rdata in info.rrset]
      
def aaaa(target):

    info=dns.resolver.resolve(target,'AAAA')

    return [str(rdata) for rdata in info.rrset]

            
 
def cname(target):

    info=dns.resolver.resolve(target,'CNAME')

    return [str(rdata) for rdata in info.rrset]
      

def mx(target):
    info=dns.resolver.resolve(target,'MX')

    return [str(rdata) for rdata in info.rrset]
   
def ns(target):
    info=dns.resolver.resolve(target,'NS')

    return [str(rdata) for rdata in info.rrset]
   
        
def txt(target):
    info=dns.resolver.resolve(target,'TXT')

    return [str(rdata) for rdata in info.rrset]
   

               
def soa(target):
    info=dns.resolver.resolve(target,'SOA')

    return [str(rdata) for rdata in info.rrset]
    
  
        
def all_records(target):
    result = {}
    for rec in ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"]:
        try:
            func = globals()[rec.lower()]
            result[rec] = func(target)
        except Exception as e:
            result[rec] = [f"Error: {e}"]
    return result

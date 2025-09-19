import whoiscan
import colorama
import sys
import argparse
import user_manuel
import perform
from colorama import Fore, Back, Style
from pyfiglet import*


f=Figlet()
def banner():


    print(Fore.LIGHTBLUE_EX+f.renderText("Dnslookup"))
    print("!!This tools is made only for testing and legal purpose !! \n")
    print("\t \t \t Created : 05.03.2025\n")
    print("\t \t \t Git hub: https://github.com/godj0ker\n")
    print("\t \t \t Version : v2.0\n")
    print("\t \t \t by Godjoker\n\n\n"+Fore.RESET)

def dlookup():
    
    banner()
    
    
    parser = argparse.ArgumentParser(description="Domain lookup" ,add_help=False) 
    parser.add_argument('-h', '--help',action='store_true',help="Show help information")
    parser.add_argument('-c', '--commands', action='store_true', help="Show available commands and options")
    parser.add_argument('-d', '--domain', type=str,help='ENTER TARGET DOMAIN')
    parser.add_argument('-l', '--lookup', type=str,choices=['whois','a', '4a','mx', 'ns', 'txt', 'soa', 'cname','all'], help='Type of DNS lookup to perform')
    parser.add_argument('-q', '--exit', action='store_true', help='Exit the program')
    args = parser.parse_args()

      

              
                
    try:
        
        if args.exit:
            print(Fore.RED+"Exiting the program. Goodbye!"+Fore.RESET)
            sys.exit(0)
            return
        
        if len(sys.argv)==1:
            print(Fore.RED+parser.format_help()+Fore.RESET)
            print(Fore.RED+parser.format_usage()+Fore.RESET)
            return
        
        if args.help:
            print(Fore.RED+parser.format_help()+Fore.RESET)
            print(Fore.RED+parser.format_usage()+Fore.RESET)
            print('\n\n')
            user_manuel.help()
            return
        
        
        if args.commands:
            user_manuel.commands()
            sys.exit(0)
            return
        
        if not args.domain:
            print(Fore.RED+"Please specify a domain using -d or --domain")
            print(Fore.RED+"!!Type -c or --commands for available commands and options!!"+Fore.RESET)
    
        if not args.lookup:
            user_manuel.help()
            args.usage = parser.format_help()
            sys.exit(0)
            return

       
    
    
        if (args.domain or args.d) and not (args.lookup or args.l):
            print(Fore.RED+"Please specify a Lookup option using -l or --lookup")
            print(Fore.RED+"!!Type -c or --commands for available commands and options!!"+Fore.RESET)
            print(Fore.RED+"Usage: dns-lookup -d <domain> -l <lookup_option>"+Fore.RESET)
            sys.exit(1)
            return
   
    
        if (args.domain or args.d) and (args.lookup or args.l):
            target=args.domain or args.d
            # Only one lookup type is possible due to argparse 'choices', so just check args.lookup
            if (args.lookup or args.l) == 'whois':
                print(Fore.GREEN+"Performing WHOIS lookup for domain: "+args.domain)
                whoiscan.whois_scan(target)
                
            elif (args.lookup or args.l) == 'a':
                print(Fore.GREEN+"Performing A record lookup for domain: "+args.domain)
                perform.arec(target)
                
            elif (args.lookup or args.l) == '4a':
                print(Fore.GREEN+"Performing AAAA record lookup for domain: "+args.domain)
                perform.aaaarec(target)
                              
                
            elif (args.lookup or args.l) == 'cname':
                print(Fore.GREEN+"Performing CNAME record lookup for domain: "+args.domain)
                perform.cnamerec(target)
                
                    
                    
            elif (args.lookup or args.l) == 'mx':
                print(Fore.GREEN+"Performing MX record lookup for domain: "+args.domain)
                perform.mxrec(target)
                
                
            elif (args.lookup or args.l) == 'ns':
                print(Fore.GREEN+"Performing NS record lookup for domain: "+args.domain)
                perform.nsrec(target)
                    
                
            elif (args.lookup or args.l) == 'txt':
                print(Fore.GREEN+"Performing TXT record lookup for domain: "+args.domain)
                perform.txtrec(target)
                
                
            elif (args.lookup or args.l) == 'soa':
                print(Fore.GREEN+"Performing SOA record lookup for domain: "+args.domain)
                perform.soarec(target)
                    
                
            elif (args.lookup or args.l) == 'all':
                print(Fore.GREEN+"Performing all record lookup for domain: "+args.domain)
                perform.allrec(target) 
                
            else:
                print(Fore.RED+"Invalid option. Please use -h or --help for usage information."+Fore.RESET)
                sys.exit(1)
                
                
        else:
            print(Fore.RED+"!!type -h or --help for usage information!!"+Fore.RESET)
            print(Fore.RED+"Please specify a domain using -d or --domain and a lookup option using -l or --lookup"+Fore.RESET)
            print(Fore.RED+"Usage: python3 dns_enum.py -d <domain> -l <lookup_option>"+Fore.RESET)
            sys.exit(1)
            return
    except argparse.ArgumentError as e:
        print(Fore.RED+"Argument error: "+str(e)+Fore.RESET)
        sys.exit(1)
        return
    
    except argparse.ArgumentTypeError as e:
        print(Fore.RED+"Argument type error: "+str(e)+Fore.RESET)
        sys.exit(1)
        return
    
    except KeyboardInterrupt:
        print(Fore.RED+"\nExiting the program. Goodbye!"+Fore.RESET)
        sys.exit(0)
        return
    
    except Exception as e:
        print(Fore.RED+"An error occurred: "+str(e)+Fore.RESET)
        sys.exit(1)
        return
    

    except ValueError as e:
        print(Fore.RED+"Value error: "+str(e)+Fore.RESET)
        sys.exit(1)
        return
    
    


    
    

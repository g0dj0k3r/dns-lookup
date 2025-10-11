import sys
import argparse
import user_manuel
import perform
from colorama import Fore
from pyfiglet import Figlet


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
    
    
    parser = argparse.ArgumentParser(description="Domain lookup", add_help=False)
    # Custom help, commands, usage, and exit arguments
    parser.add_argument('-h', '--help', action='store_true', help="Show help information")
    parser.add_argument('-c', '--commands', action='store_true', help="Show available commands and options")
    parser.add_argument('-u', '--usage', action='store_true', help='Show usage information')
    parser.add_argument('-q', '--exit', action='store_true', help='Exit the program')

    # Core functional arguments
    # Allow -d and -l to be provided without values so we can print friendly messages
    parser.add_argument('-d', '--domain', nargs='?', const='', type=str, help='ENTER TARGET DOMAIN')
    # Do not set argparse choices here; validate after parsing so empty const ('') isn't rejected.
    parser.add_argument('-l', '--lookup', nargs='?', const='', type=str,help='Type of DNS lookup to perform')

              
                
    try:
        args = parser.parse_args()

        if len(sys.argv)==2:
            if args.help:
                print(Fore.RED+parser.format_help()+Fore.RESET)
                print('\n\n')
                return
            
            if args.commands:
                user_manuel.commands()
                sys.exit(0)
                return
           
            if args.usage:
                print(Fore.RED+parser.format_usage()+Fore.RESET)
                return
            
            if args.exit:
                print(Fore.RED+"Exiting the program. Goodbye!"+Fore.RESET)
                sys.exit(0)
            # If -d was provided without a value, argparse sets args.domain to ''
            if args.domain == '':
                print(Fore.RED+"Please specify a Target domain using -d or --domain")
                print(Fore.RED+"!!Type -c or --commands for available commands and options!!"+Fore.RESET)
                return
           
        elif len(sys.argv)==3:
            if args.domain:
                print(Fore.GREEN+"Domain specified: "+args.domain+Fore.RESET)
                print(Fore.YELLOW+"Please specify a lookup option for the target domain using -l or --lookup"+Fore.RESET)

        elif len(sys.argv)==4:
            # user provided -l without a value (args.lookup will be '' because of nargs='?'/const='')
            if args.lookup in ('', None):
                print(Fore.RED+"Please specify a lookup option using -l or --lookup"+Fore.RESET)
                print(Fore.RED+parser.format_usage()+Fore.RESET)
                print(Fore.RED+"Lookup Options: whois, a, 4a, cname, mx, ns, txt, soa, all"+Fore.RESET)
                return

        elif len(sys.argv)==5:
            # target domain determination
            target=args.domain or args.d
            print(Fore.GREEN+"Domain specified: "+str(target)+Fore.RESET)

          # Now dispatch based on args.lookup
            
                
            if args.lookup == 'whois':
                print(Fore.GREEN+"Performing WHOIS lookup for domain: "+str(target)+Fore.RESET)
                perform.whoisrec(target)

            elif args.lookup == 'a':
                print(Fore.GREEN+"Performing A record lookup for domain: "+str(target)+Fore.RESET)
                perform.arec(target)

            elif args.lookup == '4a':
                print(Fore.GREEN+"Performing AAAA record lookup for domain: "+str(target)+Fore.RESET)
                perform.aaaarec(target)

            elif args.lookup == 'cname':
                print(Fore.GREEN+"Performing CNAME record lookup for domain: "+str(target)+Fore.RESET)
                perform.cnamerec(target)

            elif args.lookup == 'mx':
                print(Fore.GREEN+"Performing MX record lookup for domain: "+str(target)+Fore.RESET)
                perform.mxrec(target)

            elif args.lookup == 'ns':
                print(Fore.GREEN+"Performing NS record lookup for domain: "+str(target)+Fore.RESET)
                perform.nsrec(target)

            elif args.lookup == 'txt':
                print(Fore.GREEN+"Performing TXT record lookup for domain: "+str(target)+Fore.RESET)
                perform.txtrec(target)

            elif args.lookup == 'soa':
                print(Fore.GREEN+"Performing SOA record lookup for domain: "+str(target)+Fore.RESET)
                perform.soarec(target)

            elif args.lookup == 'all':
                print(Fore.GREEN+"Performing all record lookup for domain: "+str(target)+Fore.RESET)
                perform.allrec(target)

            else:
                print(Fore.RED+"Invalid option. Please use -h or --help for usage information."+Fore.RESET)
                sys.exit(1)
                return
    
        else:
            print(Fore.RED+"!!type -h or --help for usage information!!"+Fore.RESET)
            sys.exit(0)
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
    
    

    
    

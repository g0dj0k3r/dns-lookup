# dns-lookup

A simple Python tool for performing DNS lookups and WHOIS queries from the terminal.  
**Created for testing and legal purposes only.**

## Features

- Interactive command-line menu
- WHOIS domain info lookup
- DNS record lookups:
  - a (IPv4)
  - 4a (IPv6)
  - cname
  - mx (Mail)
  - nx (Name Server)
  - txt
  - soa
  - all records at once

## Demo

```
$ dnslookup


 ____            _             _
|  _ \ _ __  ___| | ___   ___ | | ___   _ _ __
| | | | '_ \/ __| |/ _ \ / _ \| |/ / | | | '_ \
| |_| | | | \__ \ | (_) | (_) |   <| |_| | |_) |                                                                                            |____/|_| |_|___/_|\___/ \___/|_|\_\\__,_| .__/                                                                                                                                      |_|



                                                                                                                                                                                                                                           
!!This tools is made only for testing and legal purpose !!                                                                                                                                                                                 
                                                                                                                                                                                                                                           
                         Created : 05.03.2025                                                                                                                                                                                              
                                                                                                                                                                                                                                           
                         Git hub: https://github.com/godj0ker                                                                                                                                                                              
                                                                                                                                                                                                                                           
                         Version : v2.0                                                                                                                                                                                                    
                                                                                                                                                                                                                                           
                         by Godjoker                                                                                                                                                                                                       
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
usage: dnslookup [-h] [-c] [-d DOMAIN] [-l {whois,a,4a,mx,ns,txt,soa,cname,all}] [-q]
                                                                                                                                                                                                                                           
Domain lookup                                                                                                                                                                                                                              
                                                                                                                                                                                                                                           
options:                                                                                                                                                                                                                                   
  -h, --help            Show help information                                                                                                                                                                                              
  -c, --commands        Show available commands and options                                                                                                                                                                                
  -d, --domain DOMAIN   ENTER TARGET DOMAIN                                                                                                                                                                                                
  -l, --lookup {whois,a,4a,mx,ns,txt,soa,cname,all}                                                                                                                                                                                        
                        Type of DNS lookup to perform                                                                                                                                                                                      
  -q, --exit            Exit the program                                                                                                                                                                                                   
                                                                                                                                                                                                                                           
usage: dnslookup [-h] [-c] [-d DOMAIN] [-l {whois,a,4a,mx,ns,txt,soa,cname,all}] [-q]
                                                   
```


## Usage

1. Clone the repository:
    ```
    git clone https://github.com/g0dj0k3r/dns-lookup.git
    cd dns-lookup
    ```

2. Install dependencies:
    ```
    sudo python3 setup.py install
    or
    sudo pip install e. 
    ```
    **Dependencies:**  
    - `colorama`  
    - `pyfiglet`  
    - `dnspython`  
    - `python-whois`  
    - (see your own code for additional modules if needed)

4. Run the tool:
    ```
    dnslookup -h
    ```

5. Follow the prompts in the terminal.

## Requirements

- Python 3.x
- Install dependencies (see above)

## Author

- **Godjoker**  
  GitHub: [g0dj0k3r](https://github.com/g0dj0k3r)

## License

Opensource

---

> This tool is intended for educational and legal testing purposes only. Use responsibly.

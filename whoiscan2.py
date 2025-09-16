import whois
from colorama import *

#global target

def whois_scan(target):
    try:
        info = whois.whois(target)
        info_dict = {
            "DOMAIN": info.domain_name,
            "REGISTRAR": info.registrar,
            "WHOIS SERVER": info.whois_server,
            "REFERRAL URL": info.referral_url,
            "CREATED": info.creation_date,
            "UPDATED": info.updated_date,
            "EXPIRE": info.expiration_date,
            "NAME SERVERS": info.name_servers,
            "DOMAIN STATUS": info.status,
            "EMAILS": info.emails,
            "COUNTRY": info.country,
            "CITY": info.city,
            "ZIPCODE": info.zipcode,
            "STATE": info.state,
            "PHONE": info.phone,
            "FAX": info.fax,
            "ADDRESS": info.address,
            "POSTAL CODE": info.postalcode,
            "REGISTRAR URL": info.registrar_url,
            "REGISTRAR WHOIS": info.registrar_whois_server,
            "REGISTRAR NAME": info.registrar_name,
            "REGISTRAR EMAIL": info.registrar_email,
            "REGISTRAR PHONE": info.registrar_phone,
            "REGISTRAR FAX": info.registrar_fax,
            "REGISTRAR ADDRESS": info.registrar_address,
            "REGISTRAR POSTAL CODE": info.registrar_postalcode,
            "REGISTRAR CITY": info.registrar_city,
            "REGISTRAR STATE": info.registrar_state,
            "REGISTRAR COUNTRY": info.registrar_country,
            "REGISTRAR ZIPCODE": info.registrar_zipcode
        }
        return info_dict
    except Exception as e:
        return {"ERROR": f"Unable to retrieve WHOIS information. {e}"}
# -*- coding:utf-8 -*-
#Taiwan No.1
#pip install ipwhois

from datetime import datetime
from ipwhois import IPWhois

ip_lists = []
try:
    with open('ip_lists.txt','r') as f:
        ip_lists = [line.rstrip() for line in f]
except:
    print('read ip_lists.txt Error')

def main():
    global ip_lists
    for _ in ip_lists:
        try:
          obj = IPWhois(_)
          results = obj.lookup_whois()
          print(f"IP: {_} country is {results['asn_country_code']}")
        except:
          print(f"IP: {_} is private or not found")

if __name__ == '__main__':
    print(datetime.now())
    main()
    print('-'*30)
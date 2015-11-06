from ipwhois import IPWhois
from pprint import pprint
import socket

def extractDNS(ipaddr):
	obj = IPWhois(ipaddr)
	results = obj.lookup_rdap(depth=1)
	pprint(results)

def extractIP(host):
	return socket.gethostbyname(host)

def main():
	host="www.google.com"
	extractDNS(extractIP(host))

if __name__ == '__main__':
	main()
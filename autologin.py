import  os
os.system("pip install -U autologin &> /dev/null")

import subprocess
import socket

def internet_connected(host="8.8.8.8", port=53):
	"""
	Checking internet connectivity
	Host: 8.8.8.8 (google-public-dns-a.google.com)
	OpenPort: 53/tcp
	Service: domain (DNS/TCP)
	"""
	try:
		socket.setdefaulttimeout(1)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except Exception as ex:
		pass
	return False

def autologin(url,username,password):
	"""
	Autologin to captive portal
	"""
	

def main():
	status = internet_connected()
	if status:
		autologin('https://192.168.56.2:8090/httpclient.html', '17mcmc21', 'cnf2017')

if  __name__ =='__main__':
    main()

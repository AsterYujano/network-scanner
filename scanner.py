import socket
import re
import os
import subprocess

print("[+] choice :")
print(" (1) - Scan network")
print(" (2) - Hello World")

hosts = []
choice = int(input())
ip = '192.168.0.'
x=0
if choice == 1:
	while(x<=20): #255
		p = subprocess.Popen('ping '+ip+str(x)+"-n 1",stdout=subprocess.PIPE, shell=True)
		out, error = p.communicate()
		out = str(out)
		find = re.search("Destination host unreachable", out)
		if find is None:
			hosts.append(ip+str(x))
			print("[+] Host found")
			x=x+1
	print("+------------+")
	print("+   Host(s)  +")
	print("+------------+")
	for host in hosts:
		try:
			name, a, b = socket.gethostbyaddr(host)
		except:
			name = "Not Found"
		print('| ' + host + " | " + name)
elif choice == 2:
	print("Hello World!")
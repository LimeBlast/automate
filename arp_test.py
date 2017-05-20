from scapy.all import *

buttons = {
    'goodnight': "ac:63:be:39:43:68",  # Nescafe Dolce Gusto
    'lunch': "ac:63:be:7c:60:90",  # Biona Organic
    'armchair': "ac:63:be:7b:85:8c",  # Right Guard
    'desk': "0c:47:c9:e7:46:e5"  # Fiesta kitchen towel
}
second_arp = False


def arp_detect(pkt):
    if pkt[ARP].op == 1:  # network request
        if pkt[ARP].hwsrc == buttons['armchair']:
            print('Right Guard')


if second_arp == False:
    sniff(prn=arp_detect, filter='arp', store=0)
    second_arp = True
else:
    second_arp = False

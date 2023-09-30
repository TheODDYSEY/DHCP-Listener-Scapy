from scapy.all import *
import time


def listen_dhcp():
    # Make sure it is DHCP with the filter options
    sniff(prn=print_packet, filter='udp and (port 67 or port 68)')
from scapy.all import sniff

# Callback function to process packets
def packet_callback(packet):
    print(packet.summary())  # Print packet details

# Start sniffing (change count=None for infinite capture)
sniff(prn=packet_callback, count=10)

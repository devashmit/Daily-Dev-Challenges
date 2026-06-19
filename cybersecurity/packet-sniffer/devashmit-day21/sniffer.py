"""Network Packet Sniffer with Scapy — Day 21 Cybersecurity | Author: devashmit
ETHICS: Only use on networks you own or have permission to monitor."""
from scapy.all import IP, TCP, UDP, ICMP, sniff, wrpcap

PCAP="capture.pcap"; captured=[]
PROTO={6:"TCP",17:"UDP",1:"ICMP"}

def handle(pkt):
    if not pkt.haslayer(IP): return
    ip=pkt[IP]; proto=PROTO.get(ip.proto,f"OTHER({ip.proto})"); size=len(ip.payload)
    print(f"  [{proto:<5}]  {ip.src:<18} → {ip.dst:<18}  {size} bytes")
    captured.append(pkt)

def main():
    print("\n🔐 Network Packet Sniffer\n   Only use on networks you own or have permission.\n")
    try:
        count=int(input("Packets to capture (e.g. 20): ").strip())
        bpf=input("BPF filter (e.g. 'tcp', blank = all): ").strip()
    except ValueError: count,bpf=20,""
    print(f"\n  Capturing {count} packet(s)... Ctrl+C to stop early\n")
    try: sniff(filter=bpf or None,prn=handle,count=count,store=False)
    except KeyboardInterrupt: print("\n  Stopped.")
    except PermissionError: print("\nError: Run as root/admin."); return
    if captured:
        wrpcap(PCAP,captured); print(f"\n✅ {len(captured)} packet(s) captured → {PCAP}")
    else: print("\nNo packets captured.")

if __name__=="__main__": main()

from scapy.all import ARP, Ether, srp
import socket

def get_mac(ip):
    """
    Returns the MAC address of a given IP address
    """
    try:
        # Create ARP packet
        arp = ARP(pdst=ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        # Send the packet and receive the response
        result = srp(packet, timeout=2, verbose=False)[0]

        # Extract MAC address from the response
        return result[0][1].hwsrc if result else None
    except IndexError:
        return None

def scan_network(ip_range):
    """
    Scans the network for active devices
    """
    devices = []
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=False)[0]

    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        
        devices.append({'ip': ip, 'mac': mac, 'hostname': hostname})

    return devices

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"  # Adjust based on your network's IP range
    devices = scan_network(ip_range)
    print("Connected devices:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {device['hostname']}")

#!/usr/bin/env python3

import argparse
import subprocess
from scapy.all import *
from scapy.layers.l2 import *
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

print(Fore.WHITE + Style.BRIGHT + r"""                                                                                         
MMMMMMMMMMMMMWWMMMMMWKXWMMMMMMMMMMMMMMMMMMWOdOXWMMMMMMMMMMMMMMMMWK0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNWMMMMMMMMMMMMM
MMMMMMMMMMMMNxcxXMMMXc'oKWMMMMMMMMMMMMMMMWk. .dNMMMMMMMMMMMMMMMXo..;xNMMMMMMMMMX0NMMMMMMMMMMMMMMMWOONMMWx;lONMMMMMMMMMMM
MMMMMMMMMMW0:  .oNMMNc  .;d0NMMMMMMMMMMMWk. .oXMMMMMMMMMMMMMWXd'     ,dXWMMMMMMx';kNMMMMMMMMMMMNO:.:XMMWd. .;dKWMMMMMMMM
MMMMMMMMWKl. .:kNMMMNl .l:..'cxKNMMMMMMWk. 'kWMMMMMMMMMMMWXdc,..'  .'. .l0WMMMMx.  ,xNMMMMMMMNO:.  ;XMMWd..c;..ckNMMMMMM
MMMMMMWKo. .l0WMMMMMWl ,KWKd;. .oNMMMMWx. ;0WMMMMMMMMMMW0o'  .lKx. ;KO:. .:kNMMx. ...,xXMMMNk:...  ;KMMWd.,KW0l'.'lONMMM
MMMMWKo. .lKWMMMMMMMWo  ;xKWN0ooKMMMMNd..lXMMMMMMMMMMMMNo. ;d0WMO. :XMNk;  :KMMx..dKo..'d0k;..:kx. ,KMMWd.,KMMNx.  ;0WMM
MMWKo. .oKWMMMMMMMMMWo .'..;oOXWMMMMXl. ,x000KKXXXXNNWMMWOkXMMMMO. cNMMMNkkNMMMx..dMWKo' . .cONMk. ,KMMWd.,KNk:..,dKWMMM
MM0;  .kWMMMMMMMMMMMWo ;0Kd;..'oXMMNd'..............:0WMMMMMMMMMO. cNMMMMMMMMMWd..dWMMMXd:l0WMMMk. ,0MMWd .:, .;kNMMMMMM
MMNO;. 'dXWMMMMMMMMMWl ,KMMN0l;dNMMWNXKK00OOkkxd,  .xWMMMMMMMMMMO. :XMMMMMMMMMWd. oWMMMMMWWMMMMMx. '0MMWo    'kNMMMMMMMM
MMMMNk;  'oKWMMMMMMMNl ,KMMMMWWWMMMMMMMMMMMMMMNx. .kWMMMMMMMMMMMk. :XMMMMMMMMMWo  oWMMMMMMMMMMMMx. '0MMWo  . .,oKWMMMMMM
MMMMMMNx,  .l0WMMMMMNc '0MMMMMMMMMMMMMMMMMMMMXl. 'OWMMMMMMMMMMMMx. ;XMMMMMMMMMWo  lWMMMMMMMMMMMWd. .OMMNl .dx;. .:xXWMMM
MMMMMMMMXd'  .cONMMMX: .OMMMMMMMMMMMMMMMMMMMK:  ,OWMMMMMMMMMMMMWd. ,KMMMMMMMMMNl  cNMMMMMMMMMMMWd  .OMMNc .OMNOl.  .oXMM
MMMMMMMMMWXo.  .oNMMK; .kMMMMMMMMMMMMMMMMMWO,  ,0MMMMMMMMMMMMMMWo  '0MMMMMMMMMN:  :XMMMMMMMMMMMWo  .kMMX: .xMMMWXd;;kNMM
MMMMMMMMMMMW0c,lKWMM0' .xWMMMMMMMMMMMMMMMWO'  ;0MMMMMMMMMMMMMMMNl  .OMMMMMMMMMXc..cXMMMMMMMMMMMWd..'kMMX:..xWMMMMMWNWMMM
MMMMMMMMMMMMMWNWMMMMXxlo0WMMMMMMMMMMMMMMMMXkllKMMMMMMMMMMMMMMMMNc  .kMMMMMMMMMWXKKXWMMMMMMMMMMMMNKKXNMMWX0KNMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMNOoodKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                                                                                                                                                                                               
""")
print(Fore.WHITE + Style.BRIGHT + "VLAN L2 Pivoting Instrument")
print(Fore.WHITE + Style.BRIGHT + "Author: Caster, @c4s73r, <c4s73r@protonmail.com>\n")


def vlan_sniffer(interface, timeout):
    print(Fore.YELLOW + Style.BRIGHT + "[+] Search for VLANs. . .")
    vlan_ids = set()

    def sniff_dot1q(pkt):
        if pkt.haslayer(Dot1Q):
            vlan_ids.add(pkt[Dot1Q].vlan)

    sniff(iface=interface, prn=sniff_dot1q, timeout=timeout)

    if len(vlan_ids) == 0:
        print(
            Fore.YELLOW + Style.BRIGHT + f"   [*] No VLANs found in {interface} traffic during the last {timeout} seconds.")
        return
    print(Fore.YELLOW + Style.BRIGHT + f"   [+] Detected VLANs: {', '.join(str(vlan_id) for vlan_id in vlan_ids)}")

    for vlan_id in vlan_ids:
        viface_name = f"{interface}.{vlan_id}"
        subprocess.call(
            ["sudo", "ip", "link", "add", "link", interface, "name", viface_name, "type", "vlan", "id", str(vlan_id)],
            subprocess.DEVNULL, stderr=subprocess.PIPE)
        subprocess.call(["sudo", "ip", "link", "set", viface_name, "up"], subprocess.DEVNULL, stderr=subprocess.PIPE)
    print(
        Fore.WHITE + Style.BRIGHT + f"   [*] Created virtual interfaces for the following VLANs: {', '.join(str(vlan_id) for vlan_id in vlan_ids)}    \n   After this - you can receive IP address via DHCP or configure the address statically. Go ahead.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", type=str, required=True, help="Interface to listen for traffic")
    parser.add_argument("--timeout", type=int, required=True, dest="timeout", help="How long the tool will listen to traffic")
    args = parser.parse_args()

    vlan_sniffer(args.interface, args.timeout)

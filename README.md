# HIVE
VLAN L2 Pivoting Instrument

This tool analyzes traffic for VLAN ID for gaining access to other VLAN segments. "HIVE" is completely self-contained and does not create any noise on the air. After traffic analysis, the tool creates virtual VLAN interfaces, to gain access to VLAN segments.

# Disclaimer

**All information contained in this repository is provided for educational and research purposes only. The author is not responsible for any illegal use of this tool**

In fact, the phenomenon of L2 Pivoting occurs, when the attacker gained access to a VLAN segment that was originally not supposed to be accessed. The experimental direction I am exploring.

## Impact & Scenartio
This tool is worth using if you are on a **TRUNK PORT**. The following scenarios usually contribute to this:

1) You connected to a port where VoIP and the computer itself were connected in the gap. Often enough it happens when the port is configured in the trunk for this purpose;
2) A hypervisor has been accessed, which in turn is connected to the trunk port;
3) The attacker performed a DTP injection, thereby ending up on the trunk port (this attack vector is rare, due to the peculiarities of the DTP protocol);
4) The attacker gained access to the switch he is connected to and switched himself to Trunk;

## Installation
```
git clone https://github.com/c4s73r/HIVE
sudo pip3 install -r requirements.txt
```
## Usage
This tool takes two arguments as input:

1) The interface;
2) Timeout. this is the time during which the tool will listen to the traffic. choose this parameter wisely

```
python3 HIVE.py --help
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

VLAN L2 Pivoting Instrument
Author: Caster, @c4s73r, <c4s73r@protonmail.com>

usage: HIVE.py [-h] --interface INTERFACE --timeout TIMEOUT

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Interface to listen for traffic
  --timeout TIMEOUT     How long the tool will listen to traffic
  ```
```
sudo python3 HIVE.py --interface ethX --timeout 60
```

## Last Word
[I was inspired by the track "The HIVE" (VIP REMIX)](https://youtu.be/pZZ-ELvRGeI?t=291) when I wrote this tool. This dedicated to KLOUD.

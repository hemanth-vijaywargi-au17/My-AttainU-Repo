"""
Q-2) Explain DHCP, ARP and NAT. (5 marks)
(Easy)
"""
"""
DHCP
But how exactly a network interface is assigned an IP-address? One of the options – manually. The disadvantage: 
handwork. If you're no good with your hands, you can configure duplicate addresses and get a conflict :)
Another option: Dynamic Host Configuration Protocol (DHCP), a protocol used for setting different configuration, 
including IP-addresses, automatically.
Refer to RFC documentation for more details on DHCP: https://www.ietf.org/rfc/rfc2131.txt
For DHCP to work, you need a DHCP-server, which will assign IP-addresses, and a DHCP-client on your device,
 which will request for an address. At home, the DHCP-server is usually located in router.
In order to understand how exactly DHCP works, you need to focus on "broadcasting". This is a process, 
in which our server transfers a message to all servers in the network, as it doesn't know where exactly the 
information it needs is located. Such a broadcast communication is close to a radio broadcasting.
In case of DHCP, it happens like this:
A DHCP-client sends a broadcast message with a request "I need an IP-address"
A DHCP-server catches it and sends back also a broadcast message "I have an IP-address x.x.x.x, do you want it?"
The DHCP-client receives the message and sends another one: "Yes, I want the address x.x.x.x"
The DHCP-server answers "Ok, then x.x.x.x belongs to you"
NAT
When you were reading about CIDR, there was something that might get your attention: even if we divide the network into many blocks, the total
 amount of IP-addresses isn't going to increase. Actually, a combination of private and public addresses is always used.
  Usually, one public address hides a lot of machines, each one having its own private address.
This is also true for our VMs. Each one has the private IP-address from the block 192.168.122.0/24, and all of 
them are hidden behind the public address of the host machine.
The host machine, if we continue to use our private laptop at home as it, is hidden behind our Wi-Fi router and
 also doesn't have a public address.
"""
def isIPv4(ip):
    octets = ip.split(".")
    # Check Number of Octets
    if len(octets) != 4:
        return False

    for oct in octets:
        # Length Check
        if len(oct) == 0 or len(oct) > 3:
            return False
        # Leading Zero Check
        if len(oct) != 1 and oct[0] == "0":
            return False
        # Contains Invalid Character Check
        for i in oct:
            if not(ord(i) >= 48 and ord(i) <= 57):
                return False
        # Number in range 0 to 255 Check
        if int(oct) < 0 or int(oct) > 255:
            return False

    return True


def isIPv6(ip):
    hextets = ip.split(":")
    # Check Number of Hextets
    if len(hextets) != 8:
        return False

    for hex in hextets:
        # Length Check
        if len(hex) == 0 or len(hex) > 4:
            return False
        # Contains Invalid Character Check
        for i in hex:
            if not((ord(i) >= 48 and ord(i) <= 57) or
                   (ord(i) >= 97 and ord(i) <= 102) or
                    (ord(i) >= 65 and ord(i) <= 70)):
                return False

    return True


def validIPAddress(IP):
    if len(IP) >= 7 and len(IP) <= 15:
        if isIPv4(IP):
            return "IPv4"
    if len(IP) >= 15 and len(IP) <= 39:
        if isIPv6(IP):
            return "IPv6"
    return "Neither"


if __name__ == "__main__":
    ip1 = "124.123.161.188"
    ip2 = "2001:0db8:0001:0000:0000:0ab9:C0A8:0102"
    ip3 = "192.168.1"
    print(validIPAddress(ip1))
    print(validIPAddress(ip2))
    print(validIPAddress(ip3))

import nmap

scanner = nmap.PortScanner()

print("Hello, welcome to the nmap port scanner automation tool!")
print("<--------------------------------------------------------------->")

ip_address=input("Please enter the IP address which you wish to scan: ")
print("The IP which you've entered is: ", ip_address)
type(ip_address)

resp = input("""\nPlease enter the type of scan you want to run: 
                1)SYN ACK Scan
                2)UDP Scan 
                3)Comprehensive Scan\n""")
print("You've selected the following option:", resp)

if resp == "1":
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif resp == "2":
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['udp'].keys())

elif resp == "3":
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())

elif resp >= 4:
    print("Please enter a valid option!")


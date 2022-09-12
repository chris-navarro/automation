#!/bin/env python3

# Ip Scanner Script
# Created by Chris Navarro
# Date created - 09/07/2022

import networkscan

def main():

    # Userdefined inputs - Network to scan
    network = input("Enter the IP Prefix/Network Subnet(e.i. 192.168.0.0/28, 10.20.30.0/24, 172.16.80.0/23): ")

    # Create the Object
    netScan = networkscan.Networkscan(network)
   
    # Display Prefix information's
    print()
    print("Network to scan: " + str(netScan.network))
    print("Prefix to scan: " + str(netScan.network.prefixlen))
    print("Number of hosts to scan: " + str(netScan.nbr_host))
    print()
    # Run the scan of hosts using ping command
    print("Scanning online hosts...")
    print()
    netScan.run()
    #Display the IP address of all the hosts found
    print('List of Online Hosts found.')
    for address in netScan.list_of_hosts_found:
        print(address)
    # Display information
    print()
    print("Number of hosts found: " + str(netScan.nbr_host_found))
    print()
    print("Creating a hosts file...")
    #Creates a yaml file with the list of hosts found
    res = netScan.write_file()
    # Error while writting the file?
    if res: # Yes
        print("Write errir with the file" + netScan.filename)
    else: # No Error
        print("Data saved into file " + netScan.filename)
    print()
    
if __name__ == '__main__':
    main()
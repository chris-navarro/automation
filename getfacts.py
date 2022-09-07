#!/bin/env python3

import napalm
from tabulate import tabulate
 
def main():
 
    ios_driver = napalm.get_network_driver("ios")
    nxos_driver = napalm.get_network_driver("nxos")
    eos_driver = napalm.get_network_driver("eos")
 
    device_list = [
                    ["192.168.0.210","ios", "router"],
                    ["192.168.10.2", "eos", "switch"],
                    ["192.168.10.3", "eos", "switch"],
                    ["192.168.10.11", "eos", "switch"],
                    ["192.168.10.12", "eos", "switch"],
                    ["192.168.10.13", "nxos", "switch"],
                    ["192.168.10.14", "nxos", "switch"]
                ]
 
    network_devices = []
    for device in device_list:
        if device[1] == "ios":
            network_devices.append(
                            ios_driver(
                            hostname = device[0],
                            username = "devuser",
                            password = "Root1234",
                            optional_args = {"secret":"root123"},
                            )
                              )
        elif device[1] == "nxos":
            network_devices.append(
                            nxos_driver(
                            hostname = device[0],
                            username = "devuser",
                            password = "Root1234",
                            )
                              )
        elif device[1] == "eos":
            network_devices.append(
                            eos_driver(
                            hostname = device[0],
                            username = "devuser",
                            password = "Root1234",
                            optional_args = {"enable_password":"root123"},
                            )
                              )
 
    devices_table = [["hostname", "vendor", "model", "uptime", "serial_number"]]
 
    for device in network_devices:
        print(f"Connecting to {device.hostname} ...")
        device.open()
 
        print("Gathering Device Facts.")
        device_facts = device.get_facts()
 
        devices_table.append([device_facts["hostname"],
                              device_facts["vendor"],
                              device_facts["model"],
                              device_facts["uptime"],
                              device_facts["serial_number"]
                              ])
 
        device.close()
        print("Completed Successfuly.")
    print(tabulate(devices_table, headers="firstrow"))
 
if __name__ == '__main__':
    main()
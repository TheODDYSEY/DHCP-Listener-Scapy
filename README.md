
# DHCP Packet Listener

This Python script listens for DHCP (Dynamic Host Configuration Protocol) packets on the network and extracts relevant information from these packets, such as the MAC address, requested IP address, hostname, and vendor ID of the devices making DHCP requests.

## Prerequisites

- Python 3.x
- Scapy library (Python library for packet manipulation)

## Installation

Make sure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

Install the required Python library, Scapy, using pip:

```bash
pip install scapy
```

## Usage

To use this script, follow these steps:

1. Save the script as a Python (.py) file, e.g., `dhcp_listener.py`.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using Python:

```bash
python dhcp_listener.py
```

The script will start listening for DHCP packets on the network.

## Functionality

- The script listens for DHCP packets on the network using the Scapy library.

- It extracts the following information from DHCP packets:
  - MAC address of the device making the DHCP request.
  - Requested IP address by the device.
  - Hostname of the device.
  - Vendor ID of the device.

- The extracted information is printed to the console, along with a timestamp, when a DHCP packet is received.

## Example Output

Here's an example of the output when a DHCP packet is captured:

```
[2023-10-03 - 15:30:45] : 00:1a:2b:3c:4d:5e  -  MyComputer / Android requested 192.168.1.100
[2023-10-03 - 15:30:50] : 00:0f:6a:8b:9c:1d  -  MyPhone / iPhone requested 192.168.1.101
```

The output includes the timestamp, MAC address, hostname, vendor ID, and requested IP address of the devices making DHCP requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



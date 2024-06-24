Certainly! Below is the `README.md` formatted text for your GitHub page.

# Nmap Port Scanner Automation Tool

This is an nmap port scanner automation tool.
This project provides a simple Python-based interface for automating various types of network scans using the Nmap tool.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Scan Types](#scan-types)
- [Example](#example)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have Python 3 installed on your local machine.
- You have `nmap` installed on your local machine. You can download it from [here](https://nmap.org/download.html).
- You have the `python-nmap` library installed. You can install it using pip:

```sh
pip install python-nmap
```

## Installation

To install this project, follow these steps:

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/your-username/nmap-port-scanner.git
    ```

2. Navigate to the project directory:
    ```sh
    cd nmap-port-scanner
    ```

3. Ensure all dependencies are installed:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use the nmap port scanner automation tool, run the Python script and follow the on-screen instructions:

```sh
python scanner.py
```

You will be prompted to enter the IP address you wish to scan and the type of scan you want to run.

## Scan Types

The tool supports three types of scans:

1. **SYN ACK Scan**
    - Option: `1`
    - Description: This is the most common scan option. It performs a TCP SYN scan which is a basic and popular scan type.

2. **UDP Scan**
    - Option: `2`
    - Description: This scan checks for open UDP ports. UDP scanning is generally slower and more complex than TCP scanning.

3. **Comprehensive Scan**
    - Option: `3`
    - Description: This scan performs a detailed scan, including version detection, script scanning, and OS detection.

## Example

Here's an example of how the tool works:

1. Run the script:
    ```sh
    python scanner.py
    ```

2. Enter the IP address you wish to scan:
    ```
    Please enter the IP address which you wish to scan: 192.168.1.1
    ```

3. Select the type of scan:
    ```
    Please enter the type of scan you want to run: 
        1)SYN ACK Scan
        2)UDP Scan 
        3)Comprehensive Scan
    ```

4. View the scan results:
    The tool will display the Nmap version, scan information, IP status, protocols, and open ports.

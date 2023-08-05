import subprocess

def check_internet_connection():
    """
    Check internet connection by pinging a reliable host.

    Returns:
        bool: True if internet connection is available, False otherwise.
    """
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        return True
    except subprocess.CalledProcessError:
        return False

def connect_to_wifi(ssid, password):
    """
    Connect to a Wi-Fi network using the provided SSID and password.

    Parameters:
        ssid (str): The SSID of the Wi-Fi network.
        password (str): The password for the Wi-Fi network.

    Returns:
        bool: True if connection is successful, False otherwise.
    """
    try:
        subprocess.check_output(["nmcli", "device", "wifi", "connect", ssid, "password", password])
        return True
    except subprocess.CalledProcessError:
        return False

def scan_wifi_networks():
    """
    Scan available Wi-Fi networks.

    Returns:
        str: The output of the Wi-Fi scan command, or None if an error occurs.
    """
    try:
        output = subprocess.check_output(["nmcli", "device", "wifi", "list"], universal_newlines=True)
        return output
    except subprocess.CalledProcessError:
        return None

def find_free_wifi_network(networks):
    """
    Find a free Wi-Fi network from the list of scanned networks.

    Parameters:
        networks (str): The output of the Wi-Fi scan command.

    Returns:
        str: The SSID of a free Wi-Fi network, or None if none is found.
    """
    for line in networks.splitlines():
        if "free" in line.lower():
            ssid = line.split()[0]
            return ssid
    return None

def check_connection_type():
    """
    Check the current connection type (Wi-Fi, LAN, or Unknown).

    Returns:
        str: The connection type as a string.
    """
    try:
        output = subprocess.check_output(["ip", "route", "show", "default"], universal_newlines=True)
        if "wlan" in output:
            return "Wi-Fi"
        elif "eth" in output or "enp" in output:
            return "LAN"
        else:
            return "Unknown"
    except subprocess.CalledProcessError:
        return "Error"

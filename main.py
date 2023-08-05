import log_utils
import internet_utils

known_wifi = {
    "ssid": "TUMOLabsStudents",
    "password": "!@#Cat2023Yerevan$"
}

def connect_to_wifi_or_known_network():
    """
    Try to connect to Wi-Fi or the known network if there is no internet connection.
    """
    if not internet_utils.check_internet_connection():
        log_utils.log_message("No internet connection. Trying to connect to the known network...")
        if internet_utils.connect_to_wifi(known_wifi["ssid"], known_wifi["password"]):
            log_utils.log_message("Successfully connected to the known Wi-Fi network.")
        else:
            log_utils.log_message("Failed to connect to the known Wi-Fi network.")
    else:
        log_utils.log_message("You are connected to the Wi-Fi network")

def main():
    """
    Main function to handle Wi-Fi connectivity and network detection.

    This function tries to connect to a known Wi-Fi network or a free Wi-Fi network if the connection type is unknown.
    It logs the connection type and status of the connection attempts.
    """
    if internet_utils.check_internet_connection():
        log_utils.log_message("Raspberry Pi is connected to the internet.")
    else:
        # If the Raspberry Pi is not connected to the internet, proceed with the rest of the script
        connect_to_wifi_or_known_network()

        connection_type = internet_utils.check_connection_type()
        log_utils.log_message(f"Connection type: {connection_type}")

        if connection_type == "Unknown":
            wifi_networks = internet_utils.scan_wifi_networks()
            if wifi_networks:
                free_network_ssid = internet_utils.find_free_wifi_network(wifi_networks)
                if free_network_ssid:
                    if internet_utils.connect_to_wifi(free_network_ssid, None):
                        log_utils.log_message(f"Connected to a free Wi-Fi network: {free_network_ssid}")
                    else:
                        log_utils.log_message("Failed to connect to a free Wi-Fi network.")
                else:
                    log_utils.log_message("No free Wi-Fi network found.")
            else:
                log_utils.log_message("No internet connection")

if __name__ == "__main__":
    main()

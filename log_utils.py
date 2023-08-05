import time

LOGEFILE = "/home/climatenet/service/logfile.log"

def log_message(message):
    """
    Log a message to the specified log file.

    Parameters:
        message (str): The message to be logged.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_entry = f"[{timestamp}] {message}\n"
    with open(LOGEFILE, "a") as file:
        file.write(log_entry)

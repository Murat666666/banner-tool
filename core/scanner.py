import socket

class PortScanner:

    @staticmethod
    def is_open(host, port, timeout=1):
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except:
            return False
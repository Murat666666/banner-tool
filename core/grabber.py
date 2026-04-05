import socket

class BannerGrabber:
    def __init__(self, host, port, timeout=3):
        self.host = host
        self.port = port
        self.timeout = timeout

    def grab(self):
        try:
            with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:

                sock.settimeout(2)  # ✅ BURADA olmalı (with içinde)

                # HTTP için request gönder
                if self.port == 80:
                    request = f"HEAD / HTTP/1.1\r\nHost: {self.host}\r\n\r\n"
                    sock.sendall(request.encode())

                banner = sock.recv(1024)

                return banner.decode(errors="ignore").strip()

        except Exception as e:
            return f"Hata: {e}"
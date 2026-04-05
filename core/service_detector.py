class ServiceDetector:

    COMMON_PORTS = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS"
    }

    @staticmethod
    def detect(port, banner):
        banner_lower = str(banner).lower()

        # Banner-based detection
        if "ssh" in banner_lower:
            return "SSH"
        elif "ftp" in banner_lower:
            return "FTP"
        elif "http" in banner_lower:
            return "HTTP"
        elif "smtp" in banner_lower:
            return "SMTP"
        elif "imap" in banner_lower:
            return "IMAP"
        elif "pop3" in banner_lower:
            return "POP3"

        # Fallback: port-based
        return ServiceDetector.COMMON_PORTS.get(port, "Unknown")
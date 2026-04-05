from core.cve_lookup import CVELookup
import re

class Analyzer:
    def __init__(self):
        self.signatures = {
            "OpenSSH": r"OpenSSH[_ ]([\d\.]+)",
            "vsFTPd": r"vsFTPd[_ ]([\d\.]+)"
        }

    def analyze(self, banner):
        findings = []

        for service, pattern in self.signatures.items():
            match = re.search(pattern, banner)

            if match:
                version = match.group(1)

                cves = CVELookup.search(service.lower(), version)

                findings.append({
                    "service": service,
                    "version": version,
                    "cves": cves
                })

        return findings
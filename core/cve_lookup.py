import requests

class CVELookup:

    BASE_URL = "https://cve.circl.lu/api/search/"

    @staticmethod
    def search(service, version):
        try:
            url = f"{CVELookup.BASE_URL}{service}/{version}"
            response = requests.get(url, timeout=5)

            if response.status_code != 200:
                return []

            data = response.json()

            results = []

            for item in data.get("data", [])[:3]:  # max 3 CVE
                results.append({
                    "id": item.get("id"),
                    "summary": item.get("summary")
                })

            return results

        except Exception:
            return []
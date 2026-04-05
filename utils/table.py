def print_table(results, open_only=False):
    print("\nSCAN RESULTS\n")
    print(f"{'PORT':<8}{'STATUS':<10}{'SERVICE':<15}{'VULNS'}")
    print("-" * 50)

    for r in results:
        if open_only and r.get("status") != "open":
            continue

        port = r.get("port")
        status = r.get("status")
        service = r.get("service", "-")

        vulns = r.get("vulnerabilities", [])
        vuln_text = "YES" if vulns else "NO"

        print(f"{port:<8}{status:<10}{service:<15}{vuln_text}")
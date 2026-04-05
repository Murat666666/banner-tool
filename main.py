import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

from core.grabber import BannerGrabber
from core.analyzer import Analyzer
from core.scanner import PortScanner
from core.service_detector import ServiceDetector
from utils.logger import Logger
from utils.port_parser import parse_ports
from utils.table import print_table


def scan_port(host, port, open_only=False):
    # Port açık mı kontrol et
    if not PortScanner.is_open(host, port):
        if not open_only:
            Logger.error(f"[{port}] CLOSED")
        return {
            "host": host,
            "port": port,
            "status": "closed"
        }

    grabber = BannerGrabber(host, port)
    analyzer = Analyzer()

    banner = grabber.grab()
    service = ServiceDetector.detect(port, banner)
    findings = analyzer.analyze(banner)

    result = {
        "host": host,
        "port": port,
        "status": "open",
        "service": service,
        "banner": banner,
        "vulnerabilities": findings
    }

    return result


def main():
    parser = argparse.ArgumentParser(description="Advanced Banner & Port Scanner")

    parser.add_argument("host", help="Target host")

    parser.add_argument(
        "-p",
        "--ports",
        required=True,
        help="Ports (e.g. 21,22,80 or 20-100)"
    )

    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=10,
        help="Number of threads"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Save results to JSON file"
    )

    parser.add_argument(
        "--open-only",
        action="store_true",
        help="Show only open ports"
    )

    args = parser.parse_args()

    ports = parse_ports(args.ports)

    Logger.info(f"Scanning {args.host} ({len(ports)} ports) with {args.threads} threads")

    results = []

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [
            executor.submit(scan_port, args.host, port, args.open_only)
            for port in ports
        ]

        for future in tqdm(as_completed(futures), total=len(futures), desc="Scanning"):
            try:
                results.append(future.result())
            except Exception as e:
                Logger.error(f"Error: {e}")

    # tablo göster
    print_table(results, args.open_only)

    # json kaydet
    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)
        Logger.success(f"Results saved to {args.output}")

    Logger.success("Scan completed!")


if __name__ == "__main__":
    main()
def parse_ports(port_input):
    ports = []

    parts = port_input.split(",")

    for part in parts:
        part = part.strip()

        # Range: 20-80
        if "-" in part:
            start, end = part.split("-")
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))

    return list(set(ports))  # duplicate temizle
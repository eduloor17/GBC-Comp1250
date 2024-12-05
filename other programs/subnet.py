import ipaddress


def calculate_subnets(ip_network, subnet_mask):
    network = ipaddress.IPv4Network(f'{ip_network}/{subnet_mask}', strict=False)
    print(f"Network: {network.network_address}")
    print(f"Subnet Mask: {network.netmask}")
    print(f"Number of Subnets: {network.num_addresses // 2 ** (32 - network.prefixlen)}")
    print(f"Total IP Addresses: {network.num_addresses}")

    subnets = list(network.subnets(new_prefix=network.prefixlen + 1))
    for subnet in subnets:
        print(f"Subnet: {subnet.network_address} / {subnet.prefixlen}")


if __name__ == "__main__":
    ip_network = input("Enter the IP network (e.g., 192.168.1.0): ")
    subnet_mask = int(input("Enter the subnet mask (e.g., 24 for /24): "))
    calculate_subnets(ip_network, subnet_mask)
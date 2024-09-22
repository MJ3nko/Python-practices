import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="A script to demonstrate argument parsing with argparse.",
        epilog="Example: python script.py -u http://example.com -v -k -t 10"
    )

    # General options
    general = parser.add_argument_group('General options')
    general.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Enable verbose mode"
    )
    general.add_argument(
        "-u",
        "--url",
        dest="url",
        action="store",
        type=str,
        required=True,
        help="Specify the URL"
    )

    # Security options
    security = parser.add_argument_group('Security options')
    security.add_argument(
        "-k",
        "--insecure",
        dest="insecure_tls",
        action="store_true",
        default=False,
        help="Allow insecure server connections"
    )

    # Performance options
    performance = parser.add_argument_group('Performance options')
    performance.add_argument(
        "-t",
        "--threads",
        dest="threads",
        action="store",
        type=int,
        default=256,
        help="Number of threads (default: 256)"
    )

    return parser.parse_args()

if __name__ == "__main__":
    options = parse_args()
    print(options)

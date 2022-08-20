import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="description")
    parser.add_argument("-v", "--verbose", dest="verbose",
                        action="store_true", default=False,
                        help="Verbose mode")
    parser.add_argument("-u", "--url", dest="url",
                        action="store", type=str,
                        required=True, help="URL")
    parser.add_argument("-k", "--insecure", dest="insecure_tls",
                        action="store_true", default=False,
                        help="Allow insecure server connections")
    parser.add_argument("-t", "--threads", dest="threads",
                        action="store", type=int, default=256,
                        required=False, help="Number of threads (default: 20)")
    return parser.parse_args()


if __name__ == '__main__':
    options = parse_args()

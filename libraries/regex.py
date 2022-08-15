import re


def re_match(domain):
    # Return match object, apply regex at the start of the string
    match = re.match(r"http[s]?", domain)
    if match:
        print(match.group(0))


def re_findall(domain):
    regex_domain = r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    "[a-z0-9][a-z0-9-]{0,61}[a-z0-9]"
    results = re.findall(regex_domain, domain)
    if results:
        for result in results:
            print(result)


def re_search(domain, email, ipv4):
    # Uses match object
    regex_domain = r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    "[a-z0-9][a-z0-9-]{0,61}[a-z0-9]"
    domain_results = re.search(regex_domain, domain)
    email_results = re.search(r"[\w\.-]+@[\w\.-]+", email)
    ip_results = re.search(r"^((\d){1,3}\.){3}\d{1,3}", ipv4)

    if domain_results:
        print(domain_results.group(0))
    if email_results:
        print(email_results.group(0))
    if ip_results:
        print(ip_results.group(0))


def main():
    domain = "https://www.google.com"
    ip = "127.0.0.1"
    email = input("Input email:")
    re_match(domain)
    re_findall(domain)
    re_search(domain, email, ip)


if __name__ == "__main__":
    main()

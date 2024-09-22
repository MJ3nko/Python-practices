import re


def re_match(url):
    # Return match object, apply regex at the start of the string
    match = re.match(r"https?", url)
    if match:
        print(f"Match found: {match.group(0)}")
    else:
        print("No match found")


def re_findall(url):
    # Regex pattern to find domain parts
    regex_domain = r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,6}"
    results = re.findall(regex_domain, url)
    if results:
        for result in results:
            print(f"Found domain: {result}")
    else:
        print("No domains found")


def re_search(url, email, ipv4):
    # Regex patterns
    regex_domain = r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,6}"
    regex_email = r"[\w\.-]+@[\w\.-]+\.\w+"
    regex_ip = r"^((\d{1,3}\.){3}\d{1,3})$"

    # Search for patterns
    domain_results = re.search(regex_domain, url)
    email_results = re.search(regex_email, email)
    ip_results = re.search(regex_ip, ipv4)

    if domain_results:
        print(f"Domain found: {domain_results.group(0)}")
    else:
        print("No domain found")

    if email_results:
        print(f"Email found: {email_results.group(0)}")
    else:
        print("No email found")

    if ip_results:
        print(f"IP found: {ip_results.group(0)}")
    else:
        print("No IP found")


def main():
    url = "https://www.google.com"
    ip = "127.0.0.1"
    email = input("Input email: ").strip()
    re_match(url)
    re_findall(url)
    re_search(url, email, ip)


if __name__ == "__main__":
    main()

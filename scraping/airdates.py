import requests


def get_site_content(site_url):
    site_content = requests.get(site_url).text
    print(site_content)


def main():
    print("Scraping web page initialized")
    get_site_content("https://www.airdates.tv/#today")


if __name__ == '__main__':
    main()

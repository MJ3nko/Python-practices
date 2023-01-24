import requests


def get_site_content(site_url):
    site_content = requests.get(site_url).text
    print(site_content)


def main():
    print("Scraping web page initialized")
    get_site_content("https://www.nepremicnine.net/oglasi-oddaja/ljubljana-okolica/logatec,vrhnika/stanovanje/cena-do-1000-eur-na-mesec/?s=13&nadst%5B0%5D=vsa&nadst%5B1%5D=vsa")


if __name__ == '__main__':
    main()

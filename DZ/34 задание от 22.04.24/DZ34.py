import csv
import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    r = requests.get(url)
    return r.text


def get_data(html: str) -> None:
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("article", class_="project-card base-card padding-bg")

    for el in elements:
        try:
            name = el.find("h2", class_="name").text
        except AttributeError:
            name = ""

        try:
            url = el.find("div", class_="title").find("a")["href"]
        except AttributeError:
            url = ""

        try:
            description = el.find("p", class_="description").text
        except AttributeError:
            description = ""

        try:
            downloads = el.find("strong").text.strip()
        except AttributeError:
            downloads = ""

        data = {
            "name": name,
            "url": "https://modrinth.com" + url,
            "description": description,
            "downloads": downloads + " downloads",
        }

        write_csv(data)


def write_csv(data: dict) -> None:
    with open("plugins_modrinth.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow((data["name"], data["url"], data["description"], data["downloads"]))


def main() -> None:
    url = f"https://modrinth.com/plugins"
    get_data(get_html(url))


if __name__ == '__main__':
    main()

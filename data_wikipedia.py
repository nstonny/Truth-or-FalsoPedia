from bs4 import BeautifulSoup
import requests

def get_data_wikipedia(url):
        """Extracting table data from the url"""

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")

        tables = soup.find_all("table", class_="wikitable")
        data = []

        for table in tables:
            rows = table.find_all("tr")

            for row in rows[1:]:
                cols = row.find_all("td")
                if cols:
                    text = cols[0].get_text(strip=True)  # produces Domestic dog (Canis familiaris)[3]
                    if text:
                        text = text.split("(")[
                            0]  # produces ['Domestic dog ', 'Canis familiaris)[3]'] [0] keeps Domestic Dog
                        data.append(text.strip())
        return data
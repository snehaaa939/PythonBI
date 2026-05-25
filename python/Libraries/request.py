import requests
from bs4 import BeautifulSoup

url = "https://yetiairlines.com/flight-status"
response = requests.get(url)
print(response.status_code)
response_text = response.text
print(response_text)

soup_object = BeautifulSoup(response.text, "html.parser")
# print(soup_object.title)
print(soup_object.link)
all_links = soup_object.find_all("link")
print(all_links)
for link in all_links:
    print(link)

# flight_table= soup_object.find('table', {'id': 'flightInfo'})
# print(flight_table)


def parse_html_table_data(html_data):
    table_rows = html_data.find_all("tr")
    overall_data=[]
    for row in table_rows:
        row_data = []
        cell_data= row.find_all(['td', 'th'])
        for cell_value in cell_data:
            row_data.append(cell_value.get_text(strip=True))
        overall_data.append(row_data)
        print(overall_data)


flight_table = soup_object.find("table", {"id": "flightInfo"})
parse_html_table_data(flight_table)

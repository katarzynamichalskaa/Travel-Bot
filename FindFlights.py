from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode

class FindFlights():
    def __init__(self):
        self.base_url = "https://www.azair.eu/azfin.php"
        self.default_params = {
            'tp': '0',
            'searchtype': 'flexi',
            'srcAirport': 'Poznan[POZ]',
            'srcTypedText': 'pozn',
            'dstAirport': 'Anywhere[XXX]',
            'dstTypedText': 'any',
            'adults': '4',
            'children': '0',
            'infants': '0',
            'minHourStay': '0:45',
            'maxHourStay': '16:30',
            'minHourOutbound': '0:00',
            'maxHourOutbound': '24:00',
            'minHourInbound': '0:00',
            'maxHourInbound': '24:00',
            'depdate': '12.8.2024',
            'arrdate': '30.9.2024',
            'minDaysStay': '2',
            'maxDaysStay': '8',
            'nextday': '0',
            'autoprice': 'true',
            'currency': 'PLN',
            'wizzxclub': 'false',
            'flyoneclub': 'false',
            'blueairbenefits': 'false',
            'megavolotea': 'false',
            'schengen': 'false',
            'transfer': 'false',
            'samedep': 'true',
            'samearr': 'true',
            'dep0': 'true',
            'dep1': 'true',
            'dep2': 'true',
            'dep3': 'true',
            'dep4': 'true',
            'dep5': 'true',
            'dep6': 'true',
            'arr0': 'true',
            'arr1': 'true',
            'arr2': 'true',
            'arr3': 'true',
            'arr4': 'true',
            'arr5': 'true',
            'arr6': 'true',
            'maxChng': '1',
            'isOneway': 'return',
            'resultSubmit': 'Search'
        }
        self.full_url = ""

    def generate_url(self, params):
        encoded_params = urlencode(params)
        self.full_url = f"{self.base_url}?{encoded_params}"

    def get_content(self):

        try:
            response = requests.get(self.full_url)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def find_(self):
        budgetFligts = []
        content = self.get_content()

        if content:
            soup = BeautifulSoup(content, 'lxml')
            products = soup.find_all('div', class_='result')

            for product in products:
                price_and_lenght_of_stay = product.find('div', class_='totalPrice').text.strip()
                price = price_and_lenght_of_stay.split()[0]
                length_of_stay = price_and_lenght_of_stay.split()[5]

                if int(price) < 750:
                    from_ = product.find('span', class_='from').text.strip()
                    to_ = product.find('span', class_='to').text.strip()
                    link = product.find('div', class_='bookmark').find('a')['href']
                    budgetFligts.append([from_, to_, price + ' ' + self.default_params['currency'], length_of_stay + " days", "https://www.azair.eu/" + link])

            return budgetFligts

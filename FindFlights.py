from bs4 import BeautifulSoup
from GetContent import GetContent

class FindFlights(GetContent):

    def find_(self):
        budgetFligts = []
        content = self.get_content()

        if content:
            soup = BeautifulSoup(content, 'lxml')
            products = soup.find_all('div', class_='result')

            for product in products:
                price_and_lenght_of_stay = product.find('div', class_='totalPrice').text.strip()
                numeric_part = price_and_lenght_of_stay.split()[0]

                if int(numeric_part) < 750:
                    from_ = product.find('span', class_='from').text.strip()
                    to_ = product.find('span', class_='to').text.strip()
                    link = product.find('div', class_='bookmark').find('a')['href']
                    budgetFligts.append([price_and_lenght_of_stay, from_, to_, "https://www.azair.eu/" + link])

            return budgetFligts

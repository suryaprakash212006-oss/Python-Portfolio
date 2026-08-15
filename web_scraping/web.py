import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self,url):
        self.url = url
        self.user_agent  = {"User_Agent" :"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36 Edg/140.0.0.0"}

        self.response = requests.get(url = self.url, headers = self.user_agent).text
        self.soup = BeautifulSoup(self.response,"lxml")
    def product_title(self):
        title = self.soup.find("span",{"id":"productTitle"})
        if title is not None:
          return title.text
        else:
            return "Tag Not Found"

    def product_price(self):
        price = self.soup.find("span",{"class":"a-price-whole"})
        if  price is not None:
          return  price.text
        else:
          return "Tag Not Found"


device =PriceTracer(url="https://www.amazon.in/Samsung-Smartphone-Storage-Powerful-Snapdragon/dp/B0FDL5T1PF/ref=sr_1_1_sspa?crid=21AY4VNUQ08DN&dib=eyJ2IjoiMSJ9.6F9zxmqbhCO38LI-LW5u6qURo-LPHnmPsg4P_4EVTHeBzZIrUD1aC3up9zjJ8H1xV_swwZMUaVgtgqvBBgjNThIYcUmOSTucj031_0n_ZbqC4wFddXzNvXnxzfAjRnNsqhOnfX4g6qX0v-IQFW2VVP4_0-EWRjM-OOJUGf6sPUlpf5D_3oNnjRRIR-ePne2nHyC7tTfVEWbzDLqpeBz31sfjlYpk9Dk2UjYM5Ss8VCU.3My9vNN6poGs2_7D27O4y5rVXgZPF4FwoS0rF47I63A&dib_tag=se&keywords=samsung%2Bs25%2Bultra%2B5g%2Bmobile&nsdOptOutParam=true&qid=1757402160&refinements=p_123%3A46655&rnid=91049095031&sprefix=sa%2Caps%2C285&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
print(device.product_title())
print(device.product_price())

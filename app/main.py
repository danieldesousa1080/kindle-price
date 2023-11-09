from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
from database import Prices, create_db


url = 'https://www.amazon.com.br/kindle-11geracao-preto/dp/B09SWTG9GF/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=TFSTII5SXA73&keywords=kindle&qid=1699408985&sprefix=kindl%2Caps%2C205&sr=8-1&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751'

page_html = request.urlopen(url).read()

soup = BeautifulSoup(page_html,'html.parser')

all_prices = soup.find_all("span",{"class":["a-size-large a-color-price"]})

dict_prices = {'Kindle11':float(all_prices[0].text[3:].replace('.','').replace(",",".")),
                'paperwhite':float(all_prices[1].text[3:].replace('.','').replace(",",".")),
                'paperwhiteSE':float(all_prices[2].text[3:].replace('.','').replace(",",".")),
                'oasis':float(all_prices[3].text[3:].replace('.','').replace(",","."))}

pprint(dict_prices)
create_db()
Prices(date=datetime.now(),kindle11=dict_prices['Kindle11'],paperwhite=dict_prices['paperwhite'],paperwhiteSE=dict_prices['paperwhiteSE'],oasis=dict_prices['oasis']).save()
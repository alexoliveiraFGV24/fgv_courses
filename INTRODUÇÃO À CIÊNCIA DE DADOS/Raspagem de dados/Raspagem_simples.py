import requests
import re
from bs4 import BeautifulSoup

"""
html_doc =
<html>
    <body>
        <h1>Preces</h1>
        <ol>
            <li>suri gu Carlos Ivan</li>
            <li>suri gu César Camacho</li>
            <li>suri gu Yuri Saporito</li>
        </ol>
    </body>
</html>
"""


# O navevador que sabe interpretar HTML, CSS e JS
# Site para estudar scrap = https://webscraper.io/test-sites/


# soup = BeautifulSoup(html_doc, "html.parser") 
# Construtor - pega um HTML e um parser (mecanismo que caminha as strings e as analisa)
# print(soup.find("h1").get_text())


# Precisamos ver se o site aceita scraping
"""
url = "https://www.marketwatch.com/investing/stock/aapl"
page = requests.get(url)
print(page.status_code) # Queremos ver uma porta na casa dos 200 (requisição aceita) (nesse caso, o site não aceita, ele imprime 401)
"""

url = "https://br.investing.com/equities/apple-computer-inc"
page = requests.get(url)
# print(page.status_code)  # Esse funcionou (imprime 200)


soup = BeautifulSoup(page.text, "lxml")

# Faço uma procura mais geral (vou procural em div) e vou um pouco mais específico (procuro uma classe que tenha essa especificação) e depois transformo para texto (tiro as tags html)
current_price = soup.find("div", class_="text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]").text  
print("PREÇO ATUAL: {}".format(current_price))


# Mesma coisa 
closing_price = soup.find("dd", class_="whitespace-nowrap text-[#232526]").text
print("PREÇO DE FECHAMENTO: {}".format(closing_price))

# Acho a parte que possui a variância de 52 semanas, mas a variância diária também está lá. Então damos find_all
price_var_52 = soup.find_all("div", class_="mb-3 flex justify-between font-bold tracking-[0.2px]")[1]

# Vemos que há mais elementos do que precisamos, então fazemos outro find_all para a tag específica que queremos 
price_var_52 = price_var_52.find_all("span")

# Separamos os elementos da lista 
price_var_52_low = price_var_52[0].text
price_var_52_high = price_var_52[1].text

print("VARIÂNCIA MENOR (52 semanas): {}".format(price_var_52_low))
print("VARIÂNCIA MAIOR (52 semanas): {}".format(price_var_52_high))
import re 
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.nfl.com/standings/league/2023/reg"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

table = soup.find("table", {"summary": "Standings - Detailed View"})  # Pegamos uma tabela (pedaço) do html mandando um dicionário como regra

headers = []

for each_element in table.find_all("th"):  # Para cada elemento na tabela que tem a tag <th>
    title = each_element.text.strip()  # .strip() limpa os espaços em branco (\n, \t, \s) (o método strip funciona para stings)
    headers.append(title)  # Adiciono no cabeçalho todos os títulos

dataset = pd.DataFrame(columns=headers)  # Criamos um DataSet de colunas

for each_row in table.find_all("tr")[1:]:  # Aqui estamos percorrendo linha a linha (menos a primeira (linha 0))
    row_data = []
    
    first_td = each_row.find_all("td")[0].find("div", class_="d3-o-club-fullname").text.strip()  # Procuro a primeira linha
    first_td = re.sub(r"\s+", " ", first_td) # Substituo um monte de espaços em branco por um só

    row_data.append(first_td)

    for each_td in each_row.find_all("td")[1:]:  # Pego todas as outras linhas (menos a primeira)
        row_data.append(each_td.text.strip())

    dataset.loc[len(dataset)] = row_data  # Forma de acessar uma linha de um DataSet

print(dataset) # (se você quiser ver no terminal)

dataset.to_csv("nfl_rip.csv")  # Salva a tabela python em excel
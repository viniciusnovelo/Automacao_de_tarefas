import pyautogui
import time
from acessar_chrome_site import acessar_plataforma_site
from fazer_login import login

pyautogui.PAUSE = 0.3

# 1- abrir o sistema da empresa
info = acessar_plataforma_site("chrome", "https://dlp.hashtagtreinamentos.com/python/intensivao/login")

info.acessar_plataforma()
info.acessar_site()
# esperar três segundos para o site carregar

time.sleep(3)

# 2- fazer o login

login = login("astronautadeatenas@gmail.com", "astronauta123athen")
login.preencher_email_senha(865, 483)

# 3- Importar a base de dados dos produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(3)

# 4, 5- Cadastrar 1 produto e o resto

for linha in tabela.index:

    # clicar no campo de código
    
    #time.sleep(2)
    # pegar da tabela o valor do campo que a gente quer preencher
    
    # preencher o campo
    #pyautogui.click(x=799, y=212)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.press("tab")   
    pyautogui.write(str(codigo))
    print(tabela.loc[linha, "codigo"])
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan" :
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    pyautogui.click(x=219, y=324)

 
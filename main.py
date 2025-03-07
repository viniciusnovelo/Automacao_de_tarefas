import pyautogui
import time
from acessar_chrome_site import acessar_plataforma_site
from fazer_login import login

pyautogui.PAUSE = 0.3

# 1- Open the company's system
info = acessar_plataforma_site("chrome", "https://dlp.hashtagtreinamentos.com/python/intensivao/login")

info.acessar_plataforma()
info.acessar_site()
# Wait three seconds for the site to load

time.sleep(3)

# 2- Log in

login = login("astronautadeatenas@gmail.com", "astronauta123athen")
login.preencher_email_senha(865, 483)

# 3- Import the product database
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(3)

# 4, 5- Register 1 product and the rest

for linha in tabela.index:

    # Click on the code field
    
    #time.sleep(2)
    # Get the value of the field we want to fill from the table
    
    # Fill the field
    #pyautogui.click(x=799, y=212)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.press("tab")   
    pyautogui.write(str(codigo))
    print(tabela.loc[linha, "codigo"])
    # Move to the next field
    pyautogui.press("tab")
    # Fill the field
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
    pyautogui.press("enter") # Register the product (submit button)
    # Scroll all the way up
    pyautogui.scroll(5000)
    pyautogui.click(x=219, y=324)
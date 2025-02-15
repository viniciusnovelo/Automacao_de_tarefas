import pyautogui
import time
pyautogui.PAUSE = 0.3

class acessar_plataforma_site:

    def __init__(self, nome_plataforma, nome_site):

        self.nome_plataforma=nome_plataforma
        self.nome_site=nome_site

    def acessar_plataforma(self):
        pyautogui.press("win")
        pyautogui.write(f"{self.nome_plataforma}")
        pyautogui.press("enter")
        time.sleep(1)

        if self.nome_plataforma == "chrome":
            pyautogui.click(x=1085, y=447)
        
    def acessar_site(self):
        if self.nome_plataforma == "chrome":

            pyautogui.write(f"{self.nome_site}")
            pyautogui.press("enter")
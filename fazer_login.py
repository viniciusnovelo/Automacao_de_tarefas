import pyautogui
import time
pyautogui.PAUSE=0.3

class login:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def preencher_email_senha(self, posicao_campo_email_x, posicao_campo_email_y):
        self.posicao_campo_email_x = posicao_campo_email_x
        self.posicao_campo_email_y = posicao_campo_email_y

        pyautogui.click(x=self.posicao_campo_email_x, y=self.posicao_campo_email_y)
        pyautogui.write(f"{self.email}")
        pyautogui.press("tab")
        pyautogui.write(f"{self.senha}")
        pyautogui.press("tab")
        pyautogui.press("enter")
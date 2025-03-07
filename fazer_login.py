import pyautogui
import time

# Set a default pause of 0.3 seconds between PyAutoGUI actions
pyautogui.PAUSE = 0.3

# Define a class for handling login functionality
class login:
    # Constructor to initialize email and password
    def __init__(self, email, senha):
        self.email = email  # Store the email
        self.senha = senha  # Store the password

    # Method to fill in the email and password fields and submit the form
    def preencher_email_senha(self, posicao_campo_email_x, posicao_campo_email_y):
        # Store the coordinates of the email field
        self.posicao_campo_email_x = posicao_campo_email_x
        self.posicao_campo_email_y = posicao_campo_email_y

        # Click on the email field at the specified coordinates
        pyautogui.click(x=self.posicao_campo_email_x, y=self.posicao_campo_email_y)
        
        # Enter the email
        pyautogui.write(f"{self.email}")
        
        # Move to the password field
        pyautogui.press("tab")
        
        # Enter the password
        pyautogui.write(f"{self.senha}")
        
        # Move to the submit button and press Enter
        pyautogui.press("tab")
        pyautogui.press("enter")
import pyautogui
import time

# Set a default pause of 0.3 seconds between PyAutoGUI actions
pyautogui.PAUSE = 0.3

# Define a class for accessing a platform and website
class acessar_plataforma_site:

    # Constructor to initialize the platform name and website URL
    def __init__(self, nome_plataforma, nome_site):
        self.nome_plataforma = nome_plataforma  # Store the platform name (e.g., "chrome")
        self.nome_site = nome_site  # Store the website URL

    # Method to open the platform (e.g., Chrome)
    def acessar_plataforma(self):
        pyautogui.press("win")  # Open the Start menu (Windows key)
        pyautogui.write(f"{self.nome_plataforma}")  # Type the platform name
        pyautogui.press("enter")  # Press Enter to open the platform
        time.sleep(1)  # Wait for 1 second for the platform to open

        # If the platform is Chrome, click on the "New Tab" button
        if self.nome_plataforma == "chrome":
            pyautogui.click(x=1085, y=447)  # Coordinates for the "New Tab" button
    
    # Method to access the specified website
    def acessar_site(self):
        # If the platform is Chrome, type the website URL and press Enter
        if self.nome_plataforma == "chrome":
            pyautogui.write(f"{self.nome_site}")  # Type the website URL
            pyautogui.press("enter")  # Press Enter to load the website
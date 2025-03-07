# Product Registration Automation with PyAutoGUI

This project automates the registration of products on an online platform using the PyAutoGUI library to simulate user interactions. It accesses the website, logs in, and fills out the product registration fields with data extracted from a CSV file.

## Features

- Automatically accesses the product registration website.
- Logs into the platform with predefined credentials.
- Reads a CSV file containing the list of products to be registered.
- Automatically fills out the registration form fields.
- Submits the registered products and restarts the process until all products are registered.

## Technologies Used

- Python
- PyAutoGUI
- Pandas
- Time

## Prerequisites

Before running the project, install the necessary libraries with the following command:

```bash
pip install pyautogui pandas
```

## How to Run

1. Ensure that Google Chrome is installed on your system.
2. Modify the `produtos.csv` file with the products you want to register.
3. Run the Python script:
   ```bash
   python main.py
   ```
4. The program will open the browser, access the platform, and perform the registrations automatically.

## Project Structure

```
/
|-- acessar_chrome_site.py  # Script to open the browser and access the website
|-- fazer_login.py          # Script to fill in credentials and log in
|-- main.py                 # Main script that automates the product registration
|-- produtos.csv            # Database with the products to be registered
|-- README.md               # Project documentation
```

## Example of the `produtos.csv` File

The CSV file should contain the following columns:

```
codigo,marca,tipo,categoria,preco_unitario,custo,obs
123,MarcaX,Eletrônico,Celular,1500,1200,Produto novo
456,MarcaY,Eletrônico,Notebook,3000,2500,Em promoção
```

## Notes

- The form fields are filled using the "TAB" key to navigate between them.
- If the observation field is empty, it will be ignored.
- The program includes wait times (`time.sleep()`) to ensure that elements load correctly.

## Author

Vinícius Vilela Novelo

---

### Translated README.md

```markdown
# Product Registration Automation with PyAutoGUI

This project automates the registration of products on an online platform using the PyAutoGUI library to simulate user interactions. It accesses the website, logs in, and fills out the product registration fields with data extracted from a CSV file.

## Features

- Automatically accesses the product registration website.
- Logs into the platform with predefined credentials.
- Reads a CSV file containing the list of products to be registered.
- Automatically fills out the registration form fields.
- Submits the registered products and restarts the process until all products are registered.

## Technologies Used

- Python
- PyAutoGUI
- Pandas
- Time

## Prerequisites

Before running the project, install the necessary libraries with the following command:

```bash
pip install pyautogui pandas
```

## How to Run

1. Ensure that Google Chrome is installed on your system.
2. Modify the `produtos.csv` file with the products you want to register.
3. Run the Python script:
   ```bash
   python main.py
   ```
4. The program will open the browser, access the platform, and perform the registrations automatically.

## Project Structure

```
/
|-- acessar_chrome_site.py  # Script to open the browser and access the website
|-- fazer_login.py          # Script to fill in credentials and log in
|-- main.py                 # Main script that automates the product registration
|-- produtos.csv            # Database with the products to be registered
|-- README.md               # Project documentation
```

## Example of the `produtos.csv` File

The CSV file should contain the following columns:

```
codigo,marca,tipo,categoria,preco_unitario,custo,obs
123,MarcaX,Eletrônico,Celular,1500,1200,Produto novo
456,MarcaY,Eletrônico,Notebook,3000,2500,Em promoção
```

## Notes

- The form fields are filled using the "TAB" key to navigate between them.
- If the observation field is empty, it will be ignored.
- The program includes wait times (`time.sleep()`) to ensure that elements load correctly.

## Author

Vinícius Vilela Novelo
```
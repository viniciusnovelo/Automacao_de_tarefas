# Automação de Cadastro de Produtos com PyAutoGUI

Este projeto automatiza o cadastro de produtos em uma plataforma online utilizando a biblioteca PyAutoGUI para simular interações do usuário. Ele realiza o acesso ao site, faz login e preenche os campos de cadastro de produtos com dados extraídos de um arquivo CSV.

## Funcionalidades

- Acessa automaticamente o site de cadastro de produtos.
- Faz login na plataforma com credenciais predefinidas.
- Lê um arquivo CSV contendo a lista de produtos a serem cadastrados.
- Preenche os campos do formulário de cadastro de forma automatizada.
- Envia os produtos cadastrados e reinicia o processo até cadastrar todos os produtos.

## Tecnologias Utilizadas

- Python
- PyAutoGUI
- Pandas
- Time

## Pré-requisitos

Antes de executar o projeto, instale as bibliotecas necessárias com o seguinte comando:

```bash
pip install pyautogui pandas
```

## Como Executar

1. Certifique-se de que o Google Chrome está instalado em seu sistema.
2. Altere o arquivo `produtos.csv` com os produtos que deseja cadastrar.
3. Execute o script Python:
   ```bash
   python main.py
   ```
4. O programa abrirá o navegador, acessará a plataforma e realizará os cadastros automaticamente.

## Estrutura do Projeto

```
/
|-- acessar_chrome_site.py  # Script para abrir o navegador e acessar o site
|-- fazer_login.py          # Script para preencher credenciais e fazer login
|-- main.py                 # Script principal que automatiza o cadastro de produtos
|-- produtos.csv            # Base de dados com os produtos a serem cadastrados
|-- README.md               # Documentação do projeto
```

## Exemplo do Arquivo `produtos.csv`

O arquivo CSV deve conter as seguintes colunas:

```
codigo,marca,tipo,categoria,preco_unitario,custo,obs
123,MarcaX,Eletrônico,Celular,1500,1200,Produto novo
456,MarcaY,Eletrônico,Notebook,3000,2500,Em promoção
```

## Observações

- Os campos do formulário são preenchidos utilizando a tecla "TAB" para navegar entre eles.
- Caso o campo de observação esteja vazio, ele será ignorado.
- O programa inclui tempos de espera (`time.sleep()`) para garantir que os elementos carreguem corretamente.

## Autor

Vinícius Vilela Novelo

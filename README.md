# Automacao de Login e Extracao de Dados

## Descricao
Este projeto automatiza o login em um site, extrai informacoes especificas e envia os dados por e-mail. A automacao utiliza Selenium para navegacao, Pandas para manipulacao de dados e smtplib para envio de e-mails.

## Estrutura do Projeto
```
rpa_project/
│── main.py                 # Arquivo principal que executa a automacao
│── config.py               # Configuracao de variaveis e caminhos
│── automation/
│   │── login.py            # Script de login automatizado
│   │── scraper.py          # Extracao de dados do site
│   │── email_sender.py     # Funcao para envio de e-mail
│── data/
│   │── credenciais.xlsx    # Planilha com usuarios e senhas
│── logs/
│   │── log.txt             # Arquivo de log das execucoes
│── requirements.txt        # Dependencias do projeto
│── README.md               # Documentacao do projeto
```

## Configuracao
### 1. Instalar dependencias
Execute o comando abaixo para instalar as bibliotecas necessarias:
```
pip install -r requirements.txt
```

### 2. Configurar variaveis de ambiente
Crie um arquivo `.env` na raiz do projeto e adicione:
```
EMAIL_REMETENTE=seuemail@gmail.com
EMAIL_SENHA=suasenha
EMAIL_DESTINATARIO=destinatario@email.com
```

### 3. Criar a planilha de credenciais
No diretorio `data/`, crie um arquivo `credenciais.xlsx` com o seguinte formato:
```
| usuario  | senha   |
|---------|--------|
| meuuser | 123456 |
```

### 4. Baixar o ChromeDriver
Baixe o ChromeDriver compatível com sua versao do Chrome:
[https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

Coloque o arquivo `chromedriver.exe` no diretorio raiz do projeto.

## Execucao
Para rodar o script, basta executar:
```
python main.py
```

O sistema realizara login, extraira os dados e enviara um e-mail com as informacoes obtidas.

## Logs
Todas as execucoes serao registradas no arquivo `logs/log.txt` para auditoria e depuracao.

## Possiveis Melhorias
- Adicionar OCR para captchas (Tesseract)
- Automatizar download de arquivos
- Criar um dashboard para monitorar os dados extraidos


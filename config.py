import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

CHROME_DRIVER_PATH = "chromedriver.exe"
URL_LOGIN = "https://exemplo.com/login"

# Credenciais
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")
EMAIL_DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")

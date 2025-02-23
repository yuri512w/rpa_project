import pandas as pd
import logging
from automation.login import login
from automation.scraper import extrair_dados
from automation.email_sender import enviar_email

# Configuração do log
logging.basicConfig(filename="logs/log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# 1. Ler credenciais da planilha
df = pd.read_excel("data/credenciais.xlsx")
usuario = df.loc[0, "usuario"]
senha = df.loc[0, "senha"]

# 2. Login no site
driver = login(usuario, senha)

# 3. Extração de dados
dados_extraidos = extrair_dados(driver)
print("Dados extraídos:", dados_extraidos)

# 4. Envio de e-mail
enviar_email(dados_extraidos)

# 5. Fechar navegador
driver.quit()

# 6. Log de sucesso
logging.info("Processo de automação concluído com sucesso.")

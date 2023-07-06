# Imagem base do Python
FROM python:3.9-slim

# diretório de trabalho na imagem do container
WORKDIR /app

# copiar os arquivos necessários para o diretório de trabalho
COPY . /app

# Instalar as dependências
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Definir a variável de ambiente para o caminho do arquivo de logs
ENV LOG_FILE_PATH /app/api_logs.log

# Copiar o arquivo openssl.cnf para o diretório apropriado dentro do contêiner
COPY openssl.cnf /etc/ssl/openssl.cnf

# Definir a variável de ambiente OPENSSL_CONF com o caminho correto
ENV OPENSSL_CONF /etc/ssl/openssl.cnf

# Instalar o servidor WSGI (Gunicorn)
RUN pip install gunicorn

# Expor a porta em que a API vai rodar
EXPOSE 5000

# Comando para iniciar a aplicação usando o Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api:app"]


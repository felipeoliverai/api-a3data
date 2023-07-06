# Imagem base do Python
FROM python:3.9-slim

# diretório de trabalho na imagem do container
WORKDIR /app

# copiar os arquivos necessários para o diretório de trabalho
COPY . /app

# instalar as dependências
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# definir fuso horário
RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

# variável de ambiente para o caminho do arquivo de logs
ENV LOG_FILE_PATH /app/api_logs.log

# copiar o arquivo openssl.cnf para o diretório dentro do contêiner
COPY openssl.cnf /etc/ssl/openssl.cnf

# variável de ambiente OPENSSL_CONF
ENV OPENSSL_CONF /etc/ssl/openssl.cnf

# instalar o servidor WSGI (Gunicorn)
RUN pip install gunicorn

# expor a porta em que a API vai rodar
EXPOSE 5000

# iniciar a aplicação usando o Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api:app"]


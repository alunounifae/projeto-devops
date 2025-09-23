# Imagem do Python
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar as dependências necessárias para dentro do container
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos para dentro do container
COPY . .

# Expor a porta que será utilizada pela API
EXPOSE 8000

# Executar comando para rodar a API utilizando o Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

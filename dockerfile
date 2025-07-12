FROM python:3.11-slim

# Installer wkhtmltopdf + dépendances système
RUN apt-get update && \
    apt-get install -y \
        wkhtmltopdf \
        libxrender1 \
        libxext6 \
        libfontconfig1 && \
    pip install flask pdfkit jinja2

# Créer le dossier app
WORKDIR /app
COPY . /app

# Exposer le port Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app.py"]

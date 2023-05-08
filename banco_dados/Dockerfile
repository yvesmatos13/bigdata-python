FROM mongo

RUN mkdir -p /app/data

WORKDIR /app/data

COPY formulario.csv /app/data

COPY script.sh /app/data

CMD ["mongod", "&&", "mongoimport", "-d", "bigdata", "-c", "formularios", "--file", "formulario.csv", "--headerline"]

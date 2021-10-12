

FROM python:3.8




RUN pip install --upgrade pip
# copiar requerimientos al directorio
COPY requirements.txt .
#instalar requerimientos de forma recurrente
#RUN pip3 install -r requirements.txt
RUN pip install -r requirements.txt


# exponer por el puerto 8501
EXPOSE 8501

COPY app/ . 


## descargar base de datos
#python

#CMD python aws.py
# Comando para ejecutar app
CMD streamlit run app.py

#ENTRYPOINT ["streamlit","run"]
#CMD ["main.py"]
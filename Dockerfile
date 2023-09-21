FROM python:3.8

RUN pip install aiogram==2.2 paramiko

WORKDIR /app
COPY . .

COPY remote_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
ENV SSH_PRIVATE_KEY=/root/.ssh/id_rsa

CMD ["python", "main.py"]
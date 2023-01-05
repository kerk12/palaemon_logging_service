FROM python:3.10

COPY requirements.txt /usr/share/app/
WORKDIR /usr/share/app
RUN pip install -r requirements.txt

COPY . /usr/share/app/

RUN chmod +x docker/web/entryfile.sh
ENTRYPOINT [ "docker/web/entryfile.sh" ]
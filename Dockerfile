FROM python:3.8.10

ADD . /pelican-site
WORKDIR /pelican-site
RUN pip install -r requirements.txt
EXPOSE 5051
CMD make serve-global PORT=5051

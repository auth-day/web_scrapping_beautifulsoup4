FROM python:3

COPY web_scrapping.py /

ENTRYPOINT [ "python3", "web_scrapping.py" ]

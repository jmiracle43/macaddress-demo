FROM python:3.7.4-alpine

WORKDIR /usr/src/app

COPY src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD [""]
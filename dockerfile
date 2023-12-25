FROM python:slim

WORKDIR /usr/src/app

COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

RUN mkdir /usr/src/app/config/
RUN chmod a+x entry_point.sh health_check.sh

HEALTHCHECK CMD /usr/src/app/health_check.sh

ENTRYPOINT ["./entry_point.sh"]

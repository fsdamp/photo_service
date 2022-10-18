###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.6 as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev
RUN pip install --upgrade pip

COPY . .
RUN mkdir -p /usr/logs

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########
FROM python:3.9.6-buster
# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media

WORKDIR $APP_HOME

# install dependencies

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh
RUN ["chmod", "+x", "/home/app/web/entrypoint.sh"]
RUN chmod 775 $APP_HOME/entrypoint.sh
# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME
RUN chmod 777 $APP_HOME
RUN chmod 777 $APP_HOME/media
RUN chmod 777 $APP_HOME/static

# install utils
RUN apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 netcat supervisor nano
RUN chmod -R 777 /usr/local
# change to the app user
USER app
RUN chmod 777 $APP_HOME
RUN chmod 777 $APP_HOME/media
RUN chmod 777 $APP_HOME/static
RUN chown -R app:app $APP_HOME

# run entrypoint.prod.sh
ENTRYPOINT ["sh", "/home/app/web/entrypoint.sh"]

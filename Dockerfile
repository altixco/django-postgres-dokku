FROM python:3.7

# For localizations
RUN apt-get update
RUN apt-get install gettext -y

RUN mkdir /src
COPY requirements.txt /src/
RUN pip install -r /src/requirements.txt

COPY . /src
WORKDIR /src

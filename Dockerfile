FROM python:3.7

# For webpack
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get update -qq
RUN apt-get install nodejs -y

# For localizations
RUN apt-get install gettext -y

RUN mkdir /src
WORKDIR /src

COPY package.json /src/
RUN npm install

COPY requirements.txt /src/
RUN pip install -r /src/requirements.txt

COPY . /src

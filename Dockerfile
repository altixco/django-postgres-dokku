FROM python:3.7
ENV PYTHONUNBUFFERED=1

# For node
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get update

# For localizations
RUN apt-get install gettext -y

# For webpack (to generate bundles)
RUN apt-get install nodejs -y

# Setup workdir
RUN mkdir /src
WORKDIR /src

# JS dependencies
COPY package.json /src/
RUN npm install

# Python dependencies
COPY requirements.txt /src/
RUN pip install -r /src/requirements.txt

COPY . /src

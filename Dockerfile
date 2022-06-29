FROM python:3.8.8

RUN mkdir /appium

COPY ./ /appium

COPY ./requirements.txt /appium

WORKDIR /appium
RUN pip install pip --upgrade &&  pip install -r requirements.txt
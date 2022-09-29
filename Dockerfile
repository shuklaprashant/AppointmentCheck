FROM python:3.7-alpine

ENV PYTHONBUFFERED 1
ENV TWILIO_ACCOUNT_SID=""
ENV TWILIO_AUTH_TOKEN=""

COPY ./requirement.txt /requirement.txt

RUN python -m pip install -r /requirement.txt

RUN mkdir /automation
COPY ./app /app
WORKDIR /app


# CMD ["python", "./appointment.py"]

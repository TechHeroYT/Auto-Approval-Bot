# Don't Remove Credit @hero_botss
# Subscribe YouTube Channel For Amazing Bot @bots_repo
# Ask Doubt on telegram @hero_botss

FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 bot.py

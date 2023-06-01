FROM python:latest
LABEL maintainer="hieunguyen810"

RUN pip3 install pyautogui
RUN pip3 install sklearn
RUN pip3 install pandas

RUN mkdir /home/kanji
COPY index.py /home/kanji 
COPY recognizer.py /home/kanji
COPY Kanji_dataset /home/kanji

WORKDIR /home/kanji

CMD ["python3", "./index.py"]
